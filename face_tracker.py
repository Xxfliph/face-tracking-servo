import cv2
import serial
import time

last_sent = time.time()

ser = serial.Serial("COM3", 115200)


face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(1)

def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40,40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    move_camera(faces, vid)
    return faces

def move_camera(face_position, vid):
    global last_sent
    x_difference = 0
    for (x, y, w, h) in face_position:
        x_difference = (x + w/2) - (vid.shape[1] / 2)
        if time.time() - last_sent >= 0.05:
            print(x_difference)
            data = (str(x_difference) + "\n").encode()
            ser.write(data)
            last_sent = time.time()

while True:
    result, video_frame = video_capture.read()
    video_frame = cv2.flip(video_frame, 1)
    if result is False:
        break
    faces = detect_bounding_box(video_frame)
    cv2.imshow("Video", video_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()