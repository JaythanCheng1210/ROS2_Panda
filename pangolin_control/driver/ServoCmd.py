import sys
import threading
from time import sleep
from Board import setPWMServoPulse

class Servo:
    def __init__(self):
        setPWMServoPulse(1, 1500, 100)
        setPWMServoPulse(2, 1500, 100)
        setPWMServoPulse(3, 1500, 100)
        setPWMServoPulse(4, 1500, 100)
    
    def initial_position(self):
        setPWMServoPulse(1, 1500, 100)
        setPWMServoPulse(2, 1500, 100)
        setPWMServoPulse(3, 1500, 100)
        setPWMServoPulse(4, 1500, 100)

    def forward(self, servo_angle = [40, 40, -40, -40], sleepTime = 1.0, servo_rate = [1.0, 1.0]):
        dedeviation = [-100 ,0, 40, 120]
        setPWMServoPulse(1, int(servo_rate[0]*servo_angle[2]*6.25+1500 + dedeviation[0]), 80)
        sleep(0.0085)
        setPWMServoPulse(2, int(servo_rate[0]*servo_angle[0]*6.25+1500 + dedeviation[2]), 80)
        sleep(0.0085)
        setPWMServoPulse(3, int(servo_rate[1]*servo_angle[3]*6.25+1500 + dedeviation[1]), 80)
        sleep(0.0085)
        setPWMServoPulse(4, int(servo_rate[1]*servo_angle[1]*6.25+1500 + dedeviation[3]), 80)
        sleep(sleepTime)

    def move_joystick(self, linear_x, angular_z):
        self.forward(servo_angle = [20, 0, 0, -20], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

        self.forward(servo_angle = [-38, 0, 0, 38], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

        self.forward(servo_angle = [-40, -40, 40, 40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

        self.forward(servo_angle = [0, -20, 20, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

        self.forward(servo_angle = [0, 38, -38, 0], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

        self.forward(servo_angle = [40, 40, -40, -40], sleepTime=0.08, servo_rate=[linear_x-angular_z, linear_x+angular_z])

    def sit_down(self):
        deviation = [0 ,100, -100, -100]
        setPWMServoPulse(4, int(1500 + deviation[0]), 1000)
        sleep(0.0085)
        setPWMServoPulse(2, int(1500 + deviation[1]), 1000)
        sleep(0.0085)
        setPWMServoPulse(3, int(1500 + deviation[2]), 1000)
        sleep(0.0085)
        setPWMServoPulse(1, int(1500 + deviation[3]), 1000)
        sleep(1)

        setPWMServoPulse(4, int(500 + deviation[0]), 300)
        sleep(0.0085)
        setPWMServoPulse(2, int(2500 + deviation[1]), 300)
        sleep(0.0085)
        setPWMServoPulse(3, int(700 + deviation[2]), 300)
        sleep(0.0085)
        setPWMServoPulse(1, int(2300 + deviation[3]), 300)
        sleep(0.3)

        setPWMServoPulse(4, int(2000 + deviation[0]), 150)
        sleep(0.0085)
        setPWMServoPulse(2, int(1000 + deviation[1]), 150)
        sleep(0.0085)
        setPWMServoPulse(3, int(1000 + deviation[2]), 150)
        sleep(0.0085)
        setPWMServoPulse(1, int(2000 + deviation[3]), 150)
        sleep(0.15)

        setPWMServoPulse(4, int(2000 + deviation[0]), 1000)
        sleep(0.0085)
        setPWMServoPulse(2, int(1000 + deviation[1]), 1000)
        sleep(0.0085)
        setPWMServoPulse(3, int(1400 + deviation[2]), 1000)
        sleep(0.0085)
        setPWMServoPulse(1, int(1600 + deviation[3]), 1000)
        sleep(1)

    def stand_up(self):
        deviation = [0 ,100, -100, -100]
        setPWMServoPulse(4, int(1500 + deviation[0]), 1000)
        sleep(0.0085)
        setPWMServoPulse(2, int(1500 + deviation[1]), 1000)
        sleep(0.0085)
        setPWMServoPulse(3, int(1400 + deviation[2]), 1000)
        sleep(0.0085)
        setPWMServoPulse(1, int(1600 + deviation[3]), 1000)
        sleep(1)

        setPWMServoPulse(4, int(1500 + deviation[0]), 1000)
        sleep(0.0085)
        setPWMServoPulse(2, int(1500 + deviation[1]), 1000)
        sleep(0.0085)
        setPWMServoPulse(3, int(800 + deviation[2]), 1000)
        sleep(0.0085)
        setPWMServoPulse(1, int(2200 + deviation[3]), 1000)
        sleep(1)

        setPWMServoPulse(4, int(1500 + deviation[0]), 1000)
        sleep(0.0085)
        setPWMServoPulse(2, int(1500 + deviation[1]), 1000)
        sleep(0.0085) 
        setPWMServoPulse(3, int(1500 + deviation[2]), 1000)
        sleep(0.0085)   
        setPWMServoPulse(1, int(1500 + deviation[3]), 1000)
        sleep(1)

    def sit_act(self, pSB_Left_Vertical_Axis, pSB_Right_Vertical_Axis):
        deviation = [0 ,100, -30, -50]
        setPWMServoPulse(3, int(1400 + deviation[2]),  100)
        setPWMServoPulse(1, int(1600 + deviation[3]), 100)
        setPWMServoPulse(4, int(pSB_Left_Vertical_Axis*550+1200 + deviation[0]), 100)
        setPWMServoPulse(2, int(pSB_Right_Vertical_Axis*550+1800 + deviation[1]), 100)
        sleep(0.15)