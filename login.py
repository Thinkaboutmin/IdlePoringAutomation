from routine import Routine
from routine import RoutineException
from __init__ import *

class Login(Routine):
    __past_select_char__ = None

    def __init__(self, character_index):
        self.char_index = character_index
        
        # Those two are inverted hence we correct it here when
        # the character index is given
        if (self.char_index == 1):
            self.char_btn = char_btn_1
        elif (self.char_index == 2):
            self.char_btn = char_btn_2
        elif (self.char_index == 3):
            self.char_btn = char_btn_3
        else:
            self.char_btn = char_btn_4

    def execute(self) -> int:
        location = self._disablePauseFor_(
            lambda: pyautogui.locateCenterOnScreen(start, confidence=0.9)
        )
        if (location == None):
            raise RoutineException("Could not find the start button")
        
        for i in range(Routine._command_retries_):
            pyautogui.click(location)
            _location = self._disablePauseFor_(
                lambda: pyautogui.locateCenterOnScreen(start, confidence=0.9)
            )
            if (_location == None):
                break
            elif(i == Routine._command_retries_):
                raise RoutineException("Could not click the start button")
                
        if (self.char_index != Login.__past_select_char__):
            location = self._disablePauseFor_(
                lambda: pyautogui.locateCenterOnScreen(self.char_btn, confidence=0.99)
            )

            if (location == None):
                raise RoutineException("Could not find the character button")

            for i in range(Routine._command_retries_):
                pyautogui.click(location)
                _location = self._disablePauseFor_(
                    lambda: pyautogui.locateCenterOnScreen(self.char_btn, confidence=0.99)
                )
                if (_location == None):
                    break
                elif(i == Routine._command_retries_ - 1):
                    raise RoutineException("Could not find click the character")

        

        location = self._disablePauseFor_(
            lambda: pyautogui.locateCenterOnScreen(login, confidence=0.9)
        )
    
        if (location == None):
            raise RoutineException("Could not find the login button")

        tmp = pyautogui.PAUSE
        for i in range(Routine._command_retries_):
            pyautogui.PAUSE = 30.0
            pyautogui.click(location)
            pyautogui.PAUSE = tmp
            _location = self._disablePauseFor_(
                lambda: pyautogui.locateCenterOnScreen(login, confidence=0.9)
            )
            if (_location == None):
                break
            elif (i == Routine._command_retries_ - 1):
                raise RoutineException("Couldn't click the login button")

        Login.__past_select_char__ = self.char_index
        return 0