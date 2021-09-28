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

/** Trig functions
 * Default Arduino trig functions use doubles
 * and radians, so these wrappers
 * allow it to work with floats and degrees
 */
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

  // MARIII
  // right now the xAngle and yAngle assume that
  // x=0 deg and y=90 deg is pointing straight forward
  // x might be close to the truth but y probably isn't
  // test this with the arduino and see if you need to adjust
  // the values
  xAngle = xAngle; // subtract or add some number of degrees if you find that this is off
  yAngle = yAngle - 90; // same here, it's probably not a perfect 90 degrees off
  xPos = distance * cosd(xAngle) * cosd(yAngle); // left to right
  yPos = distance * sind(xAngle) * cosd(yAngle); // forward or backward
  zPos = distance * sind(yAngle);                // up and down

//  char buffer[100];
//  sprintf(buffer, "%6f %6f %6f %6f %6f %6f", distance, xAngle, yAngle, xPos, yPos, zPos);
//  Serial.println(buffer);
  Serial.print(distance);
  Serial.print(" ");
  Serial.print(xAngle);
  Serial.print(" ");
  Serial.print(yAngle);
  Serial.print(" ");
  Serial.print(xPos);
  Serial.print(" ");
  Serial.print(yPos);
  Serial.print(" ");
  Serial.print(zPos);
  Serial.println();
  
}
