#include <ESP32Servo.h>

Servo xmyservo;
Servo ymyservo;

int xservoPin = 18;
int yservoPin = 19;
float xpos = 90;
float ypos = 90;

void setup() {
  Serial.begin(115200);
  ESP32PWM::allocateTimer(0);
  ESP32PWM::allocateTimer(1);
  ESP32PWM::allocateTimer(2);
  ESP32PWM::allocateTimer(3);
  xmyservo.setPeriodHertz(50);
  xmyservo.attach(xservoPin, 500, 2400);
  xmyservo.write(xpos);

  ymyservo.setPeriodHertz(50);
  ymyservo.attach(yservoPin, 500, 2400);
  ymyservo.write(ypos);
}

void loop() {
  if (Serial.available()) {
    String distance_string = Serial.readStringUntil('\n');

    int seperator = distance_string.indexOf(" ");
    float xdistance = distance_string.substring(0, seperator).toFloat();
    float ydistance = distance_string.substring(seperator+1).toFloat();


    float xangle_change = xdistance * 0.025;
    float yangle_change = ydistance * -0.025;

    if (xdistance < 25 && xdistance > -25) {
        xangle_change = 0;
    }
    if (ydistance < 25 && ydistance > -25) {
        yangle_change = 0;
    }

    xpos += xangle_change;
    ypos += yangle_change;
    xpos = constrain(xpos, 0, 180);
    ypos = constrain(ypos, 0, 180);
    xmyservo.write(xpos);
    ymyservo.write(ypos);
  }
}