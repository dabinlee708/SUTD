# ECB wrapper skeleton file for 50.020 Security
# Oka, SUTD, 2014
from present import *
import argparse

nokeybits=80
blocksize=64


def ecb(infile,outfile,key,mode):
    if not infile:
        return "u need to enter infile"
    file=open(infile,'rb')
    f=file.read()
    plain="".join(c.encode('hex') for c in f)

    k=open(key,'rb').read()
    key=int("".join(c.encode('hex') for c in k))
    if mode == 'e':
        ciphertext=""
        for i in range(len(plain)/16 +1):
            plainint=int(plain[16*i:16*i+16],16)
            cipher1=present(plainint, key)
            if len(format(cipher1,'x'))%2==0:
                ciphertext+=format(cipher1,'x').decode('hex')
            else:
                ciphertext+=("0"+format(cipher1,'x')).decode('hex')


        file=open(outfile,'wb')
        file.write(ciphertext)
        file.close()
        print "done"


    if mode == 'd':
        deciphertext=""
        for i in range(len(plain)/16 +1):
            if plain[16*i:16*i+16]!='':
                plainint=int(plain[16*i:16*i+16],16)
                decipher1=present_inv(plainint, key)
                if len(format(decipher1,'x'))%2==0:
                    deciphertext+=format(decipher1,'x').decode('hex')
                else:
                    deciphertext+=("0"+format(decipher1,'x')).decode('hex')

        file=open(outfile,'wb')
        file.write(deciphertext)
        file.close()

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
    mode=args.mode
    ecb(infile, outfile, keyfile, mode)
