import wave
import random
import struct
import binascii




flag_string="FLAG{WE_NEED_TO_GO_DEEPER}"
bin_flag_string=bin(int(binascii.hexlify(flag_string), 16))
# print bin_flag_string
# print bin_flag_string[2:]

frameLength=len(flag_string)*3200

noise_output = wave.open('clear_we_need_to_go_deeper.wav', 'w')
noise_output.setparams((1, 2, 44100, frameLength, 'NONE', 'not compressed'))

bin_flag_list=[]

for i in bin_flag_string[2:]:
	bin_flag_list.append(int(i))
print bin_flag_list
# cleartext=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
encode=[]
print bin_flag_string, len(bin_flag_string[2:])

for a in bin_flag_string[2:]:
	# print a
	if a=='0':
		encode.append(-32000)
		# for a in range(1,100):
			# encode.append(-32000)
	if a=='1':
		encode.append(32000)
		# for a in range(1,100):
			# encode.append(32000)
	# for a in range(1,100):
		# encode.append(0)
	# encode.append(0)
	# print encode
# print encode, len(encode)
for a in encode:
	# print a
	packed_value = struct.pack('h',a)
	noise_output.writeframes(packed_value)
noise_output.close()