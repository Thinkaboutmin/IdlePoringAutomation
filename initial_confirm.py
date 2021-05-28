from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class InitialConfirm(Routine):
   def execute(self) -> int:
        __btn_confirm__ = self._clickOn_(initial_confirm)
        if (__btn_confirm__ == None):
            raise RoutineException("Could not find the initial confirm button")
        
        for _ in range(Routine._command_retries_):
            if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(initial_confirm)) != None):
                pyautogui.click(__btn_confirm__)
            else:
                __btn_confirm__ = None

        if (__btn_confirm__ != None):
            raise RoutineException("Could not click on initial confirm")


        if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(initial_confirm, confidence = 0.9)) != None):
            raise RoutineException("Still on confirm page")

        return 0