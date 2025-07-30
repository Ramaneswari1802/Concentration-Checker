# Concentration Checker

A Python-based eye-tracking tool that helps users stay focused using webcam input. It detects blinks and eye closure using MediaPipe and plays alert sounds if concentration is lost. After successfully staying focused for a fixed amount of time, it plays a success sound.

## Features

- Tracks eye status via webcam
- Beep alert if eyes are closed (loss of focus)
- Success sound after focus session completion
- Lightweight and easy to use

## Real-world Use Cases

- Students preparing for exams without distractions
- Remote workers maintaining focus during work hours
- Developers or writers using focus techniques (like Pomodoro)
- Anyone seeking to improve focus and avoid procrastination

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- pygame

## Installation

```bash
pip install opencv-python mediapipe pygame

