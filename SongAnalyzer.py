import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import sys
import math
import time


def find_closest_number(target, index_list):#function for finding closest number to another
    index_array = np.array(index_list)
    differences = np.abs(index_array - target)
    closest_index = np.argmin(differences)
    closest_number = index_array[closest_index]
    return closest_number


def WesternToneIndex():#finds indecies where tones do exist (outputs list with indecies)
    wf=[]
    for midinum in range(71):
        wf.append((2**((midinum-32)/12))*440)
    spf=11000/2048
    indexList=[]
    for i in range(len(wf)):
        indexList.append(int(((wf[i])/spf)))
    return indexList


def SlideToTone(spectrogram,ToneIndexList):#"slides" tones to correct indecies(western tones) + deletes rest of the indecies
    freqAmount=[]#hey
    for h in range(len(spectrogram)):
        freqAmount.append(0)
    newSpec=[]
    for i in range(len(spectrogram)):
        newSpec.append([])
        for y in range(len(spectrogram[0])):
            newSpec[i].append(0)
    for frequencyIndex in range(380):#len(spectrogram) 380-->2000hz
        closestFreq=find_closest_number(frequencyIndex,ToneIndexList)
        freqAmount[closestFreq]=freqAmount[closestFreq]+1
        for TimeIndex in range(len(spectrogram[0])):
            newSpec[closestFreq][TimeIndex]=newSpec[closestFreq][TimeIndex]+spectrogram[frequencyIndex][TimeIndex]
    newSpec=np.array(newSpec)
    return newSpec


def FlippArray(inputArray):#flips array: Data[notenum][frame]-->Data[frame][notenum]   (works other way around aswell)
    flipped=[]
    for y in range (len(inputArray[0])):
        flipped.append([])
        for x in range(len(inputArray)):
            flipped[y].append(inputArray[x][y])
    flipped=np.array(flipped)
    return flipped


#Gives you a list MusicData[frame][midinum-37] (midinum strarts at 37) 37-108 [108 is just extra data for recognition ok to remove later...]
def GetToneData(audio_path,duration,offset):#43.07 tics/second
    y, sr = librosa.load(audio_path, duration=duration,offset=offset)
    D = np.abs(librosa.stft(y, n_fft=4096, hop_length=512))
    CleanD=SlideToTone(D,WesternToneIndex())
    DW=CleanD[WesternToneIndex()]
    FlippedD=FlippArray(DW)
    return FlippedD #returns array as MusicData[frame][midinum(-37)]
#also the data is not a int or float but some weird data with e's and powers of 10. Might wanna fix that!!