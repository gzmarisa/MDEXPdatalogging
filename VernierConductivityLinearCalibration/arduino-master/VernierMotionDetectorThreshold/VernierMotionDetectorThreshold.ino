/*
VernierMotionDetectorThreshhold (v 2014.09)
Takes data from a Vernier Motion Detector connected to BTD 1 connector.

This sketch measures the time taken for the ultrasound to return (in microseconds)
and then calculates the corresponding distance (based on the speed of ultrasound
in air) and displays the distance (in cm) on the Serial Monitor. 

Here is how the Vernier Motion Detector works:
- when pin 2 on BTD is pulled high the ultrasound pulse is triggered
- the program then starts timing but then delays 0.9 ms *(blanking time,
   0.9 seconds is the time it takes ultrasound to travel 15 cm twice (round trip))
- the program then monitors pin 1 on the BTD, waiting for it to go high. 
This happens when an echo is detected.

As written, the reading will be displayed roughly every quarter of a second. 
Change the delay at the end of the loop to change the rate.

This version turns on an LED connected to pin 13 if the distance is less 
than one meter.

See www.vernier.com/arduino for more information.
 */
const int TriggerPin = 3; //trigger pin
const int EchoPin = 2;// echo pin
const int LedPin = 13;// LED pin

void setup() 
{
  // initialize the Ping pin as an output:
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT); //this is the pin that goes high when an echo is received
  pinMode(LedPin, OUTPUT); //used for the LED
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
  Serial.println("Vernier Format 2");
  Serial.println("Motion Detector Readings taken using Ardunio");
  Serial.println("Data Set");
  Serial.print("Time for Echo");//long name
  Serial.print("\t"); //tab character
  Serial.println ("Distance"); //long name
  Serial.print("delta t");//short name
  Serial.print("\t"); //tab character
  Serial.println ("D"); //short name
  Serial.print("seconds");//units
  Serial.print("\t"); // tab character
  Serial.println ("meters"); //units
}
void loop() 
{
  long time;// clock reading in microseconds
  long Duration; // time it take echo to return
  const float SpeedOfSound = 340; //in m/s
  float Distance;// in centimeters
  int val = 0;digitalWrite(LedPin, LOW);
  digitalWrite(TriggerPin, LOW);
  delayMicroseconds(4000);
  digitalWrite(TriggerPin, HIGH); // start the ultrasound pulse
  time = micros(); //note time
  delayMicroseconds(900); //delay during the blanking time
  do
  {
    val =digitalRead(EchoPin);
    // if no echo, repeat loop and wait
  }
  while (val == LOW) ;
  Duration =micros() - time;
  /* The speed of sound is 340 m/s.
  The ultrasound travels out and back, so to find the distance of the
  object we take half of the distance traveled.*/
  Distance= Duration *SpeedOfSound/2/10000 ;// note convert to cm
  Serial.print(Duration);// print the time it took until the echo
  Serial.print("\t"); // tab character
  Serial.println(Distance);
  if (Distance < 100) 
    {
      // if distance< 1 meter
      digitalWrite(LedPin, HIGH);
      Serial.print(" *******"); 
     }
  delay(250); //delay a quarter of a second
}

 


