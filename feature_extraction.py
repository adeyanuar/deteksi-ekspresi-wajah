import cv2
import glob
import random
import math
import numpy as np
import dlib

emotions = ["neutral", "anger", "disgust", "fear", "happy", "sadness", "surprise"]
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("../shape_predictor_68_face_landmarks.dat")

def get_files(emotion): 
    files = glob.glob("dataset_preprocessing\\%s\\*" %emotion)
    random.shuffle(files)
    training = files[:int(len(files)*0.9)]
    nprediction = len(files) - len(training) 
    prediction = files[-nprediction:] 
    return training, prediction

def get_landmarks(images):
    image = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)
    detections = detector(image, 1)
    for k,d in enumerate(detections):
        shape = predictor(image, d) 
        xlist = []
        ylist = []
        for i in range(0,68):
            xlist.append(float(shape.part(i).x))
            ylist.append(float(shape.part(i).y))
        xc = np.mean(xlist)
        yc = np.mean(ylist)
        xl = [(x-xc) for x in xlist]
        yl = [(y-yc) for y in ylist]
        landmarks_vectorised = []
        for x, y, w, z in zip(xl, yl, xlist, ylist):
            landmarks_vectorised.append(w)
            landmarks_vectorised.append(z)
            dist = math.sqrt(math.pow(x, 2)+math.pow(y, 2))
            landmarks_vectorised.append(dist)
            angle = (math.atan2(y, x)*360)/(2*math.pi)
            landmarks_vectorised.append(angle)
        landmarks = landmarks_vectorised
    if len(detections) < 1: 
        landmarks = "error"
    return landmarks
    
training_data = []
training_labels = []
prediction_data = []
prediction_labels = []
for emotion in emotions:
    training, prediction = get_files(emotion)
    for item in training:
        images = cv2.imread(item)
        landmark = get_landmarks(images)
        if landmark == "error":
            pass
        else:
            training_data.append(landmark)
            training_labels.append(emotions.index(emotion))
    for item in prediction:
        images = cv2.imread(item)
        landmark = get_landmarks(images)
        if landmark == "error":
            pass
        else:
            prediction_data.append(landmark)
            prediction_labels.append(emotions.index(emotion))

np.save('feature_landmark/%s/training_data.npy' %i, training_data)
np.save('feature_landmark/%s/training_labels.npy' %i, training_labels)
np.save('feature_landmark/%s/prediction_data.npy' %i, prediction_data)
np.save('feature_landmark/%s/prediction_labels.npy' %i, prediction_labels)  