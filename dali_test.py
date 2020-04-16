from nvidia.dali.pipeline import Pipeline
import nvidia.dali.ops as ops
import nvidia.dali.types as types
import nvidia.dali as dali
import librosa
import time
import numpy as np

class Spectrogram(Pipeline):
	def __init__(self, device, file_name, batch_size, nfft, window_length, window_step, num_threads=1, device_id=0):
		super(Spectrogram, self).__init__(batch_size, num_threads, device_id)
		self.device = device
		self.batch_data = []

		y, sr = librosa.load(file_name, sr=44100)
		for _ in range(batch_size):
			self.batch_data.append(np.array(y, dtype=np.float32))
		self.external_source = ops.ExternalSource()
		self.spectrogram = ops.Spectrogram(device=self.device, nfft=nfft, 
							window_length = window_length, window_step = window_step)

	def define_graph(self):
		self.data = self.external_source()
		out = self.data.gpu() if self.device=="gpu" else self.data 
		out = self.spectrogram(out)
		return out
	
	def iter_setup(self):
		self.feed_input(self.data, self.batch_data)

def stft(filename, n_fft, window_length, hop_length):
	pipe = Spectrogram(device="gpu", file_name=filename, batch_size=1, nfft=n_fft, window_length=window_length, window_step=hop_length)
	pipe.build()
	start = time.time()
	outputs = pipe.run()
	spectrogram_dali = outputs[0].at(0)
	end = time.time()

	return(end-start)
