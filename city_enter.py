from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class CityEnter(Routine):
    def execute(self) -> int:
        __btn_city__ = self._clickOn_(city)
        if (__btn_city__ == None):
            __btn_city__ = self._clickOn_(city_selected)
            if (__btn_city__ == None):
                raise RoutineException("Could not find the city button")
        
        for _ in range(Routine._command_retries_):
            if (self._disablePauseFor_(
                lambda: pyautogui.locateOnScreen(city_maid) == None)):
                pyautogui.click(__btn_city__)
            else:
                __btn_city__ = None

        if (__btn_city__ != None):
            raise RoutineException("Could not click on initial confirm")

        return 0