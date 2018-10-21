int led = 13;
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
    
    break;
  case 'd':
    digitalWrite(led,LOW);
    
    break;
 }
}
