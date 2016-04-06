import binascii
import wave
import struct
import scipy.io.wavfile as wavfile

# wavFile = wave.open('encrypted_front.wav','r')
rate, data = wavfile.read('onion.wav')
# data0 is the data from channel 0.
data0 = data[:, 1]
print data0[:159], len(data0[:159])

cleaned_list=data0[:159]
cleaned_data=""
for e in cleaned_list:
	if e > 0:
		cleaned_data+='1'
	else:
		cleaned_data+='0'
# print cleaned_data
# print ''.join(chr(int(cleaned_data[i:i+8], 2)) for i in xrange(0, len(cleaned_data), 8))
# print cleaned_data
bin_cleaned_data=int(cleaned_data,2)
# print cleaned_data
# print "decrypted:"
print "decrypted:",binascii.unhexlify('%x' % bin_cleaned_data)

data=0b100011001001100010000010100011101111011010101110100010101011111010011100100010101000101010001000101111101010100010011110101111101000111010011110101111101000100010001010100010101010000010001010101001001111101
print "answerkey:",binascii.unhexlify('%x' % data)