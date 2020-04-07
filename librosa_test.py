import librosa
import time

def load(filename):
	start = time.time()
	y, sr = librosa.load(filename, sr=44100)
	end = time.time()

	return (end-start)