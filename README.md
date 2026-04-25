Rock-Paper-Scissors (Computer Vision Based)
Overview
This project is a computer vision–based Rock-Paper-Scissors game that allows users to play using real-time hand gesture recognition instead of traditional inputs. The system captures video through a webcam and uses Python to detect and classify gestures as rock, paper, or scissors.

Features
Real-time hand gesture detection using Computer Vision
Interactive gameplay against the computer
3-round game structure
Stores results (user moves, system moves, outcomes) in SQL database
Simple and user-friendly interface
Tech Stack
Python
OpenCV (Computer Vision)
SQL (Database)
How It Works
The webcam captures the user's hand gesture.
The system processes the image and identifies the gesture.
The computer generates a random move.
The winner is decided based on standard game rules.
Results are stored in a SQL database.
How to Run
Clone the repository

Install required libraries:

pip install opencv-python
Run the main Python file:

python main.py
Future Improvements
Add GUI for better user experience
Increase number of rounds or game modes
Add score visualization and analytics
Author
OM GAUR
