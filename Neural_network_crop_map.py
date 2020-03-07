# collecting Training data
import pandas as pd
import numpy as np
A=pd.read_excel('training_set.xlsx')
Train_data=np.array(A.drop(['Lable'],1))
Train_data=np.reshape(Train_data,(219,6,1))
lable_name=np.array(A['Lable'])
# Lables of Trainig dataset
Train_lable=[]
lable={'Chillies':0,'Cotton':1,'Jowar':2,'Paddy':3,'Redgram':4,'Sugarcane':5}
for i in lable_name:
    Train_lable.append(lable[i])
Train_lable=np.array(Train_lable)

# created a neural network model of 6 input neurons and 6 output neurons
from tensorflow import keras
model=  keras.Sequential([
                keras.layers.Flatten(input_shape=(6,1)),
                keras.layers.Dense(100,activation='relu'),
                keras.layers.Dense(6,activation='softmax')
                ])
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# Traing the date in the neuron network
model.fit(Train_data,Train_lable,epochs=5)

# Predecting the lables of new data sets
input_data=pd.read_excel('data.xlsx')
data=np.reshape(np.array(input_data),(2000,6,1))
pred=model.predict(data)
lable=list(lable.keys())
label_data=[]
for i in pred:
    label_data.append(lable[np.argmax(i)])

