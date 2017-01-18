from subprocess import check_output, CalledProcessError
import re

ping8 = "ping -c 4 8.8.8.8"
ping1 = "ping -c 4 192.168.1.1"

try:
    outs = [check_output(x.split()) for x in [ping8, ping1]]
except CalledProcessError:
    print('one or both pings returned error, poss because 0 packets')
    quit()

for b in outs:
    for line in b.splitlines():
        if 'packet loss' in str(line):
            s = str(line)
            search = re.search(r'(\d+)% packet loss', str(b))
            n = int(search.group(1)) # 1st parenth'd subgroup
            print(n)
