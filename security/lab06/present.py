# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

#constants
fullround=31
roundCounter=0b010101

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]

#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]

# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))
 
# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

# keys={}
def binary(num, pre='0b', length=8, spacer=0):
    return '{0}{{:{1}>{2}}}'.format(pre, spacer, length).format(bin(num)[2:])

def xor( a, b ):
    return (a or b) and not (a and b)

def genRoundKeys(key):
    roundKeyLists=[]
    roundKeyLists.append(key>>16)
    for i in range(1,32):
        # print "Original Key: ",binary(key,'0b',80,0)
        step=rol(key,61,80)
        # print "Step 1   key: ",binary(step1,'0b',80,0)
        step=int(bin(sBoxLayer(binary(step,'0b',80,0)[2:6]))+binary(step,'0b',80,0)[6:82],2)
        # print "Step 2   key: ",binary(step2,'0b',80,0)
        step=(step ^ (i << 15))
        roundKeyLists.append(step >> 16)
    for x in roundKeyLists:
        print binary(x,'0b',64,0)
    return roundKeyLists

    
    print "Step 3   key: ",binary(step2,'0b',80,0)[0:63]+\
    ''.join('0' if i == j else '1' for i, j in zip(a,b))+\
    binary(step2,'0b',80,0)[68:]

def addRoundKey(state,Ki):
    return state ^ ki

def sBoxLayer(state):
    # postSBox=0
    # for i in range(0,16):
    #     output+=sbox[(state >>)]
    return sbox[int(state)]

def pLayer(state):
    pass

def present_rounds(plain, key, rounds):
    pass

def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(plain, key):
    pass

key=0xaaaaaaaaaa0000000000
genRoundKeys(key)
# for i in range(16):
#     print sbox[i]

# if __name__=="__main__":
#     rval=rol(0b1001,1,4)
#     print "result of rol is %x"%rval
#     plain1=0x0000000000000000
#     key1=0x00000000000000000000
#     cipher1= present(plain1,key1)
#     plain11 = present_inv(cipher1,key1)
#     print format(cipher1,'x')
#     print format(plain11,'x')
#     plain2=0x0000000000000000
#     key2=0xFFFFFFFFFFFFFFFFFFFF
#     cipher2= present(plain2,key2)
#     plain22 = present_inv(cipher2,key2)
#     print format(cipher2,'x')
#     print format(plain22,'x')
#     plain3=0xFFFFFFFFFFFFFFFF
#     key3=0x00000000000000000000
#     cipher3= present(plain3,key3)
#     plain33 = present_inv(cipher3,key3)
#     print format(cipher3,'x')
#     print format(plain33,'x')
#     plain4=0xFFFFFFFFFFFFFFFF
#     key4=0xFFFFFFFFFFFFFFFFFFFF
#     cipher4= present(plain4,key4)
#     plain44 = present_inv(cipher4,key4)
#     print format(cipher4,'x')
#     print format(plain44,'x')


