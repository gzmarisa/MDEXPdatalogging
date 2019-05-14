#include <RTClib.h>

#include <Adafruit_MAX31865.h>
#include <SPI.h>
#include <Wire.h>
#include <RTClib.h>

int CS1 = 9;
int CS2 = 8;
int CS3 = 7;
int CS4 = 6;
 
// Use software SPI: CS, DI, DO, CLK
// use hardware SPI, just pass in the CS pin
Adafruit_MAX31865 max_1 = Adafruit_MAX31865(CS1);
Adafruit_MAX31865 max_2 = Adafruit_MAX31865(CS2);
Adafruit_MAX31865 max_3 = Adafruit_MAX31865(CS3);
Adafruit_MAX31865 max_4 = Adafruit_MAX31865(CS4);
RTC_PCF8523 rtc;

char daysOfTheWeek[7][12] = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
char Year, Month, Day, Hour, Minute, Second;
int Temperature1, Temperature2, Temperature3, Temperature4; 

  
// The value of the Rref resistor. Use 430.0!
#define RREF 430.0
 
void setup() {
Serial.begin(115200);
Serial.println("Temperature1,Temperature2,Temperature3,Temperature4,Year,Month,Day,Hour,Minute,Second");
max_1.begin(MAX31865_3WIRE); 
max_2.begin(MAX31865_3WIRE);
max_3.begin(MAX31865_3WIRE);
max_4.begin(MAX31865_3WIRE);
pinMode(CS1, OUTPUT);
pinMode(CS2, OUTPUT);
pinMode(CS3, OUTPUT);
pinMode(CS4, OUTPUT);
SPI.begin();
digitalWrite(CS1, HIGH); 
digitalWrite(CS2, HIGH); 
digitalWrite(CS3, HIGH); 
digitalWrite(CS4, HIGH);
Wire.begin();
while (!Serial) {
delay(1);  
}
rtc.adjust(DateTime(F(__DATE__), F(__TIME__)));
}
 
void loop() {
 
DateTime now = rtc.now();
if(now.second()==0) {
  
  digitalWrite(CS1, LOW); 
  uint16_t rtd1 = max_1.readRTD();
  float ratio1 = rtd1;
  ratio1 /= 32768; 
  Serial.print(max_1.temperature(100, RREF));
  Serial.print(',');
  digitalWrite(CS1, HIGH);
 
  digitalWrite(CS2, LOW);
  uint16_t rtd2 = max_2.readRTD();
  float ratio2 = rtd2;
  ratio2 /= 32768;
  Serial.print(max_2.temperature(100, RREF));
  Serial.print(',');
  digitalWrite(CS2, HIGH);

  digitalWrite(CS3, LOW);
  uint16_t rtd3 = max_3.readRTD();
  float ratio3 = rtd3;
  ratio2 /= 32768; 
  Serial.print(max_3.temperature(100, RREF));
  Serial.print(',');
  digitalWrite(CS3, HIGH);

  digitalWrite(CS4, LOW);
  uint16_t rtd4 = max_4.readRTD();
  float ratio4 = rtd4;
  ratio2 /= 32768;
  Serial.print(max_4.temperature(100, RREF));
  Serial.print(',');
  digitalWrite(CS4, HIGH);

DateTime now = rtc.now();//clock call
    Serial.print(now.year(), DEC);
    Serial.print(',');
    Serial.print(now.month(), DEC);
    Serial.print(',');
    Serial.print(now.day(), DEC);
    Serial.print(",");
    Serial.print(daysOfTheWeek[now.dayOfTheWeek()]);
    Serial.print(",");
    Serial.print(now.hour(), DEC);
    Serial.print(',');
    Serial.print(now.minute(), DEC);
    Serial.print(',');
    Serial.print(now.second(), DEC);
    Serial.println(); 

    delay(3000);
}  
} 



                                                                                                                                                                                                                                                                                                                                                                                                                              

