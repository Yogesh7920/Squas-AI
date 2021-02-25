import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
import os


class Recommendation:

    def __init__(self, input_dim, user):

        self.input_dim = input_dim
        self.user = user
        self.model_path = os.path.join('users', user + '.h5')
        if os.path.exists(self.model_path):
            self.model = self.load()
        else:
            self.model = self.create()

        self.cp = keras.callbacks.ModelCheckpoint(self.model_path, save_best_only=True)

    def create(self):
        model = keras.Sequential()

        model.add(layers.Dense(32, activation='relu', input_dim=self.input_dim))
        model.add(layers.Dense(32, activation='relu'))
        model.add(layers.Dense(16, activation='relu'))
        model.add(layers.Dense(1, activation='sigmoid'))

        model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

        return model

    def train(self, items, likes, epochs=20):
        es = keras.callbacks.EarlyStopping(patience=epochs//10 + 1, restore_best_weights=True)
        self.model.fit(items, likes, epochs=epochs, callbacks=[self.cp, es], validation_split=0.1)

    def predict(self, items):
        return self.model.predict(items)

    def get_best(self, items):
        return np.argmax(self.predict(items))

    def evaluate(self, items, likes):
        return self.model.evaluate(items, likes)

    def save(self):
        self.model.save(self.model_path)

    def load(self):
        return keras.models.load_model(self.model_path)
