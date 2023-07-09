# Image Caption Generator

Image Caption Generator is a machine learning model that can generate meaningful textual descriptions for a given image.

# Table of Contents

- [Image Caption Generator](#image-caption-generator)
- [Table of Contents](#table-of-contents)
- [Brief Overview](#brief-overview)
- [Demo](#demo)
- [Installation](#installation)
- [Data Sources](#data-sources)
- [Data Preprocessing](#data-preprocessing)
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
Now, install the requirements using the following command.

```shell
   pip install -r requirements.txt 
```
To access or use the application, open a terminal in the cloned repository folder and run the following command.

```shell
  streamlit run deployment.py
```
Finally, browse the link provided in your browser.

# Data Sources
[(Back to top)](#table-of-contents)

The dataset used was Flickr 8k dataset. It consists of 8,000 images that are each paired with five different captions which provide clear descriptions of the salient entities and events. The images were chosen from six different Flickr groups, and tend not to contain any well-known people or locations, but were manually selected to depict a variety of scenes and situations.

- Flickr 8k Dataset ( [Link](https://www.kaggle.com/datasets/adityajn105/flickr8k) )

# Data Preprocessing
[(Back to top)](#table-of-contents)

Since we have both image and textual data, they need to be preprocessed separately and still need to be mapped to each other. For this mapping to be possible, we use the file name as the key.

- ## Image Data Preprocessing

  For preprocessing images and extracting their features, we used `VGG16` model. The output layer of this model was removed and the image features were extracted.

- ## Text Data Preprocessing

  First, the text data was cleaned by removing special characters, digits, additional spaces etc. and converting everything into lowercase alphabets. For every     caption, `start` and `end` tags were added. Then, the captions were tokenized using `Tokenizer`. This gives an index to every word. Using the `Tokenizer`, the 
`vocabulary_size` was found which was used as the ouput layer size of the model. The `max_length` of a caption was used to pad sequences.

# Model
[(Back to top)](#table-of-contents)

The model has two inputs - image features and captions data sequences. Model was trained using LSTMs and the ouput was the probability of each word in the vocabulary. The output layer had activation `softmax`. 

Thus, for generating captions for any image, the word was found for the index with the maximum probability and it was added to the caption. If the predicted word was `end`, the caption ended.

> Model architecture and model summary are uploaded.

# Testing and Evaluation
[(Back to top)](#table-of-contents)

10% of the samples in the dataset were used for testing. Captions were generated using the trained model and then the `BLEU score` was calculated using these generated captions and the actual captions. On evalutation, the model achieved a `BLEU score` of 0.53.

![bleuscore](https://github.com/SanKolisetty/Image-to-Caption-Generator/assets/95172001/2f47fc74-a506-4d32-8000-9e46e7362746)
