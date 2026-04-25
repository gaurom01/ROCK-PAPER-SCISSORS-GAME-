import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import os
from gtts import gTTS
def mainmenu():
    pygame.mixer.init()

    def play_music(): #Used to play music
    
        pygame.mixer.music.load("F:\\CODING\\py\\Game\\background of menu\\bgmusic.mp3")  # Replace with your music file
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        print("Music started...")

    def stop_music(): #Stops the background music
   
        pygame.mixer.music.stop()
        print("Music stopped.")
    def start_game():
        messagebox.showinfo("Start Game", "Game will start now!")  # Placeholder for starting the game

    '''import sqlite3
    import random

    # Database setup
    def setup_database():
        conn = sqlite3.connect("rps_game.db")
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS game_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_choice TEXT NOT NULL,
                computer_choice TEXT NOT NULL,
                result TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    # Insert game results into the database
    def save_game_result(player_choice, computer_choice, result):
        conn = sqlite3.connect("rps_game.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO game_stats (player_choice, computer_choice, result)
            VALUES (?, ?, ?)
        """, (player_choice, computer_choice, result))
        conn.commit()
        conn.close()

    # Fetch game statistics
    def display_statistics():
        conn = sqlite3.connect("rps_game.db")
        cursor = conn.cursor()
        cursor.execute("SELECT result, COUNT(*) FROM game_stats GROUP BY result")
        stats = cursor.fetchall()
        print("\nGame Statistics:")
        for result, count in stats:
            print(f"{result}: {count}")
        conn.close()

    # Determine the winner
    def determine_winner(player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "scissors" and computer_choice == "paper") or \
            (player_choice == "paper" and computer_choice == "rock"):
            return "Win"
        else:
            return "Loss"

    # Main game loop
    def play_game():
        choices = ["rock", "paper", "scissors"]
        print("Welcome to Rock, Paper, Scissors!")
        
        while True:
            print("\nEnter your choice: rock, paper, or scissors")
            player_choice = input("Your choice: ").strip().lower()
            if player_choice not in choices:
                print("Invalid choice. Please choose rock, paper, or scissors.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(player_choice, computer_choice)
            print(f"You {result}!")

            # Save result to the database
            save_game_result(player_choice, computer_choice, result)

            # Ask to play again or show statistics
            next_action = input("\nPlay again? (yes to continue, stats to view statistics, or exit to quit): ").strip().lower()
            if next_action == "stats":
                display_statistics()
            elif next_action == "exit":
                print("Thanks for playing! Goodbye!")
                break

    # Setup database and start the game
    if __name__ == "__main__":
        setup_database()
        play_game()'''

    # Function for Leaderboard
    def show_leaderboard():
        stop_music()
        messagebox.showinfo("Leaderboard", "Coming Soon!")  # Placeholder

    # Function to quit the application
    def quit_game():
        root.destroy()
    play_music()
    # Create the main Tkinter window
    root = tk.Tk()
    root.title("Main Menu")
    root.geometry("800x600")  # Adjust size as per your image
    root.resizable(False, False)

    # Load the background image
    background_image = Image.open("F:\\CODING\\py\\Game\\background of menu\\background.jpg")  # Replace with your image file
    background_image = background_image.resize((800, 600))  # Resize to fit the window
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a Canvas and add the image
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

    '''#convert text to speech
    a_user=null
    choice=ROCK,PAPER,SCISSOR
    result=null
    text=a_user,"CHOOSED",choice,"AND",result
    tts=gTTS(text=text, lang='en' slow=False)
    tts.save("result.mp3")
    os.system("start result.mp3")'''
    

    # Add buttons on top of the background
    start_button = tk.Button(root, text="Start Game", font=("Arial", 16), command=start_game)
    leaderboard_button = tk.Button(root, text="Leaderboard", font=("Arial", 16), command=show_leaderboard)
    quit_button = tk.Button(root, text="Quit", font=("Arial", 16), command=quit_game)

    # Place buttons on the canvas
    canvas.create_window(400, 200, window=start_button)  # X, Y coordinates
    canvas.create_window(400, 300, window=leaderboard_button)
    canvas.create_window(400, 400, window=quit_button)

    # Run the Tkinter event loop
    root.mainloop()
    
mainmenu()
