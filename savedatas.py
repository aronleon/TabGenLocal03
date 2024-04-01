from save_load import*
from SongAnalyzer import*
from MidiToData import*
import os

#Saves datasets to InOutData.json file.

folder_path = "Track02"
file_list = os.listdir(folder_path)
wav_files = [os.path.join("Track02", file) for file in file_list if file.endswith(".wav")]
print(wav_files)




Midi=MidiToDataConversion("Track02/Instrument.mid")
print(len(Midi))

all_tracks=[]
for i in range(len(wav_files)):#len(wav_files)
    Tones=GetToneData(wav_files[i],184.6,0)
    print(wav_files[i], " complete...")
    print("length: ",len(Tones))
    print("")
    all_tracks.append(Tones)

x=[]
y=[]
for a in range(len(all_tracks)):
    for b in range(len(all_tracks[a])):
        frame=all_tracks[a][b]
        frame=frame[:59]
        x.append(frame)
        y.append(Midi[b])
InOutData=[x,y]


folder_path = "Track03"
file_list = os.listdir(folder_path)
wav_files = [os.path.join("Track03", file) for file in file_list if file.endswith(".wav")]
print(wav_files)




Midi=MidiToDataConversion("Track03/Instrument.mid")
Midi=Midi[:12951]
print(len(Midi))

all_tracks=[]
for i in range(len(wav_files)):#len(wav_files)
    Tones=GetToneData(wav_files[i],300.7,0)
    print(wav_files[i], " complete...")
    print("length: ",len(Tones))
    print("")
    all_tracks.append(Tones)


for a in range(len(all_tracks)):
    for b in range(len(all_tracks[a])):
        frame=all_tracks[a][b]
        frame=frame[:59]
        x.append(frame)
        y.append(Midi[b])
InOutData=[x,y]





folder_path = "Track04"
file_list = os.listdir(folder_path)
wav_files = [os.path.join("Track04", file) for file in file_list if file.endswith(".wav")]
print(wav_files)




Midi=MidiToDataConversion("Track04/MT01.mid")
Midi=Midi[:8024]
print(len(Midi))

all_tracks=[]
for i in range(len(wav_files)):#len(wav_files)
    Tones=GetToneData(wav_files[i],186.3,0)
    print(wav_files[i], " complete...")
    print("length: ",len(Tones))
    print("")
    all_tracks.append(Tones)


for a in range(len(all_tracks)):
    for b in range(len(all_tracks[a])):
        frame=all_tracks[a][b]
        frame=frame[:59]
        x.append(frame)
        y.append(Midi[b])
InOutData=[x,y]




save("InOutData.json",InOutData)

