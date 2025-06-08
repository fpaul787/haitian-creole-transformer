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
