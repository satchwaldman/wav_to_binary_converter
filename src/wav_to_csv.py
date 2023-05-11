from scipy.io.wavfile import read, write
import io
# import warnings
import numpy as np
import matplotlib.pyplot as plt
import math
import csv

with open("src/input_wav_files/woodwinds.wav", "rb") as wavfile:
    input_wav = wavfile.read()

# here, input_wav is a bytes object representing the wav object
rate, data = read(io.BytesIO(input_wav))

with open('src/output_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow([row])

# print(np.shape(data))

### VISUALIZATION

# print(data[0])
# print(rate)
# print(math.log2(np.max(data)))
# plt.plot(data)
# plt.show()

# # rate = 44100
# write('test.wav', rate, data)

### --------------

# resolution = int(np.ceil(math.log2(np.max([np.max(data), np.abs(np.min(data))])) + 1))
# print(resolution)

# binary_list = []

# print(data[0:5])

# for decimal in data:
#     binary = bin(decimal)[2:]  # Convert decimal to binary, slicing off the first two characters '0b'
#     binary = binary.zfill(resolution)  # Pad the binary string with 0s at the front until it reaches the desired resolution
#     binary_list.append(binary)

# binary_string = ''.join(binary_list)

# with open('output_bitstream.txt', 'w') as file:
#     file.write(binary_string)
