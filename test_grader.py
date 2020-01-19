from imutils.perspective import four_point_transform
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2
import pandas as pd
import xlwt
from xlwt import Workbook
import openpyxl



df = pd.DataFrame

def flp (x):

    col = 'Answer'
    t_col = 'Right'
    r = 'background-color: #fec7ce'
    g = 'background-color: #c7eecf'
    c = np.where (x [col] == x [t_col], g, r)
    y = pd.DataFrame ('', index=x.index, columns=x.columns)
    y [col] = c
    return y




def correct(file_name , file_nswer_key):
	d = pd.read_excel (file_nswer_key)
	ANSWER_KEY = d ['Answer'].values.tolist ()
	image = cv2.imread (file_name)
	""""""""""""
	#cv2.imshow ("Original", image)
	#cv2.waitKey (0)
	gray = cv2.cvtColor (image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur (gray, (5, 5), 0)
	edged = cv2.Canny (blurred, 75, 200)
	#cv2.imshow ("f", edged)
	cv2.imwrite ("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\edged.png", edged)
	#cv2.waitKey (0)

	cnts = cv2.findContours (edged.copy (), cv2.RETR_EXTERNAL,
							 cv2.CHAIN_APPROX_SIMPLE)

	cnts = imutils.grab_contours (cnts)

	docCnt = None
	how_many_times = 0

	if len (cnts) > 0:

		cnts = sorted (cnts, key=cv2.contourArea, reverse=True)

		for c in cnts:

			how_many_times += 1
			peri = cv2.arcLength (c, True)
			approx = cv2.approxPolyDP (c, 0.02 * peri, True)

			if len (approx) == 4:
				docCnt = approx
				break

	paper = four_point_transform (image, docCnt.reshape (4, 2))
	warped = four_point_transform (gray, docCnt.reshape (4, 2))
	cv2.imwrite ("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\warped.png", warped)

	thresh = cv2.threshold (warped, 0, 255,
							cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU) [1]
	#cv2.imshow ("thresh", thresh)
	cv2.imwrite ("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\thresh.png", thresh)
	#cv2.waitKey (0)

	cnts = cv2.findContours (thresh.copy (), cv2.RETR_EXTERNAL,
							 cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours (cnts)
	questionCnts = []

	for c in cnts:
		(x, y, w, h) = cv2.boundingRect (c)
		ar = w / float (h)
		""""
		mmm+=1
		print("*****")
		print(mmm)
		print("*******")
		print(x)
		print(y)
		print(w)
		print(h)
	"""
		if w >= 60 and h >= 60 and ar >= 0.9 and ar <= 2.1:
			questionCnts.append (c)
	#print (len (questionCnts))

	questionCnts = contours.sort_contours (questionCnts,
										   method="top-to-bottom") [0]
	correct = 0
	""""
	print(len (questionCnts))
	for cnt in questionCnts:
		color = (0, 0, 255)
		cv2.drawContours (paper, cnt, -1, color, 3)
	cv2.imshow("r",paper.copy())
	cv2.waitKey(0)
	cv2.imwrite("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\pp30.png",paper )
	"""
	you_answer = []
	key = []
	for (q, i) in enumerate (np.arange (0, len (questionCnts), 4)):

		cnts = contours.sort_contours (questionCnts [i:i + 4]) [0]
		bubbled = None
		ff=False

		for (j, c) in enumerate (cnts):
			mask = np.zeros (thresh.shape, dtype="uint8")
			cv2.drawContours (mask, [c], -1, 255, -1)

			mask = cv2.bitwise_and (thresh, thresh, mask=mask)
			total = cv2.countNonZero (mask)
			#print("*****")
			#print(j)
			#print(total)
			#print("******")
			if (bubbled is None) and total>2000:
				ff=True
				bubbled = (total, j+1)
			#elif bubbled is None and total<2000:
				#f=False
				#bubbled = (total, j+1)
			elif ~(bubbled is None) and  total > 2000:
				ff=True
				s = (bubbled [1]), (j + 1)

				bubbled = (total, s)



		color = (0, 0, 255)
		k = ANSWER_KEY [q]
		if ff:
			you_answer.append (bubbled [1])
		else:
			you_answer.append ("None")
		key.append (k + 1)

		if ff and k+1 == bubbled [1]:
			color = (0, 255, 0)
			correct += 1

		cv2.drawContours (paper, [cnts [k]], -1, color, 3)
	global df
	df = pd.DataFrame ({'Answer': you_answer, 'Right': key})
	print(df)
	print(type(df))
	score = (correct / 10.0) * 100
	cv2.putText (paper, "{:.2f}%".format (score), (10, 30),
				 cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

	cv2.imwrite ("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\original.png", image)
	#cv2.imshow ("Exam", paper)
	str="C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\paper.png"
	cv2.imwrite ("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images\\paper.png", paper)
	styled = df.style.apply (flp, axis=None)
	styled.to_excel ('styled.xlsx', engine='openpyxl')
	return str
	#cv2.waitKey (0)



"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to the input image")
args = vars(ap.parse_args())

"""

#correct("C:\\Users\\ANDISHASAZAN\\PycharmProjects\\optical\\venv\\Include\\images_test\\test1.jpg")
#correct("C:\\Users\\ANDISHASAZAN\\Desktop\\new_test_1.jpg" , "Answer_key.xlsx")
