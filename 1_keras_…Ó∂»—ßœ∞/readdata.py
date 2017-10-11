import metadata 
from PIL import Image
import numpy

def get_data(dataType = "train"):
    if dataType == "train":
        offset = metadata.trainOffset
        path = metadata.trainPath
    elif dataType == "valid":
        offset = metadata.validOffset
        path = metadata.validPath
    else:
        raise ValueError("train or valid")

    total_number = offset[len(offset) - 1]
  

    data = numpy.zeros([total_number, 128, 128, 3], dtype = numpy.float32)

    for i in xrange(0, total_number):
        filename = path + str(i) + ".jpg"
        img = Image.open(filename)
        sample = numpy.array(img)
        data[i, :, :, :] = sample
    
    # get labels
    class_num = len(offset) - 1
    labels = numpy.zeros([total_number, class_num], dtype = numpy.float32)
    for i in xrange(0, len(offset) - 1):
        for j in xrange(offset[i], offset[i+1]):
            labels[j][i] = 1.0

    #print len(offset) - 1
    
    return data, labels

if __name__ == "__main__":
    data, labels = get_data()
    print numpy.shape(labels)
    print numpy.shape(data)
  
