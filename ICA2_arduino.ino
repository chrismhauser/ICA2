/*
I am using the Energia IDE and the redbear WiFi Mini
 */

int sensorPin = A1;
int sensorValue = 0;
int mappedValue = 0;

byte i;

// the setup routine runs once when you press reset:
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(57600);

  
}

// the loop routine runs over and over again forever:
void loop() {

  //* for in-class assignment change this to read analog
  //   signal and send on serial port to computer

  sensorValue = analogRead(sensorPin);
  mappedValue = map(sensorValue, 0, 1023, 0, 255);
  
  // print out the value:
  Serial.write(mappedValue);
  
  delay(1);        // delay in between reads for stability
}
