import glob
from shutil import copyfile
from os.path import basename

emotions = ["neutral", "anger", "contempt", "disgust", "fear", "happy", "sadness", "surprise"]
participants = glob.glob("dataset\\data_label\\*")

for x in participants:
	for sessions in glob.glob("%s\\*" %x):
		for files in glob.glob("%s\\*" %sessions):
			file = open(files, 'r')
			emotion = int(float(file.readline())) 
			basename_file = basename(files)
			name_file = basename_file.replace("_emotion.txt", ".png")
			sourcefile_emotion = files
			sourcefile_emotion = sourcefile_emotion.replace("_emotion.txt", ".png")
			sourcefile_emotion = sourcefile_emotion.replace("data_label", "data_image")
			destination_emotion = "dataset_label\\%s\\%s" % (emotions[emotion], name_file)
			copyfile(sourcefile_emotion, destination_emotion)
			print("%s copy to %s" %(name_file, emotions[emotion]))
	code_name_file = "%s" % name_file[-12:]
	name_file_neutral = name_file.replace(code_name_file, "00000001.png")
	sourcefile_emotion_neutral = sourcefile_emotion.replace(code_name_file, "00000001.png")
	destination_emotion_neutral = "dataset_label\\neutral\\%s" % (name_file_neutral)
	copyfile(sourcefile_emotion_neutral, destination_emotion_neutral)
	print("%s copy to neutral" % name_file_neutral)

# Untuk data gambar yang diambil adalah data yang memiliki label emotion.
