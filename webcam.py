import cv2
# Define a video capture object
vid = cv2.VideoCapture(0)
while(True):
    # Capture the video frame by frame
    ret, frame = vid.read()
    # Display the resulting frame
    cv2.imshow('frame', frame)
    # The 'q' button is set as the quitting button, but you may use any button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()