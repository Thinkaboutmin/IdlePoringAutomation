from routine import Routine
from routine import RoutineException
from __init__ import *

class SendGift(Routine):
    ICY_ROSE = 0x00

    def __init__(self, gift):
        if (gift == SendGift.ICY_ROSE):
            self.btn = icy_rose

    def execute(self) -> int:
        for i in range(Routine._command_retries_):
            self._clickOn_(self.btn, 0.99)
            location = self._disablePauseFor_(
                lambda: pyautogui.locateOnScreen(self.btn, confidence=0.99)
            )
            if (location == None):
                break
            elif (i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click on gift button")

        return 0