from pathlib import Path
import tensorflow as tf
import keras
from keras.preprocessing.image import ImageDataGenerator
from keras.applications.vgg16 import preprocess_input
from lung_cancer_classifier.entity.config_entity import TrainingConfig


class ModelTraining:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = keras.models.load_model(
            self.config.updated_base_model_path
        )


    def train_valid_generator(self):
        IMAGE_SIZE = self.config.params_image_size[:-1]
        if self.config.params_is_augmentation:
            data_generator_kwargs = dict(                
                preprocessing_function = preprocess_input,
                rotation_range=40,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                horizontal_flip=True,
                fill_mode='nearest'
            )
            generator_kwargs = dict(
                target_size=IMAGE_SIZE,
                batch_size=self.config.params_batch_size,
                class_mode='binary'
            )
            
            train_datagen = ImageDataGenerator(**data_generator_kwargs)
            self.train_generator = train_datagen.flow_from_directory(
                self.config.training_data,
                **generator_kwargs
            )
                    
            test_datagen = ImageDataGenerator(**data_generator_kwargs)
            self.valid_generator = test_datagen.flow_from_directory(
                self.config.validation_data,
                **generator_kwargs
            )
        else:
            generate_kwargs = dict(
                labels='inferred',
                label_mode = 'int',
                batch_size=self.config.params_batch_size,
                image_size=IMAGE_SIZE
            )
            
            self.train_generator = keras.utils.image_dataset_from_directory(
                directory = self.config.training_data,
                **generate_kwargs
            )
            self.train_generator = self.train_generator.map(preprocess_input)

            self.valid_generator = keras.utils.image_dataset_from_directory(
                directory = self.config.validation_data,
                **generate_kwargs
            )
            self.valid_generator = self.valid_generator.map(preprocess_input)

    
    def save_figures(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(14, 7))
        fig, (ax1, ax2) = plt.subplots(1, 2)
        ax1.plot(self.histories.history['accuracy'],color='red',label='train')
        ax1.plot(self.histories.history['val_accuracy'],color='blue',label='validation')
        ax1.legend()
        ax1.set_title('Accuracy')
        ax2.plot(self.histories.history['loss'],color='red',label='train')
        ax2.plot(self.histories.history['val_loss'],color='blue',label='validation')
        ax2.legend()        
        ax2.set_title('Loss')
        plt.suptitle('Metrics') 
        fig.savefig('metrics.jpg')

    
    @staticmethod
    def save_model(path: Path, model: keras.Model):
        model.save(path)

    
    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.histories = self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_data=self.valid_generator,
            validation_steps=self.validation_steps
        )
        
        self.save_figures()

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )