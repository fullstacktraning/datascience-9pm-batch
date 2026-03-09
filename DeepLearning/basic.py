# deep learning library
# google
# Neural Networks
# Models
# Image Recognization
import tensorflow as tf
# high level api
# used to build the DL model with less lines of code
from tensorflow import keras
# Sequential - used to create Deep Learning Model input layer - h1 - h2 - output later
# create 10 neurons in layesr
# relu - Faster Training, avoid vanishing gradients, deep networks
# Output Layer - 1 neuron
model = keras.Sequential([
    keras.layers.Dense(10,activation='relu'),
    keras.layers.Dense(1)
])
# compile
model.compile(
    optimizer="adam",
    loss="mean_squared_error"
)
print("Deep Learning Model Ready")
# collect the images
# clean the data
# train the model
# test the model
# deploy
