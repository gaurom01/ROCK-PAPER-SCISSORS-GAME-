import database  # Assuming the database functions are in a file named database.py
import pyttsx3
import random
import time
from cv1 import userinput  # Assuming the `userinput` function is in a separate script

# Function to speak text
def speak(text, delay=0):
    time.sleep(delay)  # Add a delay before speaking
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function to speak text without delay
def speak1(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Game setup
result = ""
rounds = 3
player_score = 0
computer_score = 0
choices = ("Rock", "Paper", "Scissors")
player_name = input("Enter your name: ")

# Welcome the player
speech = f"Hi {player_name}, welcome to Rock, Paper, Scissors!"
speak1(speech)

# Main game loop
for i in range(1, rounds + 1):
    speak(f"Round {i}", 1)
    computer_choice = random.choice(choices)
    speak("Are you ready?", 2)
    speak("Rock", 1)
    speak("Paper", 1)
    speak("Scissors", 1)
    
    # Get the player's gesture
    player_gesture = userinput()
    

    if (player_gesture == "Rock" and computer_choice == "Scissors") or \
       (player_gesture == "Scissors" and computer_choice == "Paper") or \
       (player_gesture == "Paper" and computer_choice == "Rock"):
        player_score += 1
        speak(f"Computer chose {computer_choice} and Player chose {player_gesture}", 1)
        speak1(f"{player_name} got 1 point")
    elif player_gesture == computer_choice:
        speak(f"Computer chose {computer_choice} and Player chose {player_gesture}", 1)
        speak("It's a Tie!")
        computer_score += 1
        player_score += 1
    elif (player_gesture == "Scissors" and computer_choice == "Rock") or \
         (player_gesture == "Paper" and computer_choice == "Scissors") or \
         (player_gesture == "Rock" and computer_choice == "Paper"):
        computer_score += 1
        speak(f"Computer chose {computer_choice} and Player chose {player_gesture}", 1)
        speak("Computer got 1 point")
    else:
        speak("Hey! Use accurate gestures.")

# Final results
if player_score > computer_score:
    speak(f"Congratulations! {player_name} wins with a score of {player_score} to {computer_score}")
    result = "Won"
elif player_score < computer_score:
    speak(f"Computer wins with a score of {computer_score} to {player_score}")
    result = "Lost"
else:
    speak(f"It's a tie! Both scored {player_score}")
    result = "Tie"

# Save results to the database
try:
    conn = database.mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="GameScores"
    )
    if conn.is_connected():
        print("Connected to the database. Saving results...")
        database.insert_entry(conn, "GameResults", player_name, player_score, computer_score, result)
        print("Game results saved successfully!")
except database.Error as e:
    print(f"Error saving results to the database: {e}")
finally:
    if conn:
        conn.close()
