import tensorflow as tf
import numpy as np
from tensorflow import keras


model = tf.keras.Sequential([
    keras.layers.Dense(10, input_shape=[1], name="input_layer"),
    keras.layers.Dense(1, input_shape=[1], name="output_layer")
])


model.compile(loss=tf.keras.losses.mae,
              optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
              metrics=["mae"])


x = np.arange(-100, 100, 4)
y = x + 10
x_train = x[:40]
y_train = y[:40]

x_test = x[40:]
y_test = y[40:]
print(len(x_train), len(y_train))


# verbose controls how much gets output
model.fit(x_train, y_train, epochs=200, verbose=1)


results = model.predict([24])
print(results)
results = model.predict([17])
print(results)
results = model.predict([103])
print(results)
