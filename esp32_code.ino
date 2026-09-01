#include <ESP32Servo.h>

Servo myservo;

int servoPin = 18;
int pos = 90;

void setup() {
  Serial.begin(115200);
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  myservo.setPeriodHertz(50);
  myservo.attach(servoPin, 500, 2400);
  myservo.write(pos);
}

void loop() {
  if (Serial.available()) {
    String distance_string = Serial.readStringUntil('\n');
    float distance = distance_string.toFloat();

    if (distance > 50) {
      pos += 1;
    }
    else if (distance < -50) {
      pos -= 1;
    }

    pos = constrain(pos, 0, 180);
    myservo.write(pos);
  }
}