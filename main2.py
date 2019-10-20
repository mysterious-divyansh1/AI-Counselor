from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation
import pandas as pd 
import numpy as np 
import threading

threading.RLock()

def classify(text):
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    print("Loaded model from disk")
    # evaluate loaded model on test data
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
    # score = loaded_model.evaluate(data, labels, verbose=0)
    # print("%s: %.2f%%" % (loaded_model.metrics_names[1], accuracy(score[1]*100)))
    loaded_model.predict(tokenize(text))

def tokenize(text):
    # text = text.map(lambda x: clean_text(text))
    vocabulary_size = 20000
    tokenizer = Tokenizer(num_words= vocabulary_size)
    tokenizer.fit_on_texts(text)
    sequences = tokenizer.texts_to_sequences(text)
    data = pad_sequences(sequences, maxlen=50)
    return data


res_data = pd.DataFrame(pd.read_csv('final_sentence_classification_data.csv'))
your_problem_child = input("Please enter the exact problem you are facing")
classify(tokenize(res_data['Responses']))









