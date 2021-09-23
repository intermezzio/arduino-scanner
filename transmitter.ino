#include<Servo.h>

#define PI 3.14159265358979

int xServoPort = A0;
int yServoPort = A1;
int irPort = A0;

Servo xServo;
Servo yServo;
float irReading = 0;
float xAngle = 0;
float yAngle = 0;
float distance = 0;

float xPos = 0;
float yPos = 0;
float zPos = 0;

//
// setup function to initialize hardware and software
//
void setup()
{ 
  //
  // start the serial port
  //
//  xServo.attach(xServoPort);
//  yServo.attach(yServoPort);
  pinMode(irPort, INPUT);

//  xServo.write(0);
//  yServo.write(90);
  
  long baudRate = 9600;     // NOTE1: The baudRate for sending & receiving programs must match
  Serial.begin(baudRate);     // NOTE2: Set the baudRate to 115200 for faster communication
}

float sind(float angle) {
  double inputAngle = (double)angle * PI / 180;
  double sinAngle = sin(inputAngle);
  return (float)sinAngle;
}

float cosd(float angle) {
  double inputAngle = (double)angle * PI / 180;
  double cosAngle = cos(inputAngle);
  return (float)cosAngle;
}

float interpretIrReading(float irReading) {
  float distance = 11166.750185583001 / irReading;
  return distance;
}

//
// main loop
//
void loop() 
{  
  delay(500);
  
  xAngle = xServo.read();
  yAngle = yServo.read();

  irReading = analogRead(irPort);

  distance = interpretIrReading(irReading);

  xPos = distance * cosd(xAngle) * cosd(yAngle-90); // left to right
  yPos = distance * sind(xAngle) * cosd(yAngle-90); // forward or backward
  zPos = distance * sind(yAngle-90);                // up and down

//  char buffer[100];
//  sprintf(buffer, "%6f %6f %6f %6f %6f %6f", distance, xAngle, yAngle, xPos, yPos, zPos);
//  Serial.println(buffer);
  Serial.print("Reading:  ");
  Serial.println(irReading);
  Serial.print("Distance: ");
  Serial.println(distance);
  
}
