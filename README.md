# Haitian Creole Transformer

This project implements a Transformer-based model for processing Haitian Creole language data. It utilizes a dataset of spoken and text data sourced from Carnegie Mellon University (CMU SCS). The project includes scripts for data preprocessing, model training, and evaluation. The trained model and dataset files are organized as follows:

- **Dataset Notebook:** `transformer-model-dataset.ipynb`  
  A Jupyter notebook that contains the code for combining the CMU data and splitting it into train/test set to upload to HuggingFace. I used the 
  huggingface cli to upload the dataset to the Hugging Face Hub. You can find the train dataset at [thisisfrantz/haitian-creole-english-train](https://huggingface.co/datasets/thisisfrantz/haitian-creole-english-train) and test dataset at [thisisfrantz/haitian-creole-english-test](https://huggingface.co/datasets/thisisfrantz/haitian-creole-english-test).
  

- **Model file:** `transformer_mode.ipynb`  
    A Jupyter notebook that contains the code for training a Transformer model on the Haitian Creole dataset. It includes data loading, model architecture definition, training loop, and evaluation metrics. 

## The Haitian Creole spoken and text data comes from CMU SCS.
Dataset details:
- Source: [Haitian Creole language data by Carnegie Mellon](http://www.speech.cs.cmu.edu/haitian/)
- License or Terms: [License](http://www.speech.cs.cmu.edu/haitian/COPYING)
- Citation (if provided): [Include any formal citation or reference they ask for]

## Model Training
I wanted to create a custom Tokenizer and Model for this project, but I didn't enough
data to create one. I decided to use a pretrained tokenizer,  `Helsinki-NLP/opus-mt-ht-en` from Hugging Face to make things easier. I used the `DataLoader` class to iterate through the dataset and prepare batches for training. The model is trained using the AdamW optimizer and a learning rate scheduler. The model used is the `Helsinki-NLP/opus-mt-ht-en` model, which is a pre-trained translation model for Haitian Creole to English.

## Evaluation
I do not have access to a GPU, so I trained the model on my CPU. The training process took a long time. Despite this, I was able to achieve ok accuracy on the test set. After the initial training, the model achieved a validation loss of 0.8021 and perplexity of 2.23. I also utilized the `evaluate` library to compute the BLEU (Bilingual Evaluation Understudy) score for the model's predictions on the test set. The BLEU score was 0.1749, which indicates that the model is able to translate Haitian Creole to English with some accuracy.

## Analysis
The model was ok at translating Haitian Creole to English, but it struggled with some of the simple sentences. For example, for the sentence "koman ou ye?" (How are you?), the model translated it to "What are you?", which is not corrent. For a simple sentence like this, the model should be able to tanslate.

## Future Work
- Since I do not have access to a GPU, I was not able to train the model for a long time. I would like to train the model on a GPU to see if I can achieve better results.

## Update