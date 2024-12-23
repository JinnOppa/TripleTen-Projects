
import pandas as pd

import tensorflow as tf

from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.resnet import ResNet50
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout, Flatten
from tensorflow.keras.optimizers import Adam


def load_train(path):
    
    """
    This code is to load a part of training set from file path
    """
    
    label = pd.read_csv(path + 'labels.csv')
    train_datagen = ImageDataGenerator(validation_split=0.25,
                                rescale=1/255,
                                horizontal_flip=True,
                                vertical_flip=True)
    train_gen_flow = train_datagen.flow_from_dataframe(dataframe=label,
                                                directory=path + 'final_files/',
                                                x_col='file_name',
                                                y_col='real_age',
                                                target_size=(224, 224),
                                                batch_size=32,
                                                class_mode='raw',
                                                subset='training',
                                                seed=12345)

    return train_gen_flow


def load_test(path):
    
    """
    This code is to load a part of validation set/test from file path
    """
    
    # letakkan kode Anda di sini
    label = pd.read_csv(path + 'labels.csv')
    test_datagen = ImageDataGenerator(validation_split=0.25,
                                rescale=1/255)
    test_gen_flow = test_datagen.flow_from_dataframe(dataframe=label,
                                               directory=path + 'final_files/',
                                               x_col='file_name',
                                               y_col='real_age',
                                               target_size=(224, 224),
                                               batch_size=32,
                                               class_mode='raw',
                                               subset='validation',
                                               seed=12345)

    return test_gen_flow


def create_model(input_shape):
    
    """
    This code is to define a model
    """
    
    # letakkan kode Anda di sini
    model=Sequential()
    optimizer=Adam(lr=0.0001)
    backbone = ResNet50(include_top=False,
                        input_shape=input_shape,
                        weights='imagenet')
    model.add(backbone)
    model.add(GlobalAveragePooling2D())
    model.add(Flatten())
    model.add(Dense(1, activation='relu'))
    model.compile(loss='mean_squared_error',
                  optimizer=optimizer,
                  metrics=['mae'])

    return model


def train_model(model, train_data, test_data, batch_size=None, epochs=10,
                steps_per_epoch=None, validation_steps=None):

    """
    Train the model with the given paramter
    """
    
    # letakkan kode Anda di sini
    if steps_per_epoch is None:
        steps_per_epoch == len(train_data)
    if validation_steps is None:
        validation_steps == len(test_data)
    model.fit(train_data,
             validation_data=test_data,
             batch_size=batch_size,
             epochs=epochs,
             steps_per_epoch=steps_per_epoch,
             validation_steps=validation_steps,
             verbose=2,
             shuffle=True)

    return model


