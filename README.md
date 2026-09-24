# Face Tracking Servo

A 2D face tracking system using OpenCV, Python, an ESP32, and two servo motors.

## Demo

[![2-Axis Face-Tracking Gimbal Demo](https://img.youtube.com/vi/D_INcjYE7Wk/hqdefault.jpg)](https://youtube.com/shorts/D_INcjYE7Wk)

*Click the thumbnail above to watch the 15-second hardware demonstration on YouTube.*

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
