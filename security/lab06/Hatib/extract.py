# ECB plaintext extraction skeleton file for 50.020 Security
# Oka, SUTD, 2014

#Muhammad Hatib  1000607
#Francisco Furtado 1000560

import argparse
import binascii


def getInfo(headerfile):
    #get contents of headerfile
    with open(headerfile, "rb") as imageFile:
        f = imageFile.read()
    return f

def extract(infile,outfile,headerfile):
    #get contents of letter.e without header
    with open(infile, "rb") as imageFile:
        f = imageFile.read()
    g = binascii.hexlify(f) # change to hex
    g = g[32:] #remove header
    #split chunkcs into chunks of 16 according to pattern found
    string = map(''.join, zip(*[iter(g)]*16))
    one  = "7aa10bff92fd4179"
    fin = ""
    for n,i in enumerate(string):
        #check pattern and replace with respective digits
        if i == one:
            string[n] = "11111111"
        else:
            string[n] = "00000000"
        fin+= string[n]
    #write to file with header attached
    headStr = getInfo(headerfile)
    n = open(outfile, "w")
    n.write(headStr+"\n")
    n.write(fin)
    n.close()


if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Extract PBM pattern.')
    parser.add_argument('-i', dest='infile',help='input file, PBM encrypted format')
    parser.add_argument('-o', dest='outfile',help='output PBM file')
    parser.add_argument('-hh', dest='headerfile',help='known header file')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    headerfile=args.headerfile

    print 'Reading from: ',infile
    print 'Reading header file from: ',headerfile
    print 'Writing to: ',outfile

    success=extract(infile,outfile,headerfile)
