from keras.models import Sequential
from keras.layers import Dense, Activation, Convolution2D, MaxPooling2D, Flatten,Dropout, Input
from readdata import get_data
import metadata
import numpy

#nb_epoch = 50

def main():
    data, label = get_data()

    a = len(metadata.trainOffset) - 1 
    #print a 

    #input_image = Input(data);    

    model = Sequential()

    model.add(Convolution2D(32, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    model.add(Convolution2D(64, 5, 5, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    model.add(Convolution2D(128, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    model.add(Convolution2D(128, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    #model.add(Convolution2D(256, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    #model.add(Activation("relu"))
    #model.add(Dropout(0.5))
    #model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    #model.add(Convolution2D(64, 3, 3, border_mode='same', input_shape=(128, 128, 3), dim_ordering='tf'))
    #model.add(Activation("relu"))
    #model.add(MaxPooling2D(pool_size=(2,2), strides=None, border_mode='valid', dim_ordering='tf'))

    model.add(Flatten())

    model.add(Dense(output_dim=1024, init='he_normal', activation='relu'))
    model.add(Dropout(0.5))
    #model.add(Dense(output_dim=512, init='he_normal', activation='relu'))
    #model.add(Dropout(0.5))
    #model.add(Dense(output_dim=128, init='he_normal', activation='relu'))
    #model.add(Dropout(0.5))
    #model.add(Dense(output_dim=64, init='he_normal', activation='relu'))
    #model.add(Dropout(0.5))
    #model.add(Dense(output_dim=32, init='he_normal', activation='relu'))
    #model.add(Dropout(0.5))
    model.add(Dense(output_dim = a, init = 'he_normal', activation = 'softmax'))
    
    model.compile(
        optimizer='adadelta', 
        loss='categorical_crossentropy', 
        metrics=['accuracy']
    )
    
    model.fit(data, label, nb_epoch = 100, batch_size=32)
 
    dataT, labelT = get_data('valid')   

    loss, acc = model.evaluate(dataT, labelT, verbose=False)
    print('loss:' + str(loss) + '\naccuracy:'+ str(acc))
if __name__ == '__main__':
    main()

