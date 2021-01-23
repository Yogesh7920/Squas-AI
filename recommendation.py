import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os


class Recommendation:

    def __init__(self, input_dim):

        self.input_dim = input_dim
        if os.path.exists('recommendation.h5'):
            self.model = self.load()
        else:
            self.model = self.create()

    def create(self):
        model = keras.Sequential()

        model.add(layers.Dense(32, activation='relu', input_dim=self.input_dim))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy')

        return model

    def train(self, items, chosen):
        options = len(items)
        chosen = keras.utils.to_categorical(chosen, options).astype(np.int32)
        self.model.fit(items, chosen, epochs=5, verbose=0)

    def predict(self, items):
        return np.argmax(self.model.predict(items))

    def save(self):
        self.model.save('recommendation.h5')

    def load(self):
        return keras.models.load_model('recommendation.h5')
