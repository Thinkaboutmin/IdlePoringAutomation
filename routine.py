import pyautogui

class Routine:
    _command_retries_ = 3

    def execute(self) -> int:
        pass

    def _clickOn_(self, path, confidence = 0.9):
        location = self._disablePauseFor_(
            lambda: pyautogui.locateCenterOnScreen(path, confidence = confidence)
        )

        if (location != None):
            pyautogui.click(location)
            
        return location
    
    def _disablePauseFor_(self, fun) -> any:
        tmp = pyautogui.PAUSE
        pyautogui.PAUSE = 0
        val = fun()
        pyautogui.PAUSE = tmp
        return val

    def _locateClickWhileTesting_(self, path, confidence, name):
        location = self._disablePauseFor_(
            lambda: pyautogui.locateCenterOnScreen(path, confidence=confidence)
        )
        
        if (location == None):
            raise RoutineException("Could not find the " + name)

        tmp = pyautogui.PAUSE
        
        for i in range(Routine._command_retries_):
            pyautogui.click(location)
            
            _location = self._disablePauseFor_(
                lambda: pyautogui.locateCenterOnScreen(path, confidence=confidence)
            )
            
            if(_location == None):
                break
            elif(i == Routine._command_retries_ - 1):
                raise RoutineException("Could not click the " + name)

class RoutineException(Exception):
    pass