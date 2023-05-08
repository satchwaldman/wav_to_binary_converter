import numpy as np
import struct
import os
import wave

with open('play_after_saving/bitstreams/input_bitstream.txt', 'rb') as file:
    bitstream = file.read()

# Specify the audio parameters
sample_rate = 44100  # samples per second
duration = 5.0  # seconds
bits_per_sample = 24  # number of bits per sample

print(type(bitstream))

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