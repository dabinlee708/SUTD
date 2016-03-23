# Present skeleton file for 50.020 Security
# Oka, SUTD, 2014

#Muhammad Hatib     1000607
#Francisco Furtado  1000560


#constants
fullround=31

#S-Box Layer
sbox=[0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]
#S-Box decrypt Layer
sbox_inv = [sbox.index(x) for x in xrange(16)]

#PLayer
pmt=[0,16,32,48,1,17,33,49,2,18,34,50,3,19,35,51,\
     4,20,36,52,5,21,37,53,6,22,38,54,7,23,39,55,\
     8,24,40,56,9,25,41,57,10,26,42,58,11,27,43,59,\
     12,28,44,60,13,29,45,61,14,30,46,62,15,31,47,63]
#PLayer decrypt
pmt_inv = [pmt.index(x) for x in xrange(64)]

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
    roundkeys.append(key>>16) # firstkey
    for i in range(1,32):
        #61 bit rotate left
        nextKey = rol(key, 61 ,80)
        #S Rounds
        nextKey = (sbox[nextKey >> 76] << 76) + (nextKey & (2**76-1))
        #XOR Round
        nextKey = (nextKey ^ (i << 15))
        #Generating key from the 80 bits
        roundkeys.append(nextKey >> 16)
    return roundkeys

def addRoundKey(state,Ki): #done
    return state ^ Ki

def sBoxLayer(state): #done
    output = 0
    for i in range(16):
        output += sbox[(state >> (i*4)) & 0xF] << (i*4)
    return output

def sBoxLayer_dec(state): #done
    output = 0
    for i in range(16):
        output += sbox_inv[(state >> (i*4)) & 0xF] << (i*4)
    return output

def pLayer(state):#done
    output = 0
    for i in range(64):
        output += ((state >> i) & 0x01) << pmt[i]
    return output

def pLayer_dec(state):#done
    output = 0
    for i in range(64):
        output += ((state >> i) & 0x01) << pmt_inv[i]
    return output

def present_rounds(plain, key, rounds):
    keys = genRoundKeys(key)

    state = plain
    for k in keys[:-1]:
        state = addRoundKey(state,k)
        state = sBoxLayer(state)
        state = pLayer(state)

    return addRoundKey(state,keys[rounds])


def present(plain, key):
    return present_rounds(plain, key, fullround)

def present_inv(plain, key):
    keys = genRoundKeys(key)
    state = plain
    for k in range(31):

        state = addRoundKey(state,keys[-k-1])
        state = pLayer_dec(state)
        state = sBoxLayer_dec(state)

    return addRoundKey(state,keys[0])


if __name__=="__main__":
    plain1=0x3617856288059634
    key1=0x00000000000000000000
    print plain1.encode("hex")
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
