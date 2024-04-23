import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class PredictionPipeline:
    def __init__(self,filename):
        self.filename = filename
    
    def predict(self):
        model = load_model(os.path.join("artifacts","training", "trained_model.h5"))

        test_image = image.load_img(self.filename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        pred = model.predict(test_image)
        print(pred)
        result = round(pred[0][0])
        if result == 1:
            prediction = 'Normal'
        else:
            prediction = 'Adenocarcinoma Cancer'
        return prediction