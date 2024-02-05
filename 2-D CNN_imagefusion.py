"""
code used to construst 2-D CNN model 
"""
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPooling3D, Dropout, BatchNormalization,ZeroPadding2D

np.set_printoptions(suppress=True)

# inputting the IMS and H&E image (with 3 featues)
IMS=pd.read_csv(r"X:\Liang\matlab\11-17-2022 cory 75\cory_IMS_deep.csv")
HE=pd.read_csv(r"X:/Liang/matlab/11-17-2022 cory 75/cory_HE_deep.csv")

#reshaping the IMS and HE dataset into the format that can be inputted into the CNN
y=IMS.values
y_1 = y.reshape(1,851,601,1)
x = np.half(HE.values)
x_1= x.reshape(1,851,601,3)

# building the CNN
model = Sequential()
model.add(BatchNormalization())
model.add(ZeroPadding2D(padding=(1,1)))
model.add(Conv2D(64, kernel_size=(3,3), kernel_initializer='normal', activation='ReLU'))
model.add(BatchNormalization())
model.add(ZeroPadding2D(padding=(1,1)))
model.add(Conv2D(32, kernel_size=(3,3), kernel_initializer='normal', activation='ReLU'))
model.add(Conv2D(1, kernel_size=(1,1)))

# Compiling the model
model.compile(loss='mean_squared_error', optimizer='adam')

# Fitting the CNN 
#Batch_size should always be set to one beucase we are only training the model with one image 
model.fit(x_1, y_1 ,batch_size =1, epochs=20000, verbose=1)

# generating the calculated IMS image 
y_new = model.predict(x_1)
y_new_1 = y_new.reshape(851,601)

# output the predicted ion image 
np.savetxt('X:/Liang/matlab/11-17-2022 cory 75/cory_IMS_64_20000_calculated',y_new_1,fmt='%.4e',delimiter=',')
