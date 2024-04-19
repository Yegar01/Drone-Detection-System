from ultralytics import YOLO
import cv2

model = YOLO('C:\\Users\\dattu\\OneDrive\\Desktop\\drone\\Drone-Detection-System\\best-300e.pt')

cap = cv2.VideoCapture(1)
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run tracking on the current frame
    results = model.track(frame, persist=True)

    # Check if tracking IDs are available
    if hasattr(results[0].boxes, 'id') and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu().numpy().astype(int)
        ids = results[0].boxes.id.cpu().numpy().astype(int)

        # Draw boxes and IDs on the frame
        for box, id in zip(boxes, ids):
            cv2.rectangle(frame, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)
            cv2.putText(frame, f"Id {id}", (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    else:
        print("Tracking IDs not available.")

    # Display the frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()