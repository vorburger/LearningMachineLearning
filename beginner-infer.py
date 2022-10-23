#!/usr/bin/env python3

from tensorflow import keras

probability_model = keras.models.load_model('beginner.model/')

mnist = keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

input = x_test[:1]
probabilities = probability_model(input).numpy()
print(probabilities)

test = y_test[:1]
print(test)
