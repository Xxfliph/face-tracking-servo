# Face Tracking Servo

A 2D face tracking system using OpenCV, Python, an ESP32, and two servo motors.

## How It Works

The Python program uses OpenCV to detect faces through a webcam. It selects and tracks a face, calculates its horizontal and vertical distance from the center of the camera frame, and sends this information to an ESP32 over serial communication.

The ESP32 uses this information to control two servo motors for pan and tilt, allowing the camera to follow the tracked face in two dimensions.

## Components

* ESP32
* 2x servo motors
* Webcam
* Computer running Python
* Pan/tilt camera mount

## Software

* Python
* OpenCV
* Arduino / ESP32
* Serial communication

## Progress

The project was developed incrementally:

1. Basic face detection and servo control
2. Stepped servo movement
3. Proportional servo movement
4. Servo dead zone to reduce jitter
5. Face locking to track a specific person
6. 2D pan and tilt tracking
7. Y-axis tilt direction adjustment
8. Video display and responsiveness improvements
