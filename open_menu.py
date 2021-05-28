from routine import Routine
from routine import RoutineException
from __init__ import *

class OpenMenu(Routine):
    def execute(self) -> int:
        location = self._clickOn_(menu)
        if (location == None):
            raise RoutineException("Could not find the menu button")
        
        for i in range(Routine()._command_retries_):
            if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(menu_element, confidence=0.9)) != None):
                break
            elif (i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click on the menu button")
            else:
                pyautogui.click(location)
        
        return 0
