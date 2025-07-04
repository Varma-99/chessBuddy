## Chessboard to FEN + Stockfish Assistant

This project detects a chessboard from an image or screen capture, converts the position to FEN (Forsyth–Edwards Notation), uses Stockfish to calculate the best move, and optionally displays that move live on screen. It is designed as an educational tool to explore the integration of computer vision, machine learning, engine-based analysis, and real-time overlay systems.

**🔬 Built for learning — not for real-time gameplay assistance.**

## Features
🖼️ Detects chessboard from screenshots or images
🧠 Converts board position to FEN using a trained model (board_to_fen)
♜ Uses Stockfish to calculate the best move
👁️ Displays the best move on-screen (overlay or console output)
💡 Robust to different board styles, themes, and lighting conditions

## Tech Used
Python
OpenCV (image preprocessing, warping, masking)
TensorFlow/Keras (via board_to_fen)
Stockfish (via subprocess)
Pillow, NumPy, PyAutoGUI (optional for screen handling)

## Project Goal
This project was created to explore:
--How raw images can be converted into structured game states
--How to connect vision models with external decision systems like chess engines
--Real-time automation using Python, with practical applications in AR, training tools, and computer vision
--It was not designed to be used during live games or to gain unfair advantage — this is strictly a technical and educational project.

## Collaborators 👥

Harihara Varma (Varma-99),
Nymish Reddy(nymishreddy)
