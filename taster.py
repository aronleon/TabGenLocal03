from SongAnalyzer import*
import matplotlib.pyplot as plt
ToneData=GetToneData("Track02/Instrument5.wav",2,0)
Viz=ToneData[1]
plt.plot(Viz)
plt.show()
