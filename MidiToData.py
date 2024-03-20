import mido
import numpy as np
import re


def finddictnote(data_list,note):#finds dictionary with specific "note" value
    for item in data_list:
        if item.get('note') == note:
            return item
    return None 


def importMidi(filename):#imports midi (midimessages)
    mid = mido.MidiFile(filename, clip=True)
    MidiMessage=mid.tracks
    tps=30720 #tics/second
    MidiMessage[1].pop(0)
    MidiMessage[1].pop(0)
    MidiMessage[1].pop(-1)
    return MidiMessage[1]

#{'channel': 0, 'note': 55, 'velocity': 77, 'time': 11}
#{'channel': 0, 'note': 38, 'velocity': 0, 'time': 132}

def TimeCorrectMidi(MessageList):#creates "real-time" midi-data
    TimeCorrected=[]
    CurrentTime=0
    ComplexMessageList=[]
    FullMessage=MessageList
    for i in range(len(FullMessage)):
        input_string = str(FullMessage[i])
        matches = re.findall(r"'([^']*)'|(\w+)=(-?\d+)", input_string)
        components = {key: value or int(number) for value, key, number in matches}
        ComplexMessageList.append(components)
    #print(ComplexMessageList)
    for d in range(len(ComplexMessageList)):
        CurrentTime=CurrentTime+ComplexMessageList[d]['time']
        note=ComplexMessageList[d]['note']
        if ComplexMessageList[d]['velocity']>0:
            onoff=True
        else:
            onoff=False
        TimeCorrected.append({'note':note,'time':CurrentTime,'onoff':onoff})
    return TimeCorrected


#{'note': 77, 'time': 929522, 'onoff': False} (datastructure: TimeCorrected)
#37-95
def CreateMidiMatrix(TimeDict,fraction):#creates frame*58(notes) matrix
    Matrix=[]
    ending=int((int(TimeDict[-1]['time']))*fraction)
    #print(ending)
    for i in range(ending):
        Matrix.append([])
        for g in range(59):
            Matrix[i].append(0)
    return Matrix


def FillMatrix(TimeDict):#fills matrix with the data
    fraction=(43.07/30720) #fraction of midi fps to fourier fps
    CurrentAction=0
    CurrentTime0=0
    NoteLengths=[]
    Matrix = CreateMidiMatrix(TimeDict,fraction)
    while True:
        CurrentAction=TimeDict[0]['note']
        CurrentTime0=int(TimeDict[0]['time'])
        TimeDict.pop(0)
        NextAction=finddictnote(TimeDict,CurrentAction)
        IndexOfAction=TimeDict.index(NextAction)
        TimeDict.pop(IndexOfAction)
        NoteLengths.append({'note':CurrentAction,'length':(int(NextAction['time'])-CurrentTime0),'start':CurrentTime0}) #{'note': 40, 'length': 1920, 'start': 234516} (datastructure)
        if len(TimeDict)<1:
            break
    for a in range(len(NoteLengths)):
        Start=int(NoteLengths[a]['start']*fraction)
        NoteNum=int(NoteLengths[a]['note']-37)
        Length=int(NoteLengths[a]['length']*fraction)
        if Length<1:
            Length=1
        for t in range(Length):
            Matrix[t+Start][NoteNum]=1
    return Matrix #Matrix[frame][midinum]0:37 58:95 37-95


def MidiToDataConversion(filename):#compiled function to get matrix from filename. (framerate pre configured)
    FullData=(FillMatrix(TimeCorrectMidi(importMidi(filename))))#filename="MT01.mid"
    return FullData


def printDataMidi(Filename,length):#testing function DON'T USE!
    FullData=MidiToDataConversion(Filename)
    for u in range(length):
        print(FullData[u])
#printDataMidi("MT01.mid",30)