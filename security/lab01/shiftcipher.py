#!/usr/bin/env python
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse

def doStuff(filein,fileout,mode,key):
    # open file handles to both files
    fin  = open(filein)       # by default, read mode
    fout = open(fileout,'w')  # write mode
    c    = fin.read()         # read in file into c

    outputString=""
    print key, mode, type(mode)
    if int(key)<0 or int(key)>255:
        print "please input a correct key within 0 to 255"
    else:
        print mode.lower()
        if mode.lower()!="e" and mode.lower()!="d":
            print "Error: key in either e or d"
        else:
            if mode.lower() == "e":
                key=int(key)
            elif mode.lower() =="d":
                key=int(key)*-1
            for a in c:
                outputString+=chr((ord(a)+key)%256)
            fout.write(outputString)



    # if key>=0 or key<=255:
    #     if mode.lower()=="e":
    #         for a in c:
    #             outputString+=chr((ord(a)+int(key)%256)
    #     elif mode.lower()=="d":
    #         for a in c:
    #             outputString+=chr((ord(a)-int(key)%256)
    #     else:
    #         print "Wrong mode. Please select either 'e' for encryption or 'd' for decryption."
    #     fout.write(outputString)

    # else:
    #     print "key can be 0 - 255"

    # and write to fileout

# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key')
    parser.add_argument('-m', dest='mode', help='mode')
    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key=args.key
    mode=args.mode

    doStuff(filein,fileout,mode,key)

    # all done

    
