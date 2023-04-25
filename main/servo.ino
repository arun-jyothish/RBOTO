#include <Servo.h>
Servo myservo;

namespace servo_ns {
	int servo_pin = 9;
}

using namespace servo_ns;
void servo_setup(){
	myservo.attach( servo_pin );
}

void servo_tst(){
	delay(500);
	myservo.write(90);
	delay(500);
	myservo.write(180);
}
