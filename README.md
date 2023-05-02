# wav_to_binary_converter

Repository for converting .wav files to binary (and giving the option to play back the binary files -- NOT in real time)

TO USE:
1. Download a .wav file you would like to use, and upload it to the sound_files folder.
2. On line 8 of wav_to_binary.py, change the file path to the appropriate  file path.
3. There are five sections in wav_to_binary.py that can be commented or uncommented, depending on whether you would like to take advantage of their functionality
A. Uncomment EITHER line 17 or 18, depending on whether you want to use a curtailed version of the audio snippet or the full version.
B. Line 24 can be uncommented to see the binary bitstream printed to the terminal. 
C. Lines 28-29 can be uncommented to see the time series data comprising the audio file. 
D. Lines 33-34 can be uncommented to save the bitstream as a .txt file.
E. Lines 38-60 can be uncommented to hear the sound play back from the saved binary bit stream. Note that this will not play back in real time.