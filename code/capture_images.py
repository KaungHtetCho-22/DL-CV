import cv2

capture = cv2.VideoCapture('rtsp://admin:pass@10.43.64.134/rtsph2641080p')

img_counter = 1500

while True:

    ret, frame = capture.read(capture)

    resize = cv2.resize(frame, (960, 540))

    cv2.imshow("test", resize)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        break

    elif k%256 == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

capture.release()

cv2.destroyAllWindows()