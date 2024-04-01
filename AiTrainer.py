import tensorflow as tf
#from tensorflow.keras.models import Sequential, load_model
import numpy as np
from save_load import*
AllData=load("InOutData.json")
input_data=AllData[0]
target_data=AllData[1]
print(len(input_data))
print(len(target_data))
print(len(AllData))


input_data_np = np.array(input_data, dtype=np.float32)
target_data_np = np.array(target_data, dtype=np.float32)

input_data_tf = tf.convert_to_tensor(input_data_np)
target_data_tf = tf.convert_to_tensor(target_data_np)

for i in range(200):
    input_shape = (59,)
    model = tf.keras.models.load_model("tfmodel01.keras")

    initial_learning_rate = 0.01
    decay = 1e-6
    momentum = 0.9
    sgd_optimizer = tf.optimizers.SGD(learning_rate=initial_learning_rate, decay=decay, momentum=momentum, nesterov=True)

    model.compile(loss='binary_crossentropy',optimizer=sgd_optimizer,metrics=['Accuracy','FalsePositives','FalseNegatives'])  # Using mean squared error as the loss function (mse)categorical_crossentropy
    #128
    model.fit(input_data_tf, target_data_tf, epochs=20, batch_size=128)  # Adjust epochs and batch_size as needed

    #loss = model.evaluate(input_data_tf, target_data_tf)
    #print("Loss:", loss)

    model.save('tfmodel01.keras')