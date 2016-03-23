# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014

#Muhammad Hatib     1000607
#Francisco Furtado  1000560


from present import *
import argparse
import binascii

nokeybits=80
blocksize=64
key = 0x00000000000000000000

def ecb(infile,outfile,key,mode):
    body = ''
    # read file
    ppm = open(infile, "r")
    Tuxbody = ppm.read()
    #encode from ASCII to hex values
    body = Tuxbody.encode("hex")

    #check if hex is a multiple of 16. if not, add padding
    padding = 16-(len(body)%16)
    if padding!=0:
        bodypad = body+ ('0')*(padding)
    else:
        bodypad = body

    #split hex values into chunks of 16 digits
    data = map(''.join, zip(*[iter(bodypad)]*16))
    print data
    #encrypt data
    encryptedData = []
    for x in data:
        enc = present(int(x,16),key)
        encryptedData.append(enc)

    #decrypt data
    decryptedData = []
    for y in encryptedData:
        dec = present_inv(y,key)
        decryptedData.append(dec)

    #convert decimal values to hex values
    decryptedFullData = ''
    for j in decryptedData:
        hexJ = str("{0:x}".format(j))
        #check if hex values are 16 digits long, if not add leading 0s
        if len(hexJ)!=16:
            hexJ = '0'*(16-len(hexJ)) + hexJ

        decryptedFullData += hexJ

    #minus the padding added
    decryptedFullData=decryptedFullData[:-padding]
    #decode from hex to ASCII
    decryptedBody = decryptedFullData.decode("hex")

    #output to file
    output = open(outfile, "w")
    output.write(decryptedBody)
    output.close()

    print 'Decode file is '+outfile


if __name__=="__main__":
    parser=argparse.ArgumentParser(description='Block cipher using ECB mode.')
    parser.add_argument('-i', dest='infile',help='input file')
    parser.add_argument('-o', dest='outfile',help='output file')
    parser.add_argument('-k', dest='keyfile',help='key file')
    parser.add_argument('-m', dest='mode',help='mode')

    args=parser.parse_args()
    infile=args.infile
    outfile=args.outfile
    keyfile=args.keyfile

    print 'Reading from: ',infile
    print 'Writing to: ',outfile

    ecb(infile,outfile,key,'EBD')

