from pathlib import Path
import tensorflow as tf
from keras import Sequential
from keras.applications.vgg16 import VGG16
from keras.layers import Dense,Flatten
from keras.optimizers import Adam
from keras.losses import BinaryCrossentropy
from lung_cancer_classifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    
    def get_base_model(self):
        self.model = VGG16(
            weights = self.config.params_weights,
            input_shape = self.config.params_image_size,
            include_top = self.config.params_include_top
        )
        self.save_model(path = self.config.base_model_path, model = self.model)

    
    @staticmethod
    def __build_custom_model(base_model, classes, freeze_all, freeze_till, learning_rate):
        if freeze_all:
            base_model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in base_model.layers[:-freeze_till]:
                layer.trainable = False

        custom_model = Sequential()
        
        custom_model.add(base_model)
        custom_model.add(Flatten())
        custom_model.add(Dense(256, activation='relu'))
        custom_model.add(Dense(1, activation='sigmoid'))

        custom_model.compile(
            optimizer = Adam(learning_rate = learning_rate),
            loss = BinaryCrossentropy(),
            metrics = ["accuracy"]
        )

        custom_model.summary()
        return custom_model
    

    def create_custom_model(self):
        self.custom_model = self.__build_custom_model(
            base_model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.custom_model)