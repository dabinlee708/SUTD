# Name : James Denny Wiryo & Dabin Lee
# Student ID : 1000457 & 1000727


# ECB plaintext extraction skeleton file for 50.020 Security
# Oka, SUTD, 2014

import argparse
import binascii


def getInfo(headerfile):

    with open(headerfile, "rb") as image:
        img = image.read()
    image.close()
    return img

def extract(infile,outfile,headerfile):
    # read the contents of letter.e
    with open(infile, "rb") as image:
        img = image.read()
    # close after reading the content of letter.e
    image.close()

    # Convert the content to hex
    imghex = binascii.hexlify(img)

    # Skip the header and start from the content
    imghex = imghex[32:]

    # split into blocks
    String_map = map(''.join, zip(*[iter(imghex)]*16))

    # Set values for necessary variables
    string = ""
    mapping_var1="11111111"
    mapping_var2="00000000"

    for i,j in enumerate(String_map):
        if j == "7aa10bff92fd4179":
            String_map[i] = mapping_var1
        else:
            String_map[i] = mapping_var2
        string = string + String_map[i]

    headerString = getInfo(headerfile)

    # Output file
    n = open(outfile, "w")
    # Write to file with header
    n.write(headerString+"\n")
    # Write contents to the file
    n.write(string)
    # Close the file afte finishing write
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
