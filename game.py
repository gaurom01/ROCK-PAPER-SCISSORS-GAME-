import sqlite3
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
    play_game()
