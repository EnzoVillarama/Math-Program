'''
Lab 2 - Unit Testing
UPI: evil629
Name: Enzo Villarama
'''

import unittest             # Import the Python unit testing framework
import maths                # Our code to test
from email import message   # What do we need this for?


class MathsTest(unittest.TestCase):
    ''' Unit tests for our maths functions. '''
    
    global error_message
    
    error_message = "Test has Failed"
    # Error message for if the test case fails
    # Test case should pass anyway - just extra
    
    
    def test_add(self):
        ''' Tests the add function. '''
        
        # Arrange
        
        test_1 = maths.add(2, 3)
        test_2 = maths.add(5, 7)
        test_3 = maths.add(test_1, test_2)
        
        test_4 = maths.add(5, 3 ,2)
        test_5 = maths.add(5, 5, 16)
        
        # Act
        print('\n Add function \n', '=' * 60, '\n', 
              'Add function - Test 1 result: ', test_1, '\n', 
              'Add function - Test 2 result: ', test_2, '\n',
              'Add function - Test 3 result: ', test_3, '\n',
              'Add function - Test 4 result: ', test_4, '\n',
              'Add function - Test 5 result: ', test_5, '\n',
              '=' * 60, sep = '')
        
        # Assert 
        
        self.assertEqual(test_1, 5, msg = error_message)
        self.assertEqual(test_2, 12, msg = error_message)
        self.assertEqual(test_3, 17, msg = error_message)
        self.assertEqual(test_4, '1000', msg = error_message)
        self.assertEqual(test_5, 'A', msg = error_message)
        
        
    def test_fibonacci(self):
        ''' Tests the fibonacci function. '''
        
        # Arrange
        
        fib = maths.fibonacci(5)
        fib_2 = maths.fibonacci(10)
        
        # Act
        print('\n\n Fibonacci function \n', '=' * 60, '\n',
              'Fibonacci function - Test 1 result: ', fib, '\n',
              'Fibonacci function - Test 2 result: ', fib_2, '\n',
              '=' * 60, sep = '')
                
        # Assert
        
        self.assertEqual(fib, 5, msg = error_message)
        self.assertEqual(fib_2, 55, msg = error_message)
    
    def test_convert_base(self):
        
        # Arrange
        
        hexadecimal = maths.convert_base(10, 16)
        octal = maths.convert_base(10, 8)
        binary = maths.convert_base(10, 2)
        
        # Act
        
        print('\n\n Convert Base function \n', '=' * 60, '\n',
              'Convert Base function - Hexadecimal test result: ', hexadecimal, '\n',
              'Convert Base function - Octal test result: ', octal, '\n', 
              'Convert Base function - Binary test result: ', binary, '\n',
              '=' * 60, sep = '')
        
        # Assert
        
        self.assertEqual(hexadecimal, 'A', msg = error_message)
        self.assertEqual(octal, '12', msg = error_message)
        self.assertEqual(binary, '1010', msg = error_message)
        
        
        def test_factorial(self):
            
            # Arrange
            
            fac_1 = factorial(1)
            fac_3 = factorial(3)
            fac_5 = factorial(5)
 
            # Act
            
            
            # Assert
            
            self.assertEqual(fac_1, 1)
            self.assertEqual(fac_3, 6)
            self.assertEqual(fac_5, 120)
         
        
# This allows running the unit tests from the command line (python test_maths.py)
if __name__ == '__main__':
    unittest.main()
