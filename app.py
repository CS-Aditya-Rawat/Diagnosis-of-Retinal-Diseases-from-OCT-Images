import prediction
import streamlit as st
from PIL import Image
import cv2
import numpy as np

st.set_page_config(
    page_title="Diagnosis of Retinal Diseases from OCT Images by Aditya Rawat",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None
)

st.set_option("deprecation.showfileUploaderEncoding", False)

st.title("Diagnosis of Retinal Diseases from OCT Images")

# Uploading the OCT Image
uploaded_image = st.file_uploader("Upload an OCT Image", type=["png", "jpg", "jpeg"])

# Creating a submit button
if st.button("Submit"):
    if uploaded_image is not None:
        file_bytes = np.asarray(bytearray(uploaded_image.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)

        # Getting prediction from the save model
        pred = prediction.OCTPrediction(image)

        # Display the final predicted dataframe
        st.image(image, caption=pred)
        st.write("Prediction: ", pred)