#!/bin/python3
#coded by U4I5 For pentesting
import os
import subprocess

kali = os.system
#Target Ip address
Iptarget = input('[+] Target: ')
#Interface
Iface = input("[+] Iface: ")

if Iface == 0:
    Iface = "eth0"

#1- fast Scan nmap
kali("nmap" + " " "-sV" + " " "-sC"  + " " 'T4' + " " format(Iptarget) )

#2- Full Scan nmap  
# kali(f"nmap" + "-p-" "-sV" + "-sC" +  str('T4')+ {Iptarget} + "-oN" + {Iptarget}.txt)
