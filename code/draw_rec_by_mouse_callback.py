import cv2

drawing = False
start_x, start_y = -1, -1

# Mouse callback function
def draw_rectangle(event, x, y,flags,param):
    global drawing, start_x, start_y
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            copy_resize = resize.copy()
            cv2.rectangle(copy_resize, (start_x, start_y), (x, y), (0, 255, 0), 2)
            cv2.imshow('Image', copy_resize)
        
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(resize, (start_x, start_y), (x, y), (0, 255, 0), 2)
        cv2.imshow('Image', resize)

# Load the image
image = cv2.imread('captures/frame_100.jpg')
resize = cv2.resize(image, (960, 540)) # resize because image file is too big

# mouse_call_back_fun
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', draw_rectangle)

# for saving images
while True:
    cv2.imshow('Image', resize)
    key = cv2.waitKey(1) & 0xFF
    
    # If 's' is pressed, save the image and break out of the loop
    if key == ord('s'):
        save_path = 'labelled/labelled_100.jpg'
        cv2.imwrite(save_path, resize)
        print(f"Image saved to {save_path}")
        break
    elif key == 27:  # ESC key
        break

cv2.destroyAllWindows()
