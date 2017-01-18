from subprocess import check_output, CalledProcessError
import re
import time

ips_to_ping = ['8.8.8.8', '192.168.1.1']
sleep_seconds = 15 * 60

while(True):
    print(time.strftime("%Y-%m-%d %H:%M:%S") + " --------")
    commands = ['ping -c 4 ' + ip for ip in ips_to_ping]
    try:
        outs = [check_output(cmd.split()) for cmd in commands]
    except CalledProcessError:
        print('one or both pings returned error, poss because 0 packets')
        ### wpa_cli reassociate
        time.sleep(sleep_seconds)
        continue
    for j, b in enumerate(outs):
        for line in b.splitlines():
            if 'packet loss' in str(line):
                s = str(line)
                search = re.search(r'(\d+)% packet loss', str(b))
                n = int(search.group(1)) # 1st parenth'd subgroup
                print(ips_to_ping[j], '\t', n, 'loss')
    time.sleep(sleep_seconds)
