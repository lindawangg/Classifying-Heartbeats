from scipy.signal import find_peaks_cwt
import numpy as np

def find_peaks(samples):
	"""Gets a list of peaks for each sample"""
	all_peaks = []
	for sample in samples:
		indexes = find_peaks_cwt(sample, np.arange(1, 5))
		peaks = []
		for i in indexes:
			if sample[i] > 0.15:
				peaks.append(i)

		if len(peaks) > 1:
			i = 1
			start = 0
			tmp_array = []
			max_peak = sample[peaks[start]]
			max_ind = start
			while i < len(peaks):
				if peaks[i] <= (peaks[start] + 200):
					if sample[peaks[i]] > max_peak:
						max_peak = sample[peaks[i]]
						max_ind = i
					if i == len(peaks)-1:
						tmp_array.append(peaks[max_ind])
						break
					i += 1
				else:
					tmp_array.append(peaks[max_ind])
					start = i 
					max_ind = start
					max_peak = sample[peaks[start]]
					i += 1
			peaks = tmp_array
		all_peaks.append(peaks)
	return np.array(all_peaks)