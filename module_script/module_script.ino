// imports
#include <SD.h>
#include <SPI.h>

// Declare 'datafile' globally
File datafile;

String datafileName = "testlog.csv";
String initCSVColumnsLine = "Timestamp, Soil_Moisture_%, Light";

// pins
int soilMoistureSensorPin = A0; // Analog input pin that the sensor is attached to
int photoResistorPin = A1;

// SD card pins
int sdChipSelectPin = 53;

// initialise data values
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

  // setup SD card
  if (!SD.begin(sdChipSelectPin)) {
    if (debugMode) {
      Serial.println("SD card init failed..");
    }
    return;
  }
     
  if (debugMode) {
    Serial.println("SD card init success..");
  }

    
  // init datafile with columns
  if (!SD.exists(datafileName)) {
    // file doesn't exist
    datafile = SD.open(datafileName, FILE_WRITE); // create and open file
      
    if (datafile) {
      // write header
      datafile.println(initCSVColumnsLine);
      datafile.close();
    } else {
      if (debugMode) {
        Serial.println("File can't be written to.");
      }
    }
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
    Serial.print("Light = ");
    Serial.println(lightVoltageValue);
  }

  // Construct CSV data row
  String datarow = String(millis()) + "," + String(soilMoistureValue) + "," + String(lightVoltageValue);

  // write data to sd card
  datafile = SD.open(datafileName, FILE_WRITE); // open file for appending
  if (datafile) {
    // write
    datafile.println(datarow);
    datafile.close();
  } else {
    // file can't be written to
    if (debugMode) {
      Serial.println("Error writing to file.");
    }
  }

  delay(10000); // Delay in between reads for stability
}
