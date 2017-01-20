## usage:
##    python3 check_wifi.py &

from subprocess import check_output, CalledProcessError, STDOUT
import re
import time
import logging

logging.basicConfig(filename='../wlan_resets.log',level=logging.INFO)

ips_to_ping = ['8.8.8.8', '192.168.1.1']
sleep_seconds = 15 * 60

def print_exception(e):
    logging.info('object\t' + str(e))
    logging.info('type  \t' + str(type(e)))
    if type(e) == CalledProcessError:
        logging.info('args  \t' + str(e.args))
        logging.info('cmd   \t'  + str(e.cmd))
        logging.info('output\t' + e.output.decode('utf-8').replace('\n','\\n'))
        logging.info('r-code\t' + str(e.returncode))
        if hasattr(e, 'stderr'):
            logging.info('stderr\t'  + str(e.stderr))
        if hasattr(e, 'stdout'):
            logging.info('stdout\t'  + str(e.stdout))
        if hasattr(e, 'message'):
            logging.info('message\t'  + str(e.message))
        if (not hasattr(e, 'stderr')) and (not hasattr(e, 'stdout')):
            logging.info(str(dir(e)))
    else:
        logging.info(str(dir(e)))

while(True):
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S") + " --------")
    commands = ['ping -c 4 ' + ip for ip in ips_to_ping]
    try:
        outs = [check_output(cmd.split()) for cmd in commands]
    except CalledProcessError:
        logging.info('>= 1 ping returned error, poss because 0 packets')
        try:
            output = check_output(['wpa_cli', 'reassociate'], stderr=STDOUT)
        except Exception as e:
            print_exception(e)
        else:
            logging.info('wpa_cli success!!')
            logging.info('wpa_cli says ' + str(output))
        time.sleep(sleep_seconds)
        continue
    for j, b in enumerate(outs):
        for line in b.splitlines():
            if 'packet loss' in str(line):
                s = str(line)
                search = re.search(r'(\d+)% packet loss', str(b))
                n = int(search.group(1)) # 1st parenth'd subgroup
                logging.info(ips_to_ping[j] + '\t' + str(n) + ' loss')
    time.sleep(sleep_seconds)
