from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class FriendPat(Routine):
   def execute(self) -> int:
        try:
           self._locateClickWhileTesting_(friend_refuse_location, 0.95, "Refuse location")
        except RoutineException:
            pass

        locations =  self._disablePauseFor_(
            lambda: list(pyautogui.locateAllOnScreen(friend_pat, confidence=0.95))
        )

        if (len(locations) == 0):
            raise RoutineException("Could not find any pat buttons")

        # Updates the todos locations accordingly
        locations_todo = locations
        for location in locations:
            for i in range(Routine._command_retries_):
                pyautogui.click(pyautogui.center(location))

                _locations = self._disablePauseFor_(
                    lambda: list(pyautogui.locateAllOnScreen(friend_pat, confidence=0.95))
                )
                if (len(_locations) != len(locations_todo)):
                    locations_todo = _locations
                    break
                elif (i == Routine._command_retries_ - 1):
                    raise RoutineException("Could not click pat button")
        
        start_drag = pyautogui.center(locations[len(locations) - 1])
        end_drag = pyautogui.center(locations[len(locations) - 2])

        for i in range(Routine._command_retries_):
            pyautogui.moveTo(start_drag)
            pyautogui.dragTo(end_drag.x, end_drag.y, 2.0)
            _locations = self._disablePauseFor_(
                lambda: list(pyautogui.locateAllOnScreen(friend_pat, confidence=0.95))
            )
            if (len(_locations) != 0):
                locations = _locations
                break
            elif (i == Routine._command_retries_ - 1):
                raise RoutineException("Could not drag screen up")
            
        for i in range(Routine._command_retries_):
            pyautogui.click(pyautogui.center(locations[0]))
            _locations = self._disablePauseFor_(
                lambda: list(pyautogui.locateAllOnScreen(friend_pat, confidence=0.95))
            )
            if (len(_locations) != len(locations)):
                break
            elif (i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click pat button")

        return 0