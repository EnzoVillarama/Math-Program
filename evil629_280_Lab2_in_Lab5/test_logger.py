'''
Lab 2 - Unit Testing
UPI: evil629
Name: Enzo Villarama
'''

import unittest
from logger import Logger, Target


class LoggerTest(unittest.TestCase):
    
    def test_info(self):
    
        # Arrange
        t = Target()
        
        log = Logger(t)
        
        # Act
        
        log.info('Working!')
        
        # Assert
        self.assertEqual(log.info, '[INFO] Working?')
        
    
    
    def test_error(self):
        
        pass
        # Arrange
        
        # Act
        
        # Assert
    
    


def target():
    raise NotImplementedError


if __name__ == '__main__':
    unittest.main()
    
    
