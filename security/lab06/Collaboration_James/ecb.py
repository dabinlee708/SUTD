# ECB wrapper
 # skeleton file for 50.020 Security
# Oka, SUTD, 2014

# Dabin Lee 1000727
# James Wiryo 1000457
# Security Lab 6


from present import *
import argparse

key = 0x00000000000000000000
nokeybits=80
blocksize=64

def ecb(infile,outfile,key,mode):
    # prepare for data processing
    lol=""

    # initialize file 
    file = open(infile,"r")

    # Read the file
    tux_ex_head=file.read()
    lol=tux_ex_head.encode('hex')

    # if it isn't multiples of 16, add padding lol
    remainder=len(lol)%16
    padding=16-remainder

    # in case the padding is necessary, add zeros
    if padding!=0:

        finalPadding=padding*('0')
        body_padded=lol+finalPadding
    
    else:

        body_padded=lol

    # Initialize needed containers for encrypted and decrypted blocksize
    encrypted_split_data=[]
    decrypted_split_data=[]

    # Split the data into processable blocks
    split_data=map(''.join, zip(*[iter(body_padded)]*16))

    
    # Encryption 
    for split_block in split_data:
        # Encrypt the block in hex with a key 
        encrypted_block = present(int(split_block,16),key)
        # Append the encrypted block to the encrypted_split_data list
        encrypted_split_data.append(encrypted_block)
    
    # Decryption
    for block_decrypt in encrypted_split_data:
        decrypted_block = present_inv(block_decrypt,key)
        decrypted_split_data.append(decrypted_block)

    Decrypted_data_after_convertion=""

    for each in decrypted_split_data:
        
        eachone = str("{0:x}".format(each))

        if len(eachone)!=16:
            # print each
            eachone = '0'*(16-len(eachone))+eachone
        Decrypted_data_after_convertion+=eachone

    Decrypted_data_after_convertion=Decrypted_data_after_convertion[:-padding]
    Decrypted_result=Decrypted_data_after_convertion.decode("hex")

    output = open ( outfile, "w")
    output.write(Decrypted_result)
    output.close()







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

    ecb(infile,outfile,key,'EBD')

