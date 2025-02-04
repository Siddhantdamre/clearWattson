#define SensorPin A0  // Pin connected to pH sensor
#define Offset 0.00   // Calibration offset for the pH sensor (adjust after calibration)
#define SamplingInterval 20  // Time between measurements in milliseconds
#define ArrayLength 40  // Number of readings to average

int pHArray[ArrayLength];   // Store readings from the sensor
int pHArrayIndex = 0;

void setup() {
  Serial.begin(9600);  // Start the serial communication
  pinMode(SensorPin, INPUT);
}

void loop() {
  static unsigned long samplingTime = millis();
  if (millis() - samplingTime > SamplingInterval) {
    samplingTime = millis();
    pHArray[pHArrayIndex++] = analogRead(SensorPin);  // Read sensor value
    if (pHArrayIndex == ArrayLength) pHArrayIndex = 0;  // Reset index
    float voltage = averageAnalogRead() * 5.0 / 1024;   // Convert analog reading to voltage
    float pHValue = 3.5 * voltage + Offset;  // Conversion formula for pH value

    Serial.print("pH Value: ");
    Serial.println(pHValue);
  }

  delay(1000);  // Delay for readability
}

// Function to average sensor readings
int averageAnalogRead() {
  int sum = 0;
  for (int i = 0; i < ArrayLength; i++) {
    sum += pHArray[i];
  }
  return sum / ArrayLength;
}
