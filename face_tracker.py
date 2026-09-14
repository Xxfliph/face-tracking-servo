import cv2
import serial
import time
import math



lockedFace = None
lockedFaceFound = False

last_sent = time.time()

ser = serial.Serial("COM3", 115200)

face_classifier = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

video_capture = cv2.VideoCapture(1)


def detect_bounding_box(vid):
    global lockedFace
    global lockedFaceFound

    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)

    faces = face_classifier.detectMultiScale(
        gray_image,
        1.1,
        5,
        minSize=(40, 40)
    )

    if len(faces) == 0:
        return faces

    distance_from_center = 0
    min_distance_from_center = 1000

    lockedx = 0
    lockedy = 0
    lockedw = 0
    lockedh = 0

    if not lockedFaceFound:

        for (x, y, w, h) in faces:
            # x, y is the top-left corner of the face rectangle

            hdistance = x + w / 2 - 320
            vdistance = y + h / 2 - 240

            distance_from_center = math.sqrt(
                hdistance ** 2 + vdistance ** 2
            )

            if distance_from_center < min_distance_from_center:
                min_distance_from_center = distance_from_center

                lockedx = x
                lockedy = y
                lockedw = w
                lockedh = h

                lockedFaceFound = True

        lockedFace = (lockedx, lockedy, lockedw, lockedh)

    else:

        closestFaceDistance = 1000

        for (x, y, w, h) in faces:
            # x, y is the top-left corner of the face rectangle

            midFace = (x + w / 2, y + h / 2)

            midLockedFace = (
                lockedFace[0] + lockedFace[2] / 2,
                lockedFace[1] + lockedFace[3] / 2
            )

            distance_from_lockedFace = math.sqrt(
                (midLockedFace[0] - midFace[0]) ** 2
                + (midLockedFace[1] - midFace[1]) ** 2
            )

            if distance_from_lockedFace < closestFaceDistance:
                closestFaceDistance = distance_from_lockedFace

                lockedx = x
                lockedy = y
                lockedw = w
                lockedh = h

                lockedFaceFound = True

        lockedFace = (lockedx, lockedy, lockedw, lockedh)

    cv2.rectangle(
        vid,
        (lockedFace[0], lockedFace[1]),
        (
            lockedFace[0] + lockedFace[2],
            lockedFace[1] + lockedFace[3]
        ),
        (0, 255, 0),
        4
    )

    move_camera(lockedFace, vid)

    return faces


def move_camera(face, vid):
    global last_sent

    x_difference = (face[0] + face[2] / 2) - (vid.shape[1] / 2)
    y_difference = (face[1] + face[3] / 2) - (vid.shape[0] / 2)

    if time.time() - last_sent >= 0.05:
        print(x_difference)
        print(y_difference)
        print()

        data = f"{x_difference} {y_difference}\n".encode()

        ser.write(data)

        last_sent = time.time()

        # response = ser.readline()
        # print(response)


while True:

    result, video_frame = video_capture.read()

    # print(video_frame.shape)
    # (480, 640, 3) (y, x, channels)

    video_frame = cv2.flip(video_frame, 1)

    if result is False:
        break

    faces = detect_bounding_box(video_frame)

    if len(faces) == 0:
        continue

    cv2.imshow("Video", video_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


video_capture.release()
cv2.destroyAllWindows()
