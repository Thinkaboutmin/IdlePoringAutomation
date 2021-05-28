from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class PetDaily(Routine):
    def execute(self) -> int:
        tmp = pyautogui.PAUSE
        
        for _ in range(3):
            try:
                pyautogui.PAUSE = 10
                self._locateClickWhileTesting_(store_pet_daily_10, 0.99, "daily 10")
                pyautogui.PAUSE = tmp
                try:
                    self._locateClickWhileTesting_(pet_mvp_confirm, 0.99, "daily confirm")
                except Exception:
                    pass

                self._locateClickWhileTesting_(store_pet_confirm, 0.99, "confirm pet")

            except Exception as e:
                pyautogui.PAUSE = tmp
                raise e
        
        for location in self._disablePauseFor_(lambda: pyautogui.locateAllOnScreen(store_pet_daily_free, confidence=0.99)):
            pyautogui.PAUSE = 10
            location = pyautogui.center(location)
            for i in range(Routine._command_retries_):
                pyautogui.click(location)
                try:
                    try:
                        self._locateClickWhileTesting_(pet_mvp_confirm, 0.99, "daily confirm")
                    except Exception:
                        pass
                    self._locateClickWhileTesting_(store_pet_confirm, 0.99, "confirm pet")
                    break
                except RoutineException as e:
                    if (i == Routine._command_retries_ - 1):
                        pyautogui.PAUSE = tmp
                        raise e
                pyautogui.PAUSE = tmp
                    
        pyautogui.PAUSE = tmp

        return 0