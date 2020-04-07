import librosa
import essentia
import torchaudio
import argparse

import librosa_test
import torchaudio_test
import essentia_test

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)
parser.add_argument("--test", default="load", type=str)
parser.add_argument("--fft_bins", default=2048, type=int)
parser.add_argument("--window_length", default=1024, type=int)
parser.add_argument("--hop_length", default=512, type=int)

def main():
	args = parser.parse_args()

	if args.test=="load":
		librosa_time = librosa_test.load(args.filename)
		essentia_time = essentia_test.load(args.filename)
		torchaudio_time = torchaudio_test.load(args.filename)

		print("Librosa Load Time {} s".format(librosa_time))
		print("Essentia Load Time {} s".format(essentia_time))
		print("TorchAudio Load Time {} s".format(torchaudio_time))
	elif args.test=="stft":
		librosa_time = librosa_test.stft(args.filename, args.fft_bins, args.window_length, args.hop_length)
		essentia_time = essentia_test.stft(args.filename, args.fft_bins, args.window_length, args.hop_length)
		torchaudio_time = torchaudio_test.stft(args.filename, args.fft_bins, args.window_length, args.hop_length)

		print("Librosa STFT Time {} s".format(librosa_time))
		print("Essentia STFT Time {} s".format(essentia_time))
		print("TorchAudio STFT Time {} s".format(torchaudio_time))

if __name__=="__main__":
	main()