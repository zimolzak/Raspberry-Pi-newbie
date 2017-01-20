## usage:
##    python3 check_wifi.py &

from subprocess import check_output, CalledProcessError, STDOUT
import re
import time
import logging

logging.basicConfig(filename='../wlan_resets.log',level=logging.INFO)

ips_to_ping = ['8.8.8.8', '192.168.1.66']
sleep_seconds = 15 * 60

def print_exception(e):
    print('object\t', e)
    print('type\t', type(e))
    if type(e) == CalledProcessError:
        print('args\t', e.args)
        print('cmd\t' , e.cmd)
        print('output\t', e.output.decode('utf-8').replace('\n','\\n'))
        print('r-code\t', e.returncode)
        print('stderr\t' , e.stderr)
        print('stdout\t' , e.stdout)
    else:
        print(dir(e))

while(True):
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S") + " --------")
    commands = ['ping -c 4 ' + ip for ip in ips_to_ping]
    try:
        outs = [check_output(cmd.split()) for cmd in commands]
    except CalledProcessError:
        logging.info('>= 1 ping returned error, poss because 0 packets')
        try:
            output = check_output(['wpa_cli', 'reassociatexxx'], stderr=STDOUT)
        except Exception as e:
            print_exception(e)
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
