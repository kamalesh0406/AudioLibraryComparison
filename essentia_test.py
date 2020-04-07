import essentia
import essentia.standard

def load(filename):
	start = time.time()
	loader = essentia.standard.MonoLoader(filename=filename)
	audio = loader()
	end = time.time()

	return (end-start)