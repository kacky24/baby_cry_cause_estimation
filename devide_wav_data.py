import os
import soundfile as sf

from utils import devide_cry_by_value


# import wav data
files = []
datapath = 'wav_data/'

for x in os.listdir(datapath):
    if '.wav' in x:
        files.append(x)

# devide wav data and save
for f in files:
    x, sample_rate = sf.read(datapath + f)
    devided_cry_array = devide_cry_by_value(x)
    if devided_cry_array is None:
        continue
    for i in range(len(devided_cry_array)):
        sf.write('devided_wav_data/' + str(i) + '-' + f, devided_cry_array[i], sample_rate)
