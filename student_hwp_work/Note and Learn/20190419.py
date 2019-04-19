#%%
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#%%
from keras.datasets import mnist

#%%
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#%%
len(x_train)

#%%
len(x_test)

#%%
X = x_train[87]

#%%
X

#%% [markdown]
# 0~255
#%%
X.shape


#%%
plt.imshow(X, cmap='Greys')

#%%
y_train[87]

#%%
x_train.shape

#%% [markdown]
# 我們要拉平
#%%
x_test.shape


#%%
x_train = x_train.reshape(60000, 28*28)
x_test = x_test.reshape(10000, 28*28)

#%% [markdown]
# one-hot
#%%
from keras.utils import np_utils
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

y_train[87]
#%%
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.optimizers import SGD

#%%
model = Sequential()

#%%
model.add(Dense(4, input_dim=784))
model.add(Activation('sigmoid'))

#%%
model.add(Dense(2))
model.add(Activation('sigmoid'))

#%%
model.add(Dense(10))
model.add(Activation('softmax'))


#%%
model.compile(loss='mse', optimizer=SGD(lr=0.087), metrics=['accuracy'])

#%%
model.summary()

#%%
784*4+4

#%%
4*2+2

#%%
2*10+10

#%%
model.fit(x_train, y_train, batch_size=100, epochs=20)

#%%
from ipywidgets import interact_manual

#%%
predict = model.predict_classes(x_test)
predict

def test(測試編號):
    plt.imshow(x_test[測試編號].reshape(28,28), cmap='Greys')
    print(predict[測試編號])

interact_manual(test,測試編號=(0,9999))

#%%
#讀回來
from keras.models import model_from_json
from keras.optimizers import SGD

model = model_from_json(open('model json path').read())
model.load_weights('weight h5 path')
model.compile(loss='mse', optimizer=SGD(lr=.087))

#%%
#Normolize 資料轉全正、用全距
#fitmodel.history["acc"]

