import wave
import matplotlib.pyplot as plt
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

# plt.plot(curr_data)
# plt.show()

######################### Save bitstream as a .txt file ########################

with open('bitstreams/input_bitstream.txt', 'w') as file:
    file.write(str(bitstream))