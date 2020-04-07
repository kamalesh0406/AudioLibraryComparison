# AudioLibraryComparison

This repository contains code which you can use to compare the speeds of various audio processing libraries in Python. 

To run the tests use the following command:
```python
python main.py filename --test ['load', 'stft'] --fft_bins 2048 --window_length 1024 --hop_length 512
```
If you want to add more libraries to this list create a pull request with the tests written in a file of this format {libraryname}\_test.py
