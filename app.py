import streamlit as st
from PIL import Image
from chest_cancer_classifier.pipeline.prediction_pipeline import PredictionPipeline


st.markdown("<h1 style='text-align: center;'>Chest Cancer Prediction</h1>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_name = "uploaded_image.jpg"
    with open(image_name, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.image(image, use_column_width="auto")

    if st.button("Predict"):
        classifier = PredictionPipeline(image_name)
        prediction = classifier.predict()
        st.markdown(f"<h3 style='text-align: center;'>Prediction : {prediction}</h3>", unsafe_allow_html=True)