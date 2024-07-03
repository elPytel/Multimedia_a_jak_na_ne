from os import path 
# Math
import math
import numpy as np
# Signal processing
import scipy as scipy
import scipy.signal as signal
import matplotlib.pyplot as plt
# Image
from PIL import Image
# Audio
import soundfile as sf
import playsound as ps
import simpleaudio as sa
from pydub import AudioSegment   
# Colors
from colors import *

VERBOSE = True
AUDIO_FORMATS = ['mp3', 'wav', 'flac', 'ogg']

def play_audio(signal, sample_rate):
    # Převod signálu na formát vhodný pro přehrání
    if VERBOSE:
        print("Converting signal to 16-bit format...")
    signal = np.int16(signal * 32767)  # Převod na 16-bitový formát
    wave_obj = sa.WaveObject(signal, 1, 2, sample_rate)  # Vytvoření objektu WaveObject

    # Přehrání signálu
    if VERBOSE:
        print("Playing signal...")
    play_obj = wave_obj.play()
    play_obj.wait_done()
    if VERBOSE:
        print(f"{Green}Signal was played.{Reset}")
        
def convert_audio_file(input_file, output_file):
    # get input file format
    input_format = input_file.split('.')[-1]
    
    # get output file format
    output_format = output_file.split('.')[-1]
    
    # check if the input file exists
    if not path.exists(input_file):
        raise FileNotFoundError(f"File {input_file} not found")
    
    # check if the input file is an audio file
    if input_format not in AUDIO_FORMATS:
        raise ValueError(f"File {input_file} is not an audio file")
    
    # check if the output file is an audio file
    if output_format not in AUDIO_FORMATS:
        raise ValueError(f"File {output_file} is not an audio file")
    
    sound = AudioSegment.from_file(input_file, format=input_format)
    sound.export(output_file, format=output_format)
    