import librosa
import time

def load(filename):
	start = time.time()
	y, sr = librosa.load(filename)
	end = time.time()

	return (end-start)