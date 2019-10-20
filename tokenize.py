from keras.models import model_from_json
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing.text import Tokenizer
from keras.layers import Dense, Flatten, LSTM, Conv1D, MaxPooling1D, Dropout, Activation
import clean_text

def tokenize(text):
    # text = text.map(lambda x: clean_text(text))
    vocabulary_size = 20000
    tokenizer = Tokenizer(num_words= vocabulary_size)
    tokenizer.fit_on_texts(text)
    sequences = tokenizer.texts_to_sequences(text)
    data = pad_sequences(sequences, maxlen=50)
    return data