import cv2
import random
import sqlite3
import mediapipe as mp

# Initialize SQLite database
def initialize_database():
    conn = sqlite3.connect("rps_game.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS game_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_choice TEXT,
            computer_choice TEXT,
            result TEXT
        )
    """)
    conn.commit()
    conn.close()

# Save result to database
def save_to_database(user_choice, computer_choice, result):
    conn = sqlite3.connect("rps_game.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO game_results (user_choice, computer_choice, result)
        VALUES (?, ?, ?)
    """, (user_choice, computer_choice, result))
    conn.commit()
    conn.close()

# Determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Draw"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "User Wins"
    else:
        return "Computer Wins"

# Map hand gesture to choice
def detect_hand_gesture(frame, hand_landmarks):
    if hand_landmarks:
        landmarks = hand_landmarks[0].landmark

        # Simple logic for gesture detection (customize as needed)
        thumb_tip = landmarks[4].y
        index_tip = landmarks[8].y
        middle_tip = landmarks[12].y

        if thumb_tip > index_tip and thumb_tip > middle_tip:
            return "rock"
        elif thumb_tip < index_tip and thumb_tip < middle_tip:
            return "scissors"
        else:
            return "paper"

# Main Game Loop
def play_game():
    initialize_database()
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    cap = cv2.VideoCapture(0)

    print("Press 'q' to quit the game.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Flip the frame for a mirrored effect
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect hands
        results = hands.process(rgb_frame)

        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )

        # Detect user gesture
        user_choice = None
        if results.multi_hand_landmarks:
            user_choice = detect_hand_gesture(frame, results.multi_hand_landmarks)

        # Display detected choice
        if user_choice:
            cv2.putText(frame, f"User Choice: {user_choice}", (10, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Generate computer choice
            computer_choice = random.choice(["rock", "paper", "scissors"])

            # Determine winner
            result = determine_winner(user_choice, computer_choice)
            print(f"User: {user_choice}, Computer: {computer_choice}, Result: {result}")

            # Save to database
            save_to_database(user_choice, computer_choice, result)

        # Display the frame
        cv2.imshow("Rock Paper Scissors", frame)

        # Quit the game
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Run the game
if __name__ == "__main__":
    play_game()
