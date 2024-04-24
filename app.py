import streamlit as st
from PIL import Image
from lung_cancer_classifier.pipeline.prediction_pipeline import PredictionPipeline


st.markdown("<h1 style='text-align: center;'>🫁Lung Cancer Detection🔍</h1>", unsafe_allow_html=True)
st.write("")

uploaded_file = st.file_uploader("Choose an CT Scan image...", type=["jpg", "jpeg", "png"])
st.write("")
st.write("")

if uploaded_file is not None:
    
    image = Image.open(uploaded_file)
    image_name = "uploaded_image.jpg"
    with open(image_name, "wb") as f:
        f.write(uploaded_file.getvalue())
    st.image(image, use_column_width="auto")
    st.write("")
    
    if st.button("Predict", type = "primary"):
        classifier = PredictionPipeline(image_name)
        prediction = classifier.predict()
        st.markdown(f"<h3 style='text-align: center;'>Prediction : {prediction}</h3>", unsafe_allow_html=True)