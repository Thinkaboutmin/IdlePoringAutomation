from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class DailySignIn(Routine):
   def execute(self) -> int:
        self._locateClickWhileTesting_(daily_sign_in, 0.9,"daily sign in")
        self._locateClickWhileTesting_(daily_sign_in_btn, 0.99,"daily sign in button")
        self._locateClickWhileTesting_(daily_sign_in_confirm, 0.99,"daily sign in confirm")
        self._locateClickWhileTesting_(leave_daily_sign_in, 0.99, "leave daily sign in")

        return 0