import cv2
import numpy as np

cap = cv2.VideoCapture('rtsp://admin:pass@10.43.64.134/rtsph2641080p')

# Get the frames per second (fps) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the number of frames to skip for a 5 second interval
frames_to_skip = 2 * fps

# Counter for frames
frame_count = 0

desired_width = 800 

while(True):
    ret, frame = cap.read()
    if not ret:
        # If frame is not read correctly, skip this iteration
        continue

    resize = cv2.resize(frame, (960, 540))
    
    # Save frame at every 5 second interval
    if frame_count % frames_to_skip == 0:
        cv2.imwrite(f"captured_frame_{frame_count}.png", frame)
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', resize)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    frame_count += 1

cap.release()
cv2.destroyAllWindows()
