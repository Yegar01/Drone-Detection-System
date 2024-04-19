from ultralytics import YOLO
import cv2

model = YOLO('C:\\Users\\shubh\\OneDrive\\Desktop\\python\\drone\\Drone-Detection-System\\best-300e.pt')

cap = cv2.VideoCapture(1)
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 tracking on the frame, persisting tracks between frames
        results = model.track(frame, persist=True)
        # Visualize the results on the frame
        print(results[0].obb)

        # Display the annotated frame
        cv2.imshow("YOLOv8 Tracking", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break
print(results[0].obb)
# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()