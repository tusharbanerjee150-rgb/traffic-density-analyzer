import cv2

# Load video
cap = cv2.VideoCapture("data/traffic.mp4")

# Load car cascade
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")

# Check if video loaded
if not cap.isOpened():
    print("❌ Error: Video not loaded")
    exit()

print("✅ Video loaded successfully")

while True:
    ret, frame = cap.read()

    # Stop if video ends
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cars
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)

    car_count = 0

    # Loop through detections
    for (x, y, w, h) in cars:
        # Filter unwanted detections
        if w < 60 or h < 60 or w > 300 or h > 300:
            continue

        car_count += 1

        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Density classification
    if car_count < 3:
        density = "Low"
    elif car_count < 8:
        density = "Medium"
    else:
        density = "High"

    # Display text
    cv2.putText(frame, f"Cars: {car_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.putText(frame, f"Density: {density}", (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show output
    cv2.imshow("Traffic Analyzer", frame)

    # Exit on ESC key
    if cv2.waitKey(25) == 27:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()