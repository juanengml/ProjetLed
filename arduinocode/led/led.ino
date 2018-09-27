int led = 2;
char letra;
  
void setup() {
  // put your setup code here, to run once:
  pinMode(led,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
 letra = Serial.read();
 switch(letra){
  case 'l':
    digitalWrite(led,HIGH);
    Serial.println("pin 13 ON");
    break;
  case 'd':
    digitalWrite(led,LOW);
    Serial.println("pin 13 OFF");
    break;
 }
}
