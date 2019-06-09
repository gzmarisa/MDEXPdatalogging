
#include <Adafruit_MAX31865.h>
#include <SPI.h>
//#include <Wire.h>

//int CS1 = 9;
//int CS2 = 8;
//int CS3 = 7;
//int CS4 = 6;

// Changed these to defines to reduce RAM usage
#define CS1 9
#define CS2 8
#define CS3 7
#define CS4 6

// Scaling factors for temp measurement: used for calibration
#define RSCALE1 100.321
#define RSCALE2 100.308
#define RSCALE3 100.308
#define RSCALE4 100.295




// Use software SPI: CS, DI, DO, CLK
// use hardware SPI, just pass in the CS pin
Adafruit_MAX31865 max_1 = Adafruit_MAX31865(CS1);
Adafruit_MAX31865 max_2 = Adafruit_MAX31865(CS2);
Adafruit_MAX31865 max_3 = Adafruit_MAX31865(CS3);
Adafruit_MAX31865 max_4 = Adafruit_MAX31865(CS4);

// The value of the Rref resistor. Use 430.0!
#define RREF 430.0

#define DELIMITER ','

unsigned long millis_old; // Variable for elapsed time counter

void setup() {
  // Establish connection with computer
  Serial.begin(115200);
  // Connect to Temperature Sensors
  max_1.begin(MAX31865_3WIRE);
  max_2.begin(MAX31865_3WIRE);
  max_3.begin(MAX31865_3WIRE);
  max_4.begin(MAX31865_3WIRE);
  // The following 9 lines should be redundant
  pinMode(CS1, OUTPUT);
  pinMode(CS2, OUTPUT);
  pinMode(CS3, OUTPUT);
  pinMode(CS4, OUTPUT);
  SPI.begin();
  digitalWrite(CS1, HIGH);
  digitalWrite(CS2, HIGH);
  digitalWrite(CS3, HIGH);
  digitalWrite(CS4, HIGH);
  //Wire.begin();
  // Don't bother running the program if the serial port doesn't exist.
  while (!Serial) {
    delay(1); // Delay in milliseconds
  }

  millis_old = millis();  // Initialize elapsed time counter
}

void loop() {

  digitalWrite(CS1, LOW);
  Serial.print(max_1.temperature(RSCALE1, RREF));
  Serial.print(DELIMITER);
  digitalWrite(CS1, HIGH);

  digitalWrite(CS2, LOW);
  Serial.print(max_2.temperature(RSCALE2, RREF));
  Serial.print(DELIMITER);
  digitalWrite(CS2, HIGH);

  digitalWrite(CS3, LOW);
  Serial.print(max_3.temperature(RSCALE3, RREF));
  Serial.print(DELIMITER);
  digitalWrite(CS3, HIGH);

  digitalWrite(CS4, LOW);
  Serial.print(max_4.temperature(RSCALE4, RREF));
  digitalWrite(CS4, HIGH);

  Serial.print(DELIMITER);
  Serial.print(millis_old);
  Serial.println();

  while ((millis() - millis_old) < 1000) { // Wait until elapsed time is 1 second
    delay(1);
  }
  millis_old = millis();               // Reset elapsed time
}








