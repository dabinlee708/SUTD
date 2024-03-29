# Name : James Denny Wiryo & Dabin Lee
# Student ID : 1000457 & 1000727

# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

#constants
fullround=32

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]


#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]


#S-Box Inverse
sbox_inv =[0x5, 0xE, 0xF, 0x8, 0xC, 0x1, 0x2, 0xD, 0xB, 0x4, 0x6, 0x3, 0x0, 0x7, 0x9, 0xA]

#pLayer Inverse
pmt_inv = [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 1, 5, 9, 13, 17, 21,\
 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54,\
  58, 62, 3, 7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55, 59, 63]


# Rotate left: 0b1001 --> 0b0011
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))

# Rotate right: 0b1001 --> 0b1100
ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))

def genRoundKeys(key):
    roundkeys = []
    for i in xrange(1,fullround+1):
        roundkeys.append(key >>16)
        key = ((key & (2**19-1)) << 61) + (key >> 19)
        key = (sbox[key >> 76] << 76)+(key & (2**76-1))
        key ^= i << 15
    return roundkeys

def addRoundKey(state,Ki):
    state = state ^ Ki
    return state

def sBoxLayer(state):
    sBoxOut = 0

    for i in xrange(16):
        sBoxOut += sbox[( state >> (i*4)) & 0x0F] << (i*4)
    #print str(sBoxOut)
    #print int(sBoxOut, base = 2)
    return sBoxOut

def pLayer(state):
    pLayerOut= 0

    for i in xrange(64):
        pLayerOut += ((state >> i) & 0x01) << pmt[i]
    return pLayerOut

def present_rounds(plain, key, rounds):
    roundkeys=genRoundKeys(key)
    #print "plain = " + str(plain)
    state = plain
    #print "state = " + str(state)
    for i in xrange (rounds-1):
        state = addRoundKey(state,roundkeys[i])
        #print "state = " + str(state)
        state = sBoxLayer(state)
        state = pLayer(state)
    cipheredText = addRoundKey(state,roundkeys[-1])
    return cipheredText

def sBoxLayer_inv(state):
    sBoxInvOut = 0

    for i in xrange(16):
        sBoxInvOut += sbox_inv[( state >> (i*4)) & 0x0F] << (i*4)
    return sBoxInvOut

def pLayer_inv(state):
    pLayerInvOut = 0
    for i in xrange(64):
        pLayerInvOut += ((state >> i) & 0x01) << pmt_inv[i]
    return pLayerInvOut

def present_rounds_inv(plain, key, rounds):
    roundkeys=genRoundKeys(key)
    state = plain
    for i in xrange (fullround-1):
        state = addRoundKey(state,roundkeys[-i-1])
        state = pLayer_inv(state)
        state = sBoxLayer_inv(state)
    decipheredText = addRoundKey(state,roundkeys[0])
    return decipheredText


def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(plain, key):
    return present_rounds_inv(plain, key, fullround)



if __name__=="__main__":
    plain1=0x0000000000000000
    key1=0x00000000000000000000
    cipher1= present(plain1,key1)
    plain11 = present_inv(cipher1,key1)
    print format(cipher1,'x')
    print format(plain11,'x')
    plain2=0x0000000000000000
    key2=0xFFFFFFFFFFFFFFFFFFFF
    cipher2= present(plain2,key2)
    plain22 = present_inv(cipher2,key2)
    print format(cipher2,'x')
    print format(plain22,'x')
    plain3=0xFFFFFFFFFFFFFFFF
    key3=0x00000000000000000000
    cipher3= present(plain3,key3)
    plain33 = present_inv(cipher3,key3)
    print format(cipher3,'x')
    print format(plain33,'x')
    plain4=0xFFFFFFFFFFFFFFFF
    key4=0xFFFFFFFFFFFFFFFFFFFF
    cipher4= present(plain4,key4)
    plain44 = present_inv(cipher4,key4)
    print format(cipher4,'x')
    print format(plain44,'x')
