#importing the required libraries
import cv2

#loading the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def detect(gray, frame):
    '''
        This function takes the images, detects faces and eyes and
        draws a rectangle around them.

        Parameters:
            gray : The grayscale image
            frame : The color image
        Returns:
            the function will return the color image with rectangles
            plotted on faces and eyes.
    '''
    faces = face_cascade.detectMultiScale(gray, 1.3, 1)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        
        for xe, ye, we, he in eyes:
            cv2.rectangle(roi_color, (xe, ye), (xe+we, ye+he), (0, 255, 0), 2)

    return frame

image_path = 'assets/img1.jpg'
save_path = 'output/img1.jpg'

frame = cv2.imread(image_path)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
canvas = detect(gray, frame)

cv2.putText(canvas, 'Press ESC to quit', (0,15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,255,0))
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)

cv2.imwrite(save_path, canvas)

while True: 
    cv2.imshow('Image', canvas)
    if cv2.waitKey(1) == 27:
        break

#destroys the window
cv2.destroyAllWindows()
