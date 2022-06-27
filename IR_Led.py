#Modified by pablord
#Date: 14.06.2022
#Desc: This scrtipt script..

from rpi_hardware_pwm import HardwarePWM

class irLed(object):
    def __init__(self, pwm_channel=0):
        self.pi_pwm = HardwarePWM(pwm_channel, hz=25_000) #create PWM instance with frequency
        self.pi_pwm.start(0) #start PWM of required Duty Cycle 
        self.isOn = False

    def __del__(self):
        self.pi_pwm.stop()


    def toggle(self):
        if self.isOn==True:
            self.pi_pwm.change_duty_cycle(0)
            self.isOn = False
        else:
            self.isOn = True
            self.pi_pwm.change_duty_cycle(75)
            
    def slide(self, value):
            self.pi_pwm.change_duty_cycle(value)
