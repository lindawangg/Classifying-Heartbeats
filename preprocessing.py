import csv
import numpy as np
import wave
import struct
import pywt
 
def moreNsecs(file, N):
	"""Ignores all entries that are less than N seconds"""

    f = wave.open(file)
    frames = f.readframes(-1)
    samples = struct.unpack('h'*f.getnframes(), frames)
    framerate = f.getframerate()
    t = [float(i)/framerate for i in range(len(samples))]
    if t[-1] > 2:
        return True
    else:
        return False

def get_setA_file_label(N):
	"""Returns set a file and label"""
	"""Input: N - minimum file length"""

	x_trainAFile = [] # wave filename 
	y_trainA = [] # label 
	with open('set_a.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row[2]=='' and not row[2]=='label': 
            if moreNsecs(row[1],2):
                x_trainAFile.append(row[1])
                y_trainA.append(row[2])
     return np.array(x_trainAFile), np.array(y_trainA)

def get_setB_file_label(N):
	"""Returns set b file and label"""
	"""Input: N - minimum file length"""

	x_trainBFile = [] # wave filename 
	y_trainB = [] # label 

	with open('set_b.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row[2]=='' and not row[2]=='label': #and 'noisy' not in row[1]:
            fname = 'set_b/' + row[1][16:]
            new_fname = ''
            count = 0
            for c in fname:
                new_fname += c
                if c == '_' and 'noisy' not in row[1]:
                    if count == 1:
                       new_fname += '_' 
                    count += 1
            if moreNsecs(new_fname,2):
                x_trainBFile.append(new_fname)
                y_trainB.append(row[2])
    return np.array(x_trainBFile), np.array(y_trainB)

def get_signal(file):
	"""Returns the signal from the file"""

    f = wave.open(file)
    frames = f.readframes(-1)
    samples = struct.unpack('h'*f.getnframes(), frames)
    return samples

def get_raw_data(x_trainFile):
	"""Gets the raw x training data"""

	raw_data = []
	for i in range(len(x_trainFile)):
    	raw_data.append(np.array(get_signal(x_trainFile[i])))
	return np.array(raw_data)

def down_sample(x, factor=10):
	"""Downsample one sample by a factor of N"""

    r = range(len(x))
    down_array = []
    for i in r[0::factor]:
        down_array.append(x[i])
    return np.array(down_array)

