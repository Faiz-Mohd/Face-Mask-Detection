#importing dependencies
import numpy as np
from matplotlib import pyplot as plt
import tensorflow
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from keras.preprocessing.image import ImageDataGenerator

#Creating sequential cnn model for training

model1 = Sequential()
model1.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model1.add(MaxPooling2D())
model1.add(Conv2D(32, (3, 3), activation='relu'))
model1.add(MaxPooling2D())
model1.add(Conv2D(32, (3, 3), activation='relu'))
model1.add(MaxPooling2D())
model1.add(Flatten())
model1.add(Dense(100, activation='relu'))
model1.add(Dense(1, activation='sigmoid'))

#Pre compilation before training model.
model1.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1.0/255,shear_range=0.2,zoom_range=0.2,horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1.0/255)
train='train'
test='test'

train_set = train_datagen.flow_from_directory(
        train,
        target_size=(150, 150),
        batch_size=16,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        test,
        target_size=(150,150),
        batch_size=16,
        class_mode='binary')

model_saved1=model1.fit(
        train_set,
        epochs=10,
        validation_data=test_set
        )

model1.save('FaceMask_model_e10_2500_new.h5', model_saved1)


N = 10
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), model_saved1.history["loss"], label="train_loss")
plt.plot(np.arange(0, N), model_saved1.history["val_loss"], label="val_loss")
plt.plot(np.arange(0, N), model_saved1.history["accuracy"], label="train_acc")
plt.plot(np.arange(0, N), model_saved1.history["val_accuracy"], label="val_acc")
plt.title("Training Loss and Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Loss or Accuracy")
plt.legend(loc="upper right")
