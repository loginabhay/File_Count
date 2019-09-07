import cv2 
import os
import argparse


ap = argparse.ArgumentParser(description='videos to image')
ap.add_argument("-i", "--input", required=True,
	help="path to input video")
ap.add_argument("-o", "--output", required=True,
	help="path to output image")
ap.add_argument("-d", "--date", required=True,
	help="Required date")
args = vars(ap.parse_args())

p = os.path.join(args["output"], 'Img'+ args["date"])
os.mkdir(p)
count = 0
for file in os.listdir(args["input"]):
	path = os.path.join(args["input"],file)
	vid = cv2.VideoCapture(path)
	success,image = vid.read()
	while success:
		name = args["date"] + 'img' + str(count) + '.jpg'
		if count%15 == 0:
			cv2.imwrite(os.path.join(p, name), image) # save frame as JPEG file
  
		success,image = vid.read()
		print('Read a new frame: ', success)
		count += 1
