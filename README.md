# Concentration Checker

A Python-based eye-tracking tool that helps users stay focused using webcam input. It detects blinks and eye closure using MediaPipe and plays alert sounds if concentration is lost. After successfully staying focused for a fixed amount of time, it plays a success sound.

## Features
- Real-time focus monitoring via webcam
- Beep alert for loss of concentration
- Custom time input for focus goal
- Success sound upon completion

## Use Cases
- Students preparing for exams
- Remote workers avoiding distractions
- Study sessions or Pomodoro-style deep work

## Requirements
- Python 3.x
- OpenCV
- MediaPipe
- Pygame

## Installation
```bash
pip install opencv-python mediapipe pygame
```

## How to Run
1. Clone this repository.
2. Place `beep.mp3` and `success.mp3` in the same folder.
3. Run the Python script:
```bash
python concentration_checker.py
```

## License
MIT License
