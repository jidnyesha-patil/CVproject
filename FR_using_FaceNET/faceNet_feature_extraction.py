from keras.models import load_model
import cv2
import numpy as np
import os
from load_faces import load_faces
from sklearn.model_selection import train_test_split
model = load_model('facenet_keras.h5',compile = False)
doc = load_faces()
label = np.array(doc["label"])
images = np.array(doc["images"])

trainX, testX, trainy, testy = train_test_split(
images, label, test_size=0.25, random_state=42)

# get the face embedding for one face
def get_embedding(face_pixels,model):
    # scale pixel values
    face_pixels = face_pixels.astype('float32')
    # standardize pixel values across channels (global)
    mean, std = face_pixels.mean(), face_pixels.std()
    face_pixels = (face_pixels - mean) / std
    # transform face into one sample
    samples = np.expand_dims(face_pixels, axis=0)
    # make prediction to get embedding
    yhat = model.predict(samples)
    return yhat[0]

def generate_embeddings(trainX=trainX,testX=testX,trainy=trainy,testy=testy):    
    # convert each face in the train set to an embedding
    newTrainX = list()
    model = load_model('facenet_keras.h5',compile = False)
    for face_pixels in trainX:
        embedding = get_embedding(face_pixels,model)
        newTrainX.append(embedding)
    newTrainX = np.asarray(newTrainX)
    print(newTrainX.shape)
    # convert each face in the test set to an embedding
    newTestX = list()
    for face_pixels in testX:
        embedding = get_embedding(face_pixels,model)
        newTestX.append(embedding)
    newTestX = np.asarray(newTestX)
    print(newTestX.shape)
    return (newTrainX, newTestX, trainy, testy)