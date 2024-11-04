import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model


st.title('Welcome to DermDetect')
st.header('Skin Lesion Classification using VGG-16')
st.subheader(":blue[Making skin cancer detection fast, efficient, accessible and cost-free.]")

try:
    model = load_model('skin_lesion_classifier.h5')
    #st.write(" ")
    #st.success("Model loaded successfully.")
except Exception as e:
    st.write(f"Error loading model: {e}")


def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  
    return img_array


def classify_skin_lesion(img):
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)[0][0]

    if prediction > 0.5:
        label = 'malignant'
        confidence = prediction * 100
    else:
        label = 'benign'
        confidence = (1 - prediction) * 100

    return label, confidence


tab1, tab2 = st.tabs(["Try out DermDetect", "DermDetect Model Training and Datasets"])

with tab1:
    with st.container():
        st.write(" ")
        uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])

        if uploaded_file is not None:

            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image', width=200)

    
            label, confidence = classify_skin_lesion(img)

            st.header(f'The lesion in the image is **{label}** with **{confidence:.2f}%** confidence.')

with tab2:
    st.subheader("VGG-16: A deep learning convolutional neural network algorithm used for object detection and classification.")
    st.write(" ")
    st.subheader("Dataset: consists for 3000+ images of benign and malignant lesions from ISIC(Internation Skin Imaging Collaboration)")
    st.write(" ")
    st.subheader("Model Validation and Training Loss")
    st.image("grash.jpg")

