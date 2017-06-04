# -*- coding: utf-8 -*-
"""
Created on Fri May 12 14:51:18 2017

@author: dawkiny
"""

import uuid

print(':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff) for i in range(0,8*6,8)][::-1]))


#%%

arp -a 121.133.174.210
nbtstat -A 121.133.174.210
nmap -v -A 121.133.174.210

#%%

from subprocess import Popen, PIPE
import re
IP = "121.133.174.210"

pid = Popen(["ip", "neigh", "show", IP], stdout=PIPE)
s = pid.communicate()[0]
mac = re.search(r"(([a-f\d]{1,2}\:){5}[a-f\d]{1,2})", s).groups()[0]
mac
"fe:fd:61:6b:8a:0f"


#%%

import subprocess
import sys
 
ip = sys.argv[1]
    
# ping ip
p = subprocess.Popen(['ping', ip, '-c1'], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
 
out, err = p.communicate()
 
# arp list
p = subprocess.Popen(['arp', '-n'], stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)
 
out, err = p.communicate()
 
try:
    arp = [x for x in out.split('\n') if ip in x][0]
except IndexError:
    sys.exit(1)     # no arp entry found
else:
    # get the mac address from arp list
    # bug: when the IP does not exists on the local network
    # this will print out the interface name
    print ' '.join(arp.split()).split()[2]

#%%

import subprocess
import sys
remotehost="121.133.174.210"
cmd="nbtstat -A"
p=subprocess.Popen(cmd + remotehost, shell=True, stdout=subprocess.PIPE)
output, errors = p.communicate()


if output is not None :
    output = output.decode('cp949')
    if sys.platform in ['linux','linux2']:
        for i in output.split("\n"):
            if remotehost in i:
                for j in i.split():
                    if ":" in j:
                        print( "%s--> %s" % (remotehost,j))
    elif sys.platform in ['win32']:
        item =  output.split("\n")[-2]
        if remotehost in item:
            print("%s-->  %s" %(remotehost, item.split()[1]))


#%%
address = "121.133.174.210"
 "".join(c + ":" if i % 2 else c for i, c in enumerate(hex(address)[2:].zfill(12)))[:-1]

from uuid import getnode 
mac_addr = hex(uuid.getnode()).replace('0x', '')
':'.join(mac_addr[i : i + 2] for i in range(0, 11, 2))

#%%

import subprocess
ret = subprocess.call(["ssh", "pydemia@host", "program"]);

#%%

from subprocess import Popen, PIPE
import re
import sys


if ip is None:
    ip = "121.133.174.210"
else:
    ip = sys.argv[1]


Popen(["ping", "-c 1", ip], stdout = PIPE)
pid = Popen(["nbtstat", "-A", ip], stdout = PIPE)
msg = pid.communicate()[0].decode('cp949')
mac = re.search('(?<=MAC 주소 = )'+'\w+-'*5 + '\w+', msg).group()

print("%s --> %s" % (IP, mac))


[i for i in range(5)]
[i*2 for i in range(5) if i % 2]
