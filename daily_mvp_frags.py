from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class DailyMvpFrags(Routine):
    def execute(self) -> int:   
        self._locateClickWhileTesting_(pet_grimoire, 0.9,"daily sign in")
        self._locateClickWhileTesting_(pet_mvp_plus, 0.9,"daily sign in button")

        
        # Make really sure that we are getting all three
        for _ in range(6):
            self._clickOn_(pet_mvp_bigger_plus)

        self._locateClickWhileTesting_(pet_mvp_raid, 0.9, "leave daily sign in")
        self._locateClickWhileTesting_(pet_mvp_confirm, 0.9, "leave daily sign in")

        return 0