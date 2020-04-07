import librosa
import essentia
import torchaudio
import argparse

import librosa_test
import torchaudio_test
import essentia_test

parser = argparse.ArgumentParser()
parser.add_argument("filename", type=str)

def main():
	args = parser.parse_args()

	librosa_load_time = librosa_test.load(args.filename)
	essentia_load_time = essentia_test.load(args.filename)
	torchaudio_load_time = torchaudio_test.load(args.filename)

	print("Librosa Load Time", librosa_load_time)
	print("Essentia Load Time", essentia_load_time)
	print("TorchAudio Load Time", torchaudio_load_time)

if __name__=="__main__":
	main()