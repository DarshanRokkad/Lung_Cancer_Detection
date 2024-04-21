from flask import Flask, request, jsonify, render_template
import os
from flask_cors import CORS, cross_origin
from chest_cancer_classifier.utils.common import decodeImage
from chest_cancer_classifier.pipeline.prediction_pipeline import PredictionPipeline


app = Flask(__name__)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)


@app.route("/", methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")


@app.route("/train", methods=["GET", "POST"])
@cross_origin()
def trainRoute():
    os.system("python src\\chest_cancer_classifier\\pipeline\\training_pipeline.py")
    # os.system("dvc repro")
    return "Training done successfully!"


@app.route("/predict", methods=["POST"])
@cross_origin()
def predictRoute():
    image = request.json["image"]
    
    decodeImage(image, client_app.filename)
    result = client_app.classifier.predict()
    
    return jsonify(result)


if __name__ == "__main__":
    client_app = ClientApp()
    app.run(host="0.0.0.0")