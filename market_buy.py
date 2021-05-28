from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class MarketBuy(Routine):
    def __init__(self, times: int):
        self.__times__: int = times

    def execute(self) -> int:
        for i in range(0, self.__times__):
            locations: list = self._disablePauseFor_(
                lambda : list(pyautogui.locateAllOnScreen(market_buy_coin, confidence=0.9902))
            )
            
            if (len(locations) == 0):
                self._clickOn_(market_refresh)
                continue

            # Updates the todos locations accordingly
            locations_todo = []
            for location in locations:
                for i in range(Routine._command_retries_):
                    pyautogui.click(pyautogui.center(location))

                    _locations = self._disablePauseFor_(
                        lambda: list(pyautogui.locateAllOnScreen(market_sold_item, confidence=0.9902))
                    )
                    if (len(_locations) != len(locations_todo)):
                        locations_todo = _locations
                        break
                    elif (i == Routine._command_retries_ - 1):
                        raise RoutineException("Could not click pat button")

            if (i != times - 1):
                self._clickOn_(market_refresh)
        return 0