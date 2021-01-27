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

        self.cp = keras.callbacks.ModelCheckpoint('recommendation.h5', save_best_only=True)

    def create(self):
        model = keras.Sequential()

        model.add(layers.Dense(32, activation='relu', input_dim=self.input_dim))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=[keras.metrics.Accuracy()])

        return model

    def train(self, items, likes, epochs=20):
        es = keras.callbacks.EarlyStopping(patience=epochs//10 + 1, restore_best_weights=True)
        self.model.fit(items, likes, epochs=epochs, callbacks=[es, self.cp], validation_split=0.1)

    def predict(self, items):
        return np.argmax(self.model.predict(items))

    def evaluate(self, items, likes):
        return self.model.evaluate(items, likes)

    def save(self):
        self.model.save('recommendation.h5')

    def load(self):
        return keras.models.load_model('recommendation.h5')
