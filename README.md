# Rock-Paper-Scissors Game using OpenCV and Hand Tracking

This project is a Rock-Paper-Scissors game implemented using OpenCV for image processing and a custom hand tracking module (`HandTrackingModule.py`). The game uses a webcam feed to detect hand gestures and play against a computer opponent. The player can start, pause, and quit the game using specific key events.

## Features

- Real-time hand gesture detection using OpenCV
- Simple and interactive user interface
- Score tracking for both player and computer
- Ability to start, pause, and quit the game using keyboard controls

## Installation

### Prerequisites

- Python 3.x
- OpenCV
- Required Python packages: `numpy`, `mediapipe`

### Steps

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/RockPaperScissor-OpenCV.git
    cd RockPaperScissor-OpenCV
    ```

2. **Install the required packages:**

    ```sh
    pip install opencv-python numpy mediapipe
    ```

3. **Ensure you have the necessary hand tracking module:**

    Make sure you have the `HandTrackingModule.py` file in the project directory.

4. **Place the gesture images:**

    Ensure the images for gestures (`rock.jpg`, `paper.jpg`, `scissor.jpg`) are located in the `Fingers` directory inside the project directory.

5. **Run the game:**

    ```sh
    python rock_paper_scissors.py
    ```

## How to Play

1. **Start the Game:**
    - Press `s` to start the game.

2. **Pause/Resume the Game:**
    - Press `p` to pause or resume the game.

3. **Quit the Game:**
    - Press `q` to quit the game.

## Game Controls

- **Start the game**: Press `s`
- **Pause/Resume the game**: Press `p`
- **Quit the game**: Press `q`

## Hand Gestures

- **Rock**: Show a closed fist
- **Paper**: Show an open hand
- **Scissor**: Show a V-sign with your index and middle fingers

## Score Display

- The player's score is displayed on the right side of the screen.
- The computer's score is displayed on the left side of the screen.

## Directory Structure

```
RockPaperScissor-OpenCV
├── Fingers
│   ├── rock.jpg
│   ├── paper.jpg
│   ├── scissor.jpg
├── HandTrackingModule.py
├── rock_paper_scissors.py
```

## Troubleshooting

- Ensure your webcam is working and properly connected.
- Check the paths to the gesture images in the `Fingers` directory.
- Verify that the required Python packages are installed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The hand tracking functionality is powered by MediaPipe.
- Special thanks to OpenCV for providing an extensive library for image processing.

