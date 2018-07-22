#define AD5 A5
#define AD4 A4
int Intensity=0;
void setup() {
// put your setup code here, to run once:
Serial.begin(9600);
}
void loop() {
// put your main code here, to run repeatedly:
if(analogRead(AD4)==0)
{
Serial.println(9999);
delay(3000);
}
Intensity =analogRead(AD5)+1000;
Serial.println(Intensity);
  delay(100);

}
