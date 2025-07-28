# Drowsiness Detection System

This project is a real-time drowsiness detection system that utilizes a webcam to monitor a person's eyes. It analyzes eye blink patterns to determine if the user is active, drowsy, or sleeping, and provides corresponding audible alerts to help prevent accidents caused by fatigue.

## Features
- Real-time video capture and processing from a webcam.
- Face detection using dlib's frontal face detector.
- Facial landmark prediction to accurately locate the eyes.
- Calculation of the Eye Aspect Ratio (EAR) to monitor eye closure.
- Classification of the user's state into 'Active', 'Drowsy', or 'Sleeping'.
- Threaded audio alerts for each state to avoid interrupting the video stream.

## How It Works
The application captures video frames from the default camera. In each frame, it performs the following steps:
1.  **Face Detection:** It uses dlib's built-in face detector to locate faces in the frame.
2.  **Landmark Prediction:** For each detected face, it uses a pre-trained model (`shape_predictor_68_face_landmarks.dat`) to identify 68 specific facial landmarks.
3.  **Eye Aspect Ratio (EAR) Calculation:** It isolates the landmarks corresponding to the eyes and computes the EAR. The EAR is a ratio of distances between the vertical and horizontal eye landmarks. A lower EAR indicates that the eye is closing.
4.  **State Analysis:** The system tracks the EAR over consecutive frames. If the EAR falls below certain thresholds for a sustained period, the user's status is updated to 'Drowsy' or 'Sleeping'.
5.  **Alerts:** When the status changes, a corresponding sound alert is played in a separate thread.

## Prerequisites
- Python 3.x
- A webcam
- The following Python libraries:
  - `opencv-python`
  - `dlib`
  - `numpy`
  - `imutils`
  - `playsound`
- The dlib facial landmark predictor model file.
- Three `.mp3` audio files for the alerts.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/adityaa1205/Drowsiness-Detection-System.git
    cd Drowsiness-Detection-System
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install opencv-python dlib numpy imutils playsound==1.2.2
    ```
    *Note: `playsound` version 1.2.2 is recommended for better stability.*

3.  **Download the facial landmark predictor:**
    Download the `shape_predictor_68_face_landmarks.dat` file. You can get it from the official dlib source [here](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2). Unzip the file and place `shape_predictor_68_face_landmarks.dat` inside the project directory.

4.  **Add audio alert files:**
    Obtain three `.mp3` files for the "active," "drowsy," and "sleeping" states and place them in your project directory or a known location.

5.  **Update File Paths in `main.py`:**
    This is a critical step. Open `main.py` and modify the hardcoded file paths to point to the correct locations of your shape predictor and audio files.

    ```python
    # Update this path
    predictor = dlib.shape_predictor("path/to/your/shape_predictor_68_face_landmarks.dat")

    # ... later in the code ...

    # Update paths to your sound files
    threading.Thread(target=play_sound, args=("path/to/your/sleeping_alert.mp3",)).start()
    # ...
    threading.Thread(target=play_sound, args=("path/to/your/drowsy_alert.mp3",)).start()
    # ...
    threading.Thread(target=play_sound, args=("path/to/your/active_alert.mp3",)).start()
    ```

## Usage

After completing the setup, run the script from your terminal:
```bash
python main.py
```
Two windows will open:
-   **Frame:** The main camera feed with the current status ("Active", "Drowsy !", or "SLEEPING !!!") displayed.
-   **Result of detector:** A copy of the feed with the detected face and all 68 facial landmarks drawn.

To stop the application, press the `ESC` key while one of the video windows is active.
