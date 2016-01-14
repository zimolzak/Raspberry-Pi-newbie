from telnetlib import Telnet
import time
tn = Telnet('192.168.1.15', 13666, None)

#tn.interact()

tn.write("hello\n")
tn.write("screen_add s1\n")
tn.write("screen_set s1 -priority 1\n")
tn.write("widget_add s1 w1 title\n")
tn.write("widget_add s1 w2 string\n")
tn.write("widget_set s1 w1 {YEH}\n")
tn.write("widget_set s1 w2 4 2 {MAN}\n")
print "sleeping"
time.sleep(10)
