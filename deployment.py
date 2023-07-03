import streamlit as st
import tensorflow as tf
from tensorflow import keras
# import cv2 as cv
import numpy as np
# import matplotlib.pyplot as plt
from PIL import Image, ImageOps
import os
import pickle
# import numpy as np
# from tqdm.notebook import tqdm
# import cv2 as cv
# from matplotlib import pyplot as plt
from tensorflow import keras
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Model
from tensorflow.keras.utils import to_categorical, plot_model
from tensorflow.keras.layers import Input, Dense, LSTM, Embedding, Dropout, add
from tensorflow.keras.models import load_model

max_length = 31
img_size = 48

vgg_model = VGG16()
vgg_model = Model(inputs = vgg_model.inputs, outputs = vgg_model.layers[-2].output)

model = tf.keras.models.load_model("Image_Caption_Generator.h5")

pickle_in = open("tokenizer.pickle", "rb")
tokenizer = pickle.load(pickle_in)

def ind_to_word (index, tokenizer):
    for word, ind in tokenizer.word_index.items():
        if index == ind:
            return word
    return None

def predict_caption(model, image, tokenizer, max_length):
    capt = 'start'
    for i in range(max_length):
        seq = tokenizer.texts_to_sequences([capt])[0]
        seq = pad_sequences([seq], max_length)
        y_hat = model.predict([image, seq], verbose=0)
        y_hat = np.argmax(y_hat)
        word = ind_to_word(y_hat, tokenizer)
        if word is None:
            break
        capt += ' ' + word
        if word == 'end':
            break
    return capt

def gen_caption_image(img, vgg_model, model, tokenizer, max_length):   
    # reshape data for model
    img = img.reshape((1, img.shape[0], img.shape[1], img.shape[2]))
    # preprocess image for vgg
    img = preprocess_input(img)
    # extract features
    feature = vgg_model.predict(img, verbose=0)
    # # get image ID
    y_pred = predict_caption(model, feature, tokenizer, max_length)
    return y_pred

st.title("Image Caption Generator")       
        
img = st.file_uploader("Upload your Image")

if img and st.button("Check"):
    image = Image.open(img)
    st.image(img)
    image = ImageOps.fit(image, (224,224), Image.LANCZOS)
    img_array = img_to_array(image)
    capt = gen_caption_image(img_array, vgg_model, model, tokenizer, max_length)
    st.write(capt)
    
