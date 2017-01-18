## usage:
##    python3 check_wifi.py &

from subprocess import check_output, CalledProcessError
import re
import time
import logging

logging.basicConfig(filename='../wlan_resets.log',level=logging.INFO)

ips_to_ping = ['8.8.8.8', '192.168.1.1']
sleep_seconds = 15 * 60

while(True):
    logging.info(time.strftime("%Y-%m-%d %H:%M:%S") + " --------")
    commands = ['ping -c 4 ' + ip for ip in ips_to_ping]
    try:
        outs = [check_output(cmd.split()) for cmd in commands]
    except CalledProcessError:
        logging.info('one or both pings returned error, poss because 0 packets')
        output = check_output(['wpa_cli', 'reassociate'])
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
