from routine import *
from __init__ import *
import pyautogui

class Battle(Routine):
    __battle_index__ = 0    

    def execute(self) -> int:
        if (self._disablePauseFor_(lambda: pyautogui.locateOnScreen(no_pvp, confidence=0.99)) != None and 
            len(self._disablePauseFor_(lambda: list(pyautogui.locateAllOnScreen(pvp_challenge, confidence = 0.9)))) == 0):
            return 1

        __btn_start__ = self._clickOn_(pvp)
        if (__btn_start__ == None):
            if (len(list(self._disablePauseFor_(lambda: pyautogui.locateAllOnScreen(pvp_challenge, confidence = 0.9)))) == 0):
                raise RoutineException("Could not find the button to start fight")
        else:
            Battle.__battle_index__ = 0

            if (__btn_start__ != None):
                # Tries x times to challenge
                for _ in range(Routine._command_retries_):
                    try:
                        self.__clickOnBtnChallenge__()
                        __btn_start__ = None
                        break
                    except RoutineException:
                        pyautogui.click(__btn_start__)

                if (__btn_start__ != None):
                    raise RoutineException("Could not enter the battle")

        for i in range(Routine._command_retries_):
            # Checks if we left the challenge menu
            try:
                self.__clickOnBtnChallenge__()
            except RoutineException:
                break

            if (i == Routine._command_retries_ - 1):
                    raise RoutineException("Could not challenge player")

        # Go to next challenge
        if (Battle.__battle_index__):
            Battle.__battle_index__ = 0
        else:
            Battle.__battle_index__ = 1

        return 0

    def __clickOnBtnChallenge__(self):
        # There's more than on challenge button.
        locations = self._disablePauseFor_(lambda: tuple(pyautogui.locateAllOnScreen(pvp_challenge, confidence=0.9)))

        if (len(locations) != 2):
            raise RoutineException("Could not find all challenge buttons")

        location = locations[self.__battle_index__]
        pyautogui.click(location)

        return location