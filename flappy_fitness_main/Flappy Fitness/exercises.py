import cv2
import mediapipe as mp
import os
import socketio
import threading
import time
import random

sio = socketio.Client()

# Initialize MediaPipe Pose
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.7
)

# Initialize video capture
cap = cv2.VideoCapture(0)

# Global variables
count = 0
position = None
start_time = time.time()
exercise = random.choice(["Jumping Jacks", "Squats", "Toe Touches"])

# Function to process video frames
def process_frame():

    global position, count, start_time, exercise
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Empty Camera")
            break

        # Update exercise every 5 seconds
        current_time = time.time()
        if current_time - start_time > 10:
            start_time = current_time
            exercise = random.choice(["Jumping Jacks", "Squats", "Toe Touches"])
            

        if exercise == "Jumping Jacks":
            val1, val2, val3, val4 = 12, 14, 11, 13
        elif exercise == "Squats" or exercise == "Toe Touches":
            val1, val2, val3, val4 = 25, 19, 26, 20

        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        result = pose.process(image)
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        imlist = []
        if result.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, result.pose_landmarks, mp_pose.POSE_CONNECTIONS
            )
            for id, lm in enumerate(result.pose_landmarks.landmark):
                h, w, _ = image.shape
                X, Y = int(lm.x * w), int(lm.y * h)
                imlist.append([id, X, Y])
        if len(imlist) != 0:
            if imlist[val1][2] >= imlist[val2][2] and imlist[val3][2] >= imlist[val4][2]:
                position = "down"
            if imlist[val1][2] < imlist[val2][2] and imlist[val3][2] < imlist[val4][2] and position == "down":
                position = "up"
                count += 1
                sio.emit('jumping_jack', {'detected': True})
                print(f"{exercise} Count:", count)
        
        # Display exercise and count
        cv2.putText(image, f'{exercise} | Total Reps: {count}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        cv2.imshow('Exercise Detection', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()



def connect_to_server():
    sio.connect('http://localhost:8000')
    sio.wait()

@sio.event
def connect():
    print('JJ connected to server')
    

@sio.event
def disconnect():
    print('Disconnected from server')



threading.Thread(target=connect_to_server).start()
process_frame()
# signal_file = 'jump_signal.txt'