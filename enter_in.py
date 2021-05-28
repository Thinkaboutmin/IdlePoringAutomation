from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class EnterIn(Routine):
    CITY = 0x00
    PET = 0x01

    def __init__(self, place):
        if (place == EnterIn.CITY):
            self.name = "city"
            self.btn = city
            self.btn_selected = city_selected
            self.rec_point = city_maid
        elif (place == EnterIn.PET):
            self.name = "pet"
            self.btn = pet
            self.btn_selected = pet_selected
            self.rec_point = pet_explore
        
    def execute(self) -> int:
        __btn__ = self._clickOn_(self.btn)
        if (__btn__ == None):
            __btn__ = self._clickOn_(self.btn_selected)
            if (__btn__ == None):
                raise RoutineException("Could not find the {0} button".format(self.name))
        for _ in range(Routine._command_retries_):
            if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(self.rec_point, confidence=0.95)) == None):
                pyautogui.click(__btn__)
            else:
                __btn__ = None

        if (__btn__ != None):
            raise RoutineException("Could not click on initial confirm")

        return 0