from routine import Routine
from routine import RoutineException
from __init__ import *

class SendPresentMenu(Routine):
    def __init__(self, index=0):
        self._index = index

    def execute(self) -> int:
        locations = self._disablePauseFor_(
            lambda: list(pyautogui.locateAllOnScreen(friend_send, confidence=0.92))
        )

        if (len(locations) == 0):
            raise RoutineException("Could not find a single send button")
        
        for i in range(Routine._command_retries_):
            pyautogui.click(pyautogui.center(locations[self._index]))
            _locations = self._disablePauseFor_(
                lambda: list(pyautogui.locateAllOnScreen(friend_send, confidence=0.92))
            )
            if (len(_locations) == 0):
                break
            elif(i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click on send button")
        
        return 0
