import essentia
import essentia.standard
import time

def load(filename):
	start = time.time()
	loader = essentia.standard.MonoLoader(filename=filename, sampleRate=44100)
	audio = loader()
	end = time.time()

	return (end-start)