import cv2

# Read the image
image = cv2.imread('0103.jpg')

# starting and ending coordinates
x1, y1 = 15, 110
x2, y2 = 280, 440

# Draw the rectangle
cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  

# Display the image with the rectangle
cv2.imshow('Rectangle Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()