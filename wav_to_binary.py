import wave
import matplotlib.pyplot as plt
import numpy as np
import struct
import os
import matplotlib.pyplot as plt

w = wave.open("sound_files/pluck.wav", "rb")
binary_data = w.readframes(w.getnframes())
w.close()

int_data_full = list(binary_data)
int_data_cut = int_data_full[0:1000]

###### Choose whether to use the entire bitstream or a curtailed version #######

# curr_data = int_data_cut
curr_data = int_data_full

bitstream = bytes(curr_data)

###################### Display the resulting binary string #####################

# print(bitstream)

#################################### PLOT ######################################

plt.plot(curr_data)
plt.show()

######################### Save bitstream as a .txt file ########################

with open('bitstreams/input_bitstream.txt', 'w') as file:
    file.write(str(bitstream))

################################ PLAY SOUND ####################################

# Specify the audio parameters
sample_rate = 44100  # samples per second
duration = 5.0  # seconds
bits_per_sample = 24  # number of bits per sample

# Pad the bitstream with zeros if necessary
if len(bitstream) % 2 != 0:
    bitstream += b'\x00'

# Open a new wave file in write mode
with wave.open('output.wav', 'wb') as file:
    file.setnchannels(1)  # mono sound
    file.setsampwidth(bits_per_sample // 8)  # 16-bit audio
    file.setframerate(sample_rate)  # set the sample rate

    # Convert the binary bitstream to an array of audio samples
    data = np.array(struct.unpack('h'*int(len(bitstream)/2), bitstream))

    # Write the audio data to the file
    file.writeframes(data.tobytes())

# Play the audio file using the OS's default audio player
os.system('afplay output.wav') # for macOS