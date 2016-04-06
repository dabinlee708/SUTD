import binascii
import wave
import struct
import scipy.io.wavfile as wavfile

# wavFile = wave.open('encrypted_front.wav','r')
rate, data = wavfile.read('encrypted_front.wav')
# data0 is the data from channel 0.
data0 = data[:, 0]
cleaned_list=data0[:207]
cleaned_data=""
for a in cleaned_list:
	if a > 0:
		cleaned_data+='1'
	if a < 0:
		cleaned_data+='0'
	else:
		pass
bin_cleaned_data=int(cleaned_data,2)
# print cleaned_data
print "decrypted:",binascii.unhexlify('%x' % bin_cleaned_data)

data=0b100011001001100010000010100011101111011010101110100010101011111010011100100010101000101010001000101111101010100010011110101111101000111010011110101111101000100010001010100010101010000010001010101001001111101

print "answerkey:",binascii.unhexlify('%x' % data)