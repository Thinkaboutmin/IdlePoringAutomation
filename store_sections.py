from routine import Routine
from routine import RoutineException
from __init__ import *
import pyautogui

class StoreSections(Routine):
    SECTION_PET = 0x00

    def __init__(self, section):
        if (section == StoreSections.SECTION_PET):
            self.section = store_pet
            self.section_selected = store_pet_selected

    def execute(self) -> int:
        try:
            self._locateClickWhileTesting_(self.section, 0.99, "section")
        except RoutineException as e:
            locate = self._disablePauseFor_(
                lambda: pyautogui.locateOnScreen(self.section_selected, confidence=0.99)
            )
            if (locate == None):
                raise RoutineException(str(e))

        return 0