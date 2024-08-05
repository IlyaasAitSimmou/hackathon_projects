# Flappy Fitness

Flappy Fitness is an interactive fitness game that uses a camera to track exercises and provide real-time feedback. The game features three main exercises: squats, jumping jacks, and toe touches.

![Flappy Fitness](https://github.com/user-attachments/assets/04277aef-40bf-42c4-8f7c-ade62e6d2e25)

## Files and Their Purposes

- `main.py`: Initializes the game, connects to the server, and runs the main game loop.
- `exercises.py`: Handles exercise detection using computer vision and connects to the server to send exercise data.
- `server.py`: Handles server-side operations, including connecting clients and receiving exercise data.
- `run_it_all.py`: Runs the main, exercise, and server files concurrently.

## Setup Instructions

1. **Install Dependencies**: Ensure you have all the required dependencies installed. You can install them using pip.
    ```bash
    pip install pygame socketio opencv-python mediapipe eventlet
    ```

2. **Run the Application**: Execute the `run_it_all.py` script to start the game, exercise detection, and server concurrently.
    ```bash
    python run_it_all.py
    ```

## Gameplay Instructions

![Screenshot 2024-07-31 002244](https://github.com/user-attachments/assets/050b2950-257c-438f-b23a-b5905b7987f0)

1. **Starting the Game**:
    - When you start the game, it will connect to the server and wait for the player to begin.
    - The game will randomly select one of the three exercises: squats, jumping jacks, or toe touches.

2. **Exercise Guidelines**:
    - **Squats**: Ensure your arms go below your knees and your legs form a 90-degree angle.
    - **Jumping Jacks**: Your arms should touch at the top and then retreat back while jumping.
    - **Toe Touches**: Your hands should completely touch your toes.

3. **Camera Setup**:
    - Ensure your entire body is visible in the camera frame at all times for accurate detection.
    - Position yourself at a distance where your full body fits within the camera view.

4. **In-Game Feedback**:
    - The game will provide real-time feedback on your exercise form and count your repetitions.
    - Make sure to follow the visual feedback to maintain proper form.

## Features

![Screenshot 2024-07-31 001255](https://github.com/user-attachments/assets/06ee3ce5-f6ab-4733-8609-1bd56880eb5b)
![Screenshot 2024-07-31 001400](https://github.com/user-attachments/assets/57e5709a-6d33-4a56-ba08-5764ca905e5b)

- **Instruction Menu**: Provides the best instructions depending on the exercise.
- **Real-Time Connection**: Ensures a real-time connection to Flappy Bird without any output delay.
- **Accurate Exercise Detection**: Uses computer vision to accurately detect and count exercise repetitions.
- **Real-Time Feedback**: Offers immediate feedback on exercise performance to help you improve your form.

## Development and Contributions

- If you wish to contribute to the project, feel free to fork the repository and submit pull requests.
- For any issues or feature requests, please open an issue on the repository.

## Youtube Video Promotion
https://youtu.be/Gxp1On56xcA

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
