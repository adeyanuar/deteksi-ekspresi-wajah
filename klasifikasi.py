import numpy as np
from sklearn.svm import SVC

clf = SVC(kernel='linear', probability=True, decision_function_shape="ovo")

feature = 'feature_landmark' 
training_data = np.load('%s\\training_data.npy' %(feature))
training_labels = np.load('%s\\training_labels.npy' %(feature))
prediction_data = np.load('%s\\prediction_data.npy' %(feature))
prediction_labels = np.load('%s\\prediction_labels.npy' %(feature))

clf.fit(training_data, training_labels)
predic = clf.score(prediction_data, prediction_labels)
print(predic)
