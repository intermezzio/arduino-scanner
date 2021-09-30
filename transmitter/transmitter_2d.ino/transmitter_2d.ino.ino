#include<Servo.h>

#define PI 3.14159265358979

int xServoPort = 6;
int yServoPort = 5;
int irPort = A0;


Servo xServo;
Servo yServo;

float irReading = 0;
float xAngle = 0;
float yAngle = 0;
float distance = 0;
float xStart = 60;
float yStart = 90;

float xPos = 0;
float yPos = 0;
float zPos = 0;


float armlength = 3.81;
float disorigin = 1.5875;
float height = 6.6675;
//
// setup function to initialize hardware and software
//
void setup()
{ 
  //
  // start the serial port
  //
  xServo.attach(xServoPort);
  yServo.attach(yServoPort);
  pinMode(irPort, INPUT);

  xServo.write(xStart);
  yServo.write(yStart);
  
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
//  delay(500);
  
//  char buffer[100];
//  sprintf(buffer, "%6f %6f %6f %6f %6f %6f", distance, xAngle, yAngle, xPos, yPos, zPos);
//  Serial.println(buffer);
  
  for(int i=90; i<= 180; i+=5){
    yServo.write(i);
    
    xAngle = xServo.read();
    yAngle = yServo.read();
    
    irReading = analogRead(irPort);

    distance = interpretIrReading(irReading);

    xAngle = xAngle-50; // subtract or add some number of degrees if you find that this is off
    yAngle = yAngle-90; // same here, it's probably not a perfect 90 degrees off
    xPos = (disorigin + distance * cosd(PI/2 - xAngle) - armlength * cosd(xAngle)) * sind(yAngle); // left to right
    yPos = (disorigin + distance * cosd(PI/2 - xAngle) - armlength * cosd(xAngle)) * cosd(yAngle); // forward or backward
    zPos = height + armlength * sind(xAngle) + distance * sind(PI/2 - xAngle);   // up and down

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
    delay(1000);
  }
  
}
