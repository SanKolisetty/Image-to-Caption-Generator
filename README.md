# Image Caption Generator

Image Caption Generator is a machine learning model that can generate meaningful textual descriptions for a given image.

# Table of Contents

- [Image Caption Generator](#ai-image-classifier)
- [Table of Contents](#table-of-contents)
- [Brief Overview](#brief-overview)
- [Demo](#demo)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Model](#model)
- [Testing and Evaluation](#testing-and-evaluation)

# Brief Overview
[(Back to top)](#table-of-contents)

This project involved building a model that can generate meaningful textual descriptions for given input images. To start, we gathered a dataset of images and their associated captions. Once we have completed the data collection process, we proceeded to build a model using Convolutional Nueral Networks (CNN) and Recurrent Nueral Networks (RNN) in combination. CNNs were used to extract meaningful features from the input images, while RNNs, specifically Long Short-Term Memory (LSTM) networks, were employed to generate captions based on the extracted features.

# Demo
[(Back to top)](#table-of-contents)

Here is a short demo of the model deployed in streamlit and running on local host.

https://github.com/SanKolisetty/Image-to-Caption-Generator/assets/95172001/7b59912b-d88e-4ef1-b28a-b63c911b9ef1

# Installation
[(Back to top)](#table-of-contents)

Open Git Bash and change the directory to the location where the repository is to be cloned. Then, type the following commands.

```shell
  git init
```
```shell
  git clone https://github.com/SanKolisetty/Image-to-Caption-Generator.git
```
Now, install the requirements given below.

- Python3 
- TensorFlow 
- NumPy
- Streamlit
- Keras
- Pillow

To access or use the application, open a terminal in the cloned repository folder and run the following command.

```shell
  streamlit run deployment.py
```
Finally, browse the link provided in your browser.

# Data Sources
[(Back to top)](#table-of-contents)

The dataset used was Flickr 8k dataset. It consists of 8,000 images that are each paired with five different captions which provide clear descriptions of the salient entities and events. The images were chosen from six different Flickr groups, and tend not to contain any well-known people or locations, but were manually selected to depict a variety of scenes and situations.

- Flickr 8k Dataset ( [Link](https://www.kaggle.com/datasets/adityajn105/flickr8k) )

# Model
[(Back to top)](#table-of-contents)

The CNN model was built similar to `VGG16` and was trained on the train dataset. The model has a `Convolutional` Layer, `MaxPooling` Layer and a `Dropout` Layer repeated four times with increasing sizes of filters of the Convolutional Layer i.e. 32, 64, 128, and 256. It has 3 dense layers. The activation for all the layers is `relu` except for the last layer, which has activation `sigmoid`. The model architecture and model summary are uploaded.

# Testing and Evaluation
[(Back to top)](#table-of-contents)

On evaluation, model achieved an BLEU Score of 0.53.


