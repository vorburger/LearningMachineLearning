#!/usr/bin/env python3

# This is https://www.tensorflow.org/tutorials/quickstart/beginner, initially forked
# from https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb,
# and then extended - to self learn.

import pandas as pd
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

predictions = model(x_train[:1]).numpy()
print(predictions)

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(y_train[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5)

model.evaluate(x_test,  y_test, verbose=2)

probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

# TODO range = :1 # :3
input = x_test[:1] # TODO range
probabilities = probability_model(input).numpy()
print(probabilities)

# %%
test = y_test[:1] # TODO range
print(test)
