##Installing OpenCV and Gradio in Envionment Variables
#Installing opencv-python gradio

###Imoporting Packages

import imutils #Resize Image
import cv2 #Opening CV


redLower = (58, 95, 80)
redUpper = (147, 255, 255)

camera=cv2.VideoCapture(0) #Obtain feed from camera
while True:

        (grabbed, frame) = camera.read() #Read from the Camera

    frame = imutils.resize(frame, width=1000) #Resizing the Image
    blurred = cv2.GaussianBlur(frame, (11, 11), 0) #Smoothening the Image 
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #Converting the Color to Gray Scale Image
    

        mask = cv2.inRange(hsv, redLower, redUpper) #Mask the blue colour
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)


        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        if len(cnts) > 0: #Capture frame-by-frame
                c = max(cnts, key=cv2.contourArea)
                ((x, y), radius) = cv2.minEnclosingCircle(c)
                M = cv2.moments(c)
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                if radius > 10:
                        cv2.circle(frame, (int(x), int(y)), int(radius),
                                (0, 255, 255), 2)
                        cv2.circle(frame, center, 5, (0, 0, 255), -1)
                        #print(center,radius)
                        if radius > 250:
                                print("stop") #Display the resulting frame
                        else:
                                if(center[0]<150):
                                        print("Right")
                                elif(center[0]>450):
                                        print("Left")
                                elif(radius<250):
                                        print("Front")
                                else:
                                        print("Stop")
        cv2.imshow("Frame", frame) #Draw Bounding Boxes
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break

camera.release()
cv2.destroyAllWindows()
