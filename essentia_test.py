import essentia
import essentia.standard
import time

def load(filename):
	start = time.time()
	loader = essentia.standard.MonoLoader(filename=filename, sampleRate=44100)
	audio = loader()
	end = time.time()

	return (end-start)

def stft(filename, n_fft, window_length, hop_length):
	start = time.time()

	loader = essentia.standard.MonoLoader(filename=filename, sampleRate=44100)
	audio = loader()

	w = essentia.standard.Windowing(type='hann')
	spectrum = essentia.standard.Spectrum(size=n_fft)

	spectrogram = essentia.Pool()

	for frame in essentia.standard.FrameGenerator(audio, frameSize=window_length, hopSize=hop_length, startFromZero=True):
		spec = spectrum(w(frame))
		spectrogram.add("spectrogram", spec)
	end = time.time()

	return (end-start)