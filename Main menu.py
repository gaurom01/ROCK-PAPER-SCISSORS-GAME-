import pygame
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from cv1 import userinput
def mainmenu():
    pygame.mixer.init()

    def play_music(): #Used to play music
    
        pygame.mixer.music.load("F:\\Rockpaperscissor\\bgmusic.mp3")
        pygame.mixer.music.play(-1)  # -1 means loop indefinitely
        print("Music started...")

    def stop_music(): #Stops the background music
   
        pygame.mixer.music.stop()
        print("Music stopped.")
    def start_game():
        pygame.mixer.music.load("F:\\Rockpaperscissor\\click.mp3") 
        pygame.mixer.music.play(1)  # 
        print("Click started...")
        root.withdraw()
        import GameTest

    # Function for Leaderboard
    def show_leaderboard():
        stop_music()
        pygame.mixer.music.load("F:\\Rockpaperscissor\\click.mp3") 
        pygame.mixer.music.play(1)  # 
        print("Click started...")
        root.withdraw()
        import Leaderboard

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
    background_image = Image.open("F:\\Rockpaperscissor\\background.jpg")  # Replace with your image file
    background_image = background_image.resize((800, 600))  # Resize to fit the window
    background_photo = ImageTk.PhotoImage(background_image)

    # Create a Canvas and add the image
    canvas = tk.Canvas(root, width=800, height=600)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=background_photo, anchor="nw")

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