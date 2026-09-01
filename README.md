# Face Tracking Servo

A one-axis face tracking system using OpenCV, Python, an ESP32, and a servo motor.

## How It Works

The Python program uses OpenCV to detect faces through a webcam. It selects and tracks a face, calculates its horizontal distance from the center of the camera frame, and sends this information to an ESP32 over serial communication.

The ESP32 uses this information to control a servo motor and rotate the camera toward the tracked face.

## Components

- ESP32
- Servo motor
- Webcam
- Computer running Python
- OpenCV

## Software

- Python
- OpenCV
- Arduino / ESP32
- Serial communication

## Progress

The project was developed incrementally:

1. Basic face detection and servo control
2. Stepped servo movement
3. Proportional servo movement
4. Servo dead zone to reduce jitter
5. Face locking to track a specific person