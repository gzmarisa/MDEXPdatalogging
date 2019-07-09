/* VernierTutorialLinearCalibration (v2017)
 * This sketch reads the raw count from a Vernier Analog (BTA) 
 * sensor once every half second, and uses its algebraic slope 
 * and intercept to convert it to standard units.
 * 
 * Plug the sensor into the Analog 2 port on the Vernier Arduino 
 * Interface Shield or into an Analog Protoboard Adapter wired 
 * to Arduino pin A2.
 */

float rawCount; //create global variable for reading from A/D converter (0-1023)
float voltage; //create global variable for voltage (0-5V)
float sensorValue; //create global variable for sensor value
float slope = 960; //create global variable for slope 
float intercept = 0; //create global variable for intercept 
//const char* units = "(MICS)"; //create global variable for units for conductivity sensor 

unsigned long millis_old;
void setup() {
  Serial.begin(115200); //setup communication to display
  //milis_old = millis()
}

void loop() {
  rawCount=analogRead(A2); //read one data value (0-1023)
  voltage=rawCount/1023*5; //convert raw count to voltage (0-5V)
  sensorValue=(slope*voltage)+intercept; //convert to sensor value with linear calibration equation
  Serial.print(sensorValue); //print sensor value 
  Serial.println(" "); //create space
  //Serial.println(units); //print units and skip to next line
   while ((millis() - millis_old) < 1000) { // Wait until elapsed time is 1 second
    delay(1);
  }
  millis_old = millis();               // Reset elapsed time
}
