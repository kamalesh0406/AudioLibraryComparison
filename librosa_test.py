import librosa
import time

def load(filename):
	start = time.time()
	y, sr = librosa.load(filename, sr=44100)
	end = time.time()

	return (end-start)

def stft(filename, n_fft, window_length, hop_length):
	start = time.time()
	y, sr = librosa.load(filename, sr=44100)
	spec = librosa.core.stft(y, n_fft=n_fft, hop_length=hop_length, win_length=window_length)
	end = time.time()	

	return (end-start)