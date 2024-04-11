const int relayPin = 2; // Pin connected to the relay

void setup() {
  pinMode(relayPin, OUTPUT);
  Serial.begin(9600); // Set the baud rate to match the Python code
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      digitalWrite(relayPin, HIGH); // Turn on relay
    } else if (command == '0') {
      digitalWrite(relayPin, LOW); // Turn off relay
    }
  }
}
