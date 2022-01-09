import streamlit as st
import tensorflow as tf
import numpy as np
import cv2

__all__ = ["demo"]


def img_preprocessing(uploaded_image):
    """ Preprocessing of the fingerprint image

    Args:
        uploaded_image (bmp image): fingerprint image

    Returns:
        fp_array (np.array): numpy array representing the fingerprint
    """

    img_size = 96
    # Decode image to grayscale
    fp_image = np.asarray(bytearray(uploaded_image.read()))
    fp_image = cv2.imdecode(fp_image, cv2.IMREAD_GRAYSCALE)
    # Resize fingerprint array (CNN inputs)
    fp_array = cv2.resize(fp_image, (img_size, img_size))
    fp_array = np.array(fp_array).reshape(-1, img_size, img_size, 1)
    # Normalizing to [0, 1]
    fp_array = fp_array / 255.0
    return fp_array


def demo():
    model = tf.keras.models.load_model("../src/models/contact_fingerprint_cnn.h5")

    st.write("## Demonstration")
    uploaded_image = st.file_uploader("Add fingerprint:",
                                      type=["BMP"],
                                      accept_multiple_files=False)
    st.write("")
    if uploaded_image is not None:
        st.image(uploaded_image)
        fp_array = img_preprocessing(uploaded_image)
        st.write("")
        if st.button("Predict User Id"):
            id_pred = np.argmax(model.predict(fp_array)) + 1
            st.write(f"**Predicted User Id:** `{id_pred}`")
