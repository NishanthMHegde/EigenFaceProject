import numpy as np
import cv2
import os
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer=cv2.createEigenFaceRecognizer()
recognizer.load('recognizer/trainingData.yml') #load the trainingdata into the recognizer
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4) #font to use to display user ID
path = "user10tdata"
imagePath = [os.path.join(path,f) for f in os.listdir(path)]
count =0
sample=0
unknown=0
for image in imagePath:
    sample = sample +1
    color = cv2.imread(image) #read the testing image

    img = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY) #onvert the image to grayscale
    faces = face_cascade.detectMultiScale(img,1.3,5) #detect the face portion within the grayscale

    for(x,y,w,h) in faces: # starting coordinate, width and height of face
        cv2.rectangle(color,(x,y),(x+w,y+h),(255,0,0),3)
        gaus = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,43,0) #apply Gaussian adaptive threshold to the image

        p_image = gaus[y:y+h,x:x+w]  #store the region of interest in a temporary variable
        img = cv2.resize(p_image,(640,480)) #resize the image to match that of the training data

        id,conf = recognizer.predict(img) #use the predictor to predict the userID
        if id==10:
            print "found"
            count =count +1
        else :
            unknown =unknown+1



        cv2.cv.PutText(cv2.cv.fromarray(color),str(id),(x,y+h),font,255) #display the user ID that has been retrieved
        cv2.imshow('gaus',gaus)

    cv2.imshow('img',color)

    cv2.waitKey(100)




print str(count)
print str(sample)
print "unknown" + str(unknown)


cv2.destroyAllWindows()
