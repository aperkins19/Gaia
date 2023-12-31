// pins
int soilMoistureSensorPin = A0; // Analog input pin that the sensor is attached to
int photoResistorPin = A1;

int soilMoistureValue = 0;      // Value read from the sensor
int lightVoltageValue = 0;

bool debugMode = true;

void setup() {
  // pin setup
  pinMode(soilMoistureSensorPin, INPUT);
  pinMode(photoResistorPin, INPUT);
  
   if (debugMode) {
    Serial.begin(9600);         // Start the serial communication    
    }
   
}

void loop() {

    // collect data
    // Read the value from the sensors
    soilMoistureValue = analogRead(soilMoistureSensorPin); 
    lightVoltageValue = analogRead(photoResistorPin);

    // Print the value to the serial monitor
    if (debugMode) {
      Serial.print("Soil Moisture = ");
      Serial.println(soilMoistureValue);
      Serial.println("Light = ");
      Serial.println(lightVoltageValue);

    }


    delay(1000); // Delay in between reads for stability
}
