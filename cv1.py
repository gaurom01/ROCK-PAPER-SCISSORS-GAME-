import cv2
from cvzone.HandTrackingModule import HandDetector
import time

def userinput():
    # Initialize camera and hand detector
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    detector = HandDetector(maxHands=1)  # Detect one hand
    gesture = "Unknown"  # Default gesture
    start_time = time.time()  # Start the timer

    while True:
        success, img = cap.read()
        if not success:
            break

        # Find hands in the frame
        hands, img = detector.findHands(img, flipType=False)  # Detection with no flip

        if hands:
            # Process the first detected hand
            hand = hands[0]
            fingers = detector.fingersUp(hand)  # Get the state of fingers

            # Detect hand gestures
            if fingers == [0, 0, 0, 0, 0]:
                gesture = "Rock"
            elif fingers == [1, 1, 1, 1, 1]:
                gesture = "Paper"
            elif fingers == [0, 1, 1, 0, 0]:
                gesture = "Scissors"
            else:
                gesture = "Unknown"

            # Display the detected gesture on the screen
            cv2.putText(img, f"Gesture: {gesture}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        # Display the image
        cv2.imshow("Hand Gesture", img)

        # Check if 2 seconds have passed since gesture detection
        if gesture != "Unknown" and time.time() - start_time > 2:
            break

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

    return gesture  # Return the detected gesture

