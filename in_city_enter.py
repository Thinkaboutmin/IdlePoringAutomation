from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class InCityEnter(Routine):
    BATTLE = 0x00
    SMELT = 0x01
    FRIEND = 0x02
    STORE = 0x03
    MARKET = 0x04

    def __init__(self, button):
        if (button == InCityEnter.BATTLE):
            self.btn = pvp_enter
        elif (button == InCityEnter.SMELT):
            self.btn = smith        
        elif (button == InCityEnter.FRIEND):
            self.btn = friend
        elif (button == InCityEnter.STORE):
            self.btn = store
        elif (button == InCityEnter.MARKET):
            self.btn = market

    def execute(self) -> int:
        __btn_city__ = self._clickOn_(self.btn)
        if (__btn_city__ == None):
            raise RoutineException("Could not find the in city button")
        
        for _ in range(Routine._command_retries_):
            if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(city_maid)) != None):
                pyautogui.click(__btn_city__)
            else:
                __btn_city__ = None

        if (__btn_city__ != None):
            raise RoutineException("Could not click in city button")

        return 0