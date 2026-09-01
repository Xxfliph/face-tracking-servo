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
    if (distance > 25 && distance <= 100) {
      pos += 1;
    }
    else if (distance > 100 && distance <= 200) {
      pos += 2;
    }
    else if (distance > 200 && distance <= 300) {
      pos += 3;
    }
    else if (distance > 300) {
      pos += 4;
    }
    else if (distance < -25 && distance >= -100) {
      pos -= 1;
    }
    else if (distance < -100 && distance >= -200) {
      pos -= 2;
    }
    else if (distance < -200 && distance >= -300) {
      pos -= 3;
    }
    else if (distance < -300) {
      pos -= 4;
    }
    pos = constrain(pos, 0, 180);
    myservo.write(pos);
  }
}