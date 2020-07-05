int sensorValue;

void setup(){

Serial.begin(9600); // sets the serial port to 9600 
} 

void loop(){
  sensorValue = analogRead(A0); // read analog input pin 0

  Serial.print(sensorValue); // prints the value read 
  Serial.print("\n");

delay(1000); // wait 1000ms for next reading 
}
