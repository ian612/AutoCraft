from scipy.io import wavfile
import scipy.signal as sps
import numpy as np
import os

def downsample(fname):
    sampling_rate, data = wavfile.read(fname)
    samples = round(len(data) * float(newrate) / sampling_rate)
    new_data = sps.resample(data, samples).astype(np.int16)
    return new_data

# Define sample rates
sample_rate = 48000
newrate = 16000

# Define folder for loading audio files
folder = 'files_'+str(int(sample_rate/1000))+'kHz/'
smolFolder = 'files_'+str(int(newrate/1000))+'kHz/'
ext = '.wav'

if not os.path.exists(smolFolder):
    os.makedirs(smolFolder)

for filename in os.listdir(folder):
    if filename.endswith(ext):
        og_fname = os.path.join(folder, filename)
        smolAudio = downsample(og_fname)
        #breakpoint()
        wavfile.write(os.path.join(smolFolder, filename), newrate, smolAudio)

print('Downsampling is complete, files stored in', smolFolder)