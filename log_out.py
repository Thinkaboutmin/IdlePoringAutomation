from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class LogOut(Routine):
    def execute(self) -> int:
        location = self._disablePauseFor_(
            lambda: pyautogui.locateCenterOnScreen(logout, confidence=0.99)
        )

        if (location == None):
            raise RoutineException("Could not find the logout button")
        
        for i in range(Routine._command_retries_):
            pyautogui.click(location)
            _location = self._disablePauseFor_(
                lambda: pyautogui.locateCenterOnScreen(confirm_logout, confidence=0.90)
            )
            if (_location != None):
                location = _location
                break
            elif(i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click the logout button")

        for i in range(Routine._command_retries_):
            pyautogui.click(location)
            _location = self._disablePauseFor_(
                lambda: pyautogui.locateOnScreen(confirm_logout, confidence = 0.9)
            )
            if (_location == None):
                break
            elif(i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click the logout confirm button")

        return 0