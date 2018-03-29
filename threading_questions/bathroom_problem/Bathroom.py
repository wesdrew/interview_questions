from LightSwitch import LightSwitch
import logging
import threading

MALE = 1
FEMALE = 0


class Bathroom:

    def __init__(self):
        self.male_switch = LightSwitch()
        self.female_switch = LightSwitch()

    def enter(self, sex,  cv):
        if sex == MALE:
            self.female_switch.inc(cv)
        elif sex == FEMALE:
            self.male_switch.inc(cv)

    def leave(self, sex, cv):
        if sex == MALE:
            self.female_switch.dec(cv)
        elif sex == FEMALE:
            self.male_switch.dec(cv)

