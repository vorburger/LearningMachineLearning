# %%
"""
This is https://www.tensorflow.org/tutorials/quickstart/beginner, initially forked from https://github.com/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb, and then extended - to self learn.
"""

# %%
"""
## Import TensorFlow
"""

# %%
import tensorflow as tf
print("TensorFlow version:", tf.__version__)

import pandas as pd

# %%
"""
## Load a dataset

Load and prepare the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). Convert the sample data from integers to floating-point numbers:
"""

# %%
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

print("Shapes: x_train", x_train.shape, "; y_train", y_train.shape, "; x_test", x_test.shape, "; ", y_test.shape, "\n")
print("Description of y_train:", pd.DataFrame(y_train).describe(), "\n")
print("y_train[:1] = ", y_train[:1])

# %%
"""
## Build a machine learning model

Build a `tf.keras.Sequential` model by stacking layers.
"""

# %%
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# %%
"""
For each example, the model returns a vector of [logits](https://developers.google.com/machine-learning/glossary#logits) or [log-odds](https://developers.google.com/machine-learning/glossary#log-odds) scores, one for each class.
"""

# %%
predictions = model(x_train[:1]).numpy()
print(predictions)

# %%
"""
The `tf.nn.softmax` function converts these logits to *probabilities* for each class: 
"""

# %%
tf.nn.softmax(predictions).numpy()

# %%
"""
Define a loss function for training using `losses.SparseCategoricalCrossentropy`, which takes a vector of logits and a `True` index and returns a scalar loss for each example.
"""

# %%
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# %%
"""
This loss is equal to the negative log probability of the true class: The loss is zero if the model is sure of the correct class.

This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to `-tf.math.log(1/10) ~= 2.3`.
"""

# %%
loss_fn(y_train[:1], predictions).numpy()

# %%
"""
Before you start training, configure and compile the model using Keras `Model.compile`. Set the [`optimizer`](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers) class to `adam`, set the `loss` to the `loss_fn` function you defined earlier, and specify a metric to be evaluated for the model by setting the `metrics` parameter to `accuracy`.
"""

# %%
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# %%
"""
## Train and evaluate your model

Use the `Model.fit` method to adjust your model parameters and minimize the loss: 
"""

# %%
model.fit(x_train, y_train, epochs=5)

# %%
"""
The `Model.evaluate` method checks the models performance, usually on a "[Validation-set](https://developers.google.com/machine-learning/glossary#validation-set)" or "[Test-set](https://developers.google.com/machine-learning/glossary#test-set)".
"""

# %%
model.evaluate(x_test,  y_test, verbose=2)

# %%
"""
The image classifier is now trained to ~98% accuracy on this dataset. To learn more, read the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).
"""

# %%
"""
If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:
"""

# %%
probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])

# %%
# TODO range = :1 # :3
input = x_test[:1] # TODO range
probabilities = probability_model(input).numpy()
print(probabilities)

# %%
test = y_test[:1] # TODO range
print(test)