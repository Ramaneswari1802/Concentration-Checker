import cv2
import time
import pygame
import threading

# Initialize pygame mixer
pygame.mixer.init()

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

# Load eye cascade
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# User input for focus time
focus_minutes = int(input("Enter focus time in minutes: "))
focus_seconds = focus_minutes * 60

cap = cv2.VideoCapture(0)

start_time = time.time()
status = "Focused"
last_status = "Focused"
eye_closed_frames = 0
EYE_CLOSED_THRESHOLD = 45  # Tolerate blinks up to ~1.5 seconds

print("Focus session started! Stay focused.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)

    if len(eyes) == 0:
        eye_closed_frames += 1
    else:
        eye_closed_frames = 0

    if eye_closed_frames > EYE_CLOSED_THRESHOLD:
        status = "Not Focused"
    else:
        status = "Focused"

    if status != last_status:
        if status == "Not Focused":
            threading.Thread(target=play_sound, args=("beep.mp3",)).start()
        last_status = status

    color = (0, 255, 0) if status == "Focused" else (0, 0, 255)
    cv2.putText(frame, f"Status: {status}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    cv2.imshow("Concentration Checker", frame)

    if time.time() - start_time >= focus_seconds:
        play_sound("success.mp3")
        print("✅ Goal Completed! You stayed focused.")
        time.sleep(3)
        break

    if cv2.waitKey(1) == 27:
        print("Session stopped early.")
        break

cap.release()
cv2.destroyAllWindows()
