/*
Project 1
Sam Teerlinck
1NMCT4
*/

//Variables
int potpin = 1; //Potentiometer pin (analog)
int val = 0; //to store the Potentiometer value
int randNumber = 0; //to store the random number

void setup()
{
  //set LED pins to output
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(11, OUTPUT);
}

void loop()
{
  randNumber = random(9, 12); //random number (9, 10 or 11)
  val = analogRead(potpin); //read the Potentiometer value and store it
  
  if (val <= 1010) //if the potentiometer is not turned all the way down, start lightshow
  {
    analogWrite(randNumber, 255); //turn one of the LEDs on
    delay(val); //wait
    analogWrite(randNumber, 0); //turn that same LED off
    delay(val); //wait
  }
  else //if the potentiometer is all the way down, turn off all LEDs
  {
    analogWrite(9, 0);
    analogWrite(10, 0);
    analogWrite(11, 0);
  }
} 
