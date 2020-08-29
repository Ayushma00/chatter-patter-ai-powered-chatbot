
import random
import json
from keras.models import load_model
import numpy as np
import pickle
import nltk
from nltk.stem import WordNetLemmatizer
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

lemmatizer = WordNetLemmatizer()
model = load_model(os.path.join(BASE_DIR,'economics_model.h5'))
purpose = json.loads(open(os.path.join(BASE_DIR,'economics.json')).read())
tags = pickle.load(open(os.path.join(BASE_DIR,'economics_tags.pkl'), 'rb'))
words = pickle.load(open(os.path.join(BASE_DIR,'economics_words.pkl'), 'rb'))


def clean_up_sentencte(sentence):
    word = nltk.word_tokenize(sentence)
    word = [lemmatizer.lemmatize(w.lower()) for w in word]
    return word


def bow(sentence, words):
    sentence_words = clean_up_sentencte(sentence)
    bag = [0] * len(words)

    for s in sentence_words:
        for i, w in enumerate(words):
            if s == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(sentence, model):
    p = bow(sentence, words)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'tag_list': tags[r[0]], 'probability': str(r[1])})
    return return_list


def get_response(pred, json_file):
    tag = pred[0]['tag_list']
    lists = json_file['purpose']

    for i in lists:
        if i['id_name'] == tag:
            result = random.choice(i['answers'])
            break

    return result


def chatbot_response(text):
    ints = predict_class(text, model)
    result = get_response(ints, purpose)
    return result
