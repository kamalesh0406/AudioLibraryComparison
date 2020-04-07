import torchaudio
import time

def load(filename):
	start = time.time()
	y, sr = torchaudio.load(filename)
	end = time.time()

	return (end-start)