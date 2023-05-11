import csv
import numpy as np
from scipy.io import wavfile

input_file = "output_data_mono.csv"
output_file = "output_wav_file.wav"
sample_rate = 44100  # Change this to the desired sample rate (e.g., 44100 for CD quality)

# Read the CSV file and extract the values
with open(input_file, "r") as file:
    reader = csv.reader(file)
    values = [int(row[0]) for row in reader]

# Convert the values to a numpy array
audio_data = np.array(values, dtype=np.int16)

# Save the audio data to a WAV file
wavfile.write(output_file, sample_rate, audio_data)
