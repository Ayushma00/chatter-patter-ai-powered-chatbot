import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer= WordNetLemmatizer()
import pickle
import numpy as np
import pandas as pd
from keras. models import Sequential
from keras.layers import Dense,Activation, Dropout
from keras.optimizers import Adam
import random
import json

files = ['agriculture','culture','economics','health','politics']

for file in files:
    words = []
    tags= []
    documents= []
    ignore_words=['?','!']
    data_file = open(file+'.json').read()
    purposes = json.loads(data_file)

    for purpose in purposes['purpose']:
        for question in purpose['questions']:
            w = nltk.word_tokenize(question)
            words.extend(w)

            documents.append((w,purpose['id_name']))

            if purpose['id_name'] not in tags:
                tags.append(purpose['id_name'])

    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    tags = sorted(list(set(tags)))
    pickle.dump(words,open(file+'_words.pkl','wb'))
    pickle.dump(tags,open(file+'_tags.pkl','wb'))

    training=[]
    output = [0]*len(tags)
    for doc in documents:
        bags=[]
        question = doc[0]
        question = [lemmatizer.lemmatize(w.lower()) for w in question]

        for w in words:
            bags.append(1) if w in question else bags.append(0)

            out = list(output)
            out[tags.index(doc[1])]=1
            training.append([bags,out])

    random.shuffle(training)
    training = np.array(training)
    X_train = list(training[:,0])
    y_train = list(training[:,1])

    model=Sequential()
    model.add(Dense(128,activation="relu",input_shape=(len(X_train[0]),)))
    model.add(Dropout(0.2))
    model.add(Dense(64,activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(len(y_train[0]),activation="softmax"))
    adam = Adam(learning_rate=0.01)
    model.compile(optimizer=adam,loss="categorical_crossentropy",metrics=["accuracy"])

    hist = model.fit(np.array(X_train),np.array(y_train),epochs=40,batch_size=5,verbose=1)

    model.save(file+'_model.h5',hist)
