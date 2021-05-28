from __init__ import *
from routine import Routine, RoutineException
import pyautogui

class SmeltItems(Routine):
    def execute(self) -> int:
        location = self._clickOn_(smelt_start)

        if (location == None):
            raise RoutineException("Could not find the start smelt button")

        while(self._disablePauseFor_(lambda: pyautogui.locateOnScreen(empty_smelt, confidence=0.9)) == None):
            pyautogui.click(location)

        return 0