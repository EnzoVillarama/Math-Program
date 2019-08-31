'''
Lab 2 - Unit Testing
UPI: evil629
Name: Enzo Villarama
'''
from builtins import None

class Logger(object):
    ''' A class for logging information in a program. '''

    def __init__(self, target=None):
        ''' Initialise the logger with a target. If no target is set, it will log to the console. '''
        self._target = self._to_console if target is None else target

    def _to_console(self, text):
        ''' An internal method to log to the console. '''
        print(text)

    def info(self, text):
        ''' Logs an informational message. '''
        self._target('[INFO] ' + text)

    def error(self, text):
        ''' Logs an error message. '''
        self._target('[WARNING] ' + text)        

 
 
class Target():
     
    def __init__(self):
        self.t = None
        
    def set(self, o):
        self.t = o
        
    def get(self):
        return self.t