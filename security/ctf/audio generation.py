import wave
import random
import struct

noise_output = wave.open('encrypted_audio.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))
cleartext=[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
encode=[]
for a in cleartext:
	if a==1:
		for a in range(1,100):
			encode.append(-32000)
	else:
		for a in range(1,100):
			encode.append(32000)
	for a in range(1,100):
		encode.append(0)

for a in encode:
	packed_value = struct.pack('h',a)
	noise_output.writeframes(packed_value)
noise_output.close()