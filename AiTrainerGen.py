import tensorflow as tf
import numpy as np
from save_load import*
from sklearn.metrics import accuracy_score

AllData=load("InOutData.json")
input_data=AllData[0]
target_data=AllData[1]


input_data_np = np.array(input_data, dtype=np.float32)
target_data_np = np.array(target_data, dtype=np.float32)

input_data_tf = tf.convert_to_tensor(input_data_np)
target_data_tf = tf.convert_to_tensor(target_data_np)

input_shape = (59,) 
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=input_shape),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(59, activation='sigmoid')
])

model.compile(loss='binary_crossentropy',optimizer='rmsprop',metrics=['Accuracy','FalsePositives','FalseNegatives']) # Using mean squared error as the loss function

model.fit(input_data_tf, target_data_tf, epochs=1, batch_size=64)  # Adjust epochs and batch_size as needed

#loss = model.evaluate(input_data_tf, target_data_tf)
#print("Loss:", loss)

model.save('tfmodel01.keras')