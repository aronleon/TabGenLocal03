import tensorflow as tf
#from tensorflow.keras.models import Sequential, load_model
import numpy as np
from save_load import*
import matplotlib.pyplot as plt
from SongAnalyzer import*

AllData=load("InOutData.json")
input_data=AllData[0]
target_data=AllData[1]


input_data_np = np.array(input_data, dtype=np.float32)
target_data_np = np.array(target_data, dtype=np.float32)

input_data_tf = tf.convert_to_tensor(input_data_np)
target_data_tf = tf.convert_to_tensor(target_data_np)

#input_shape = (59,) 
model = tf.keras.models.load_model("tfmodel01.keras")
inin=GetToneData("GuitarSamp.mp3",7,0)
input_array=inin[207]
input_array=input_array[:59]
input_array=np.array(input_array)
input_array = input_array.reshape(1, -1)
y_hat = model.predict(input_array)
print(y_hat)