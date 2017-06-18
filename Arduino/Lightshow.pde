int potpin = 1;
int ledpin = 11;
int val = 0;
int randNumber = 0;

void setup()
{
  Serial.begin(9600);
  pinMode(ledpin, OUTPUT);
}

void loop()
{
  randNumber = random(9, 12);
  val = analogRead(potpin);
  if (val <= 1010)
  {
    analogWrite(randNumber, 255);
    delay(val);
    analogWrite(randNumber, 0);
    delay(val);
    Serial.println(val);
  }
  else
  {
    analogWrite(9, 0);
    analogWrite(10, 0);
    analogWrite(11, 0);
  }
} 