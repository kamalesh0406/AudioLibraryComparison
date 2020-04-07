import torchaudio
import time

def load(filename):

	start = time.time()
	y, sr = torchaudio.load(filename)
	end = time.time()

	return (end-start)

def stft(filename, n_fft, window_length, hop_length):

	start = time.time()
	y, sr = torchaudio.load(filename)
	spectrum = torchaudio.transforms.Spectrogram(n_fft=n_fft, win_length=window_length, hop_length=hop_length)(y)
	end = time.time()	

	return (end-start)
