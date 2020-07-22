import cv2

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(r"C:\Users\Aseel Sh\PycharmProjects\untitled3\tr\haarcascade_frontalface_default.xml")

# Read the image
image = cv2.imread(r"C:\Users\Aseel Sh\PycharmProjects\untitled3\tr\t.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (100, 0, 0), 2)
cv2.imshow("Faces found", image)
cv2.waitKey()
