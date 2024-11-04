import streamlit as st
from streamlit_lottie import st_lottie 


st.title('About DermDetect')
col1, col2 = st.columns(2)

with col1:
    st.header("What is DermDetect?")

    st.write('**DermDetect** is an app that classifies skin lesions as either benign or malignant based on pictures, giving a confidence rate for each result.')
    st.write('Using a 16-layered Convolutional Neural Network VGG-16, DermDetect utilizes deep learning to make the detection process more  _:blue[accessible, efficient, and cost-free.]_') 

    
    st.write("---") 
    st.header("Why DermDetect?")
    st.write("Conventional skin cancer detection methods, such as biopsies, are often lengthy, painful, and expensive. In India, particularly in rural areas, these methods are frequently inaccessible. This app aims to help individuals and healthcare providers quickly identify potential skin cancers, even in the most remote areas, reducing the workload for dermatologists and improving early detection rates at zero cost. By automating the initial screening, DermDetect contributes to better patient outcomes and simplifies access to medical care.")
    st.write("_Today skin cancer in India is increasing rapidly, as some research says it is directly related to level of arsenic and pesticides in drinking water (other than UV exposure)._")

with col2:
    st.image("data1.jpg")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.image("data2.jpg")
st.subheader(':blue[Melanoma and Squamous Skin Cancer are aggressive forms of cancer, but they are also the most curable when detected early. Skin Lesions are the first symptoms of skin cancer. Early detection can save lives.]')