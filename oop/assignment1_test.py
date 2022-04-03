# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 10:12:02 2021

@author: ergun
"""
# To test your code: 
# 1. put this test file and your your python code in the same directory
# 2. replace assignment1 in the import statement with the name of your code file  


import unittest
import numpy as np
import smooth2 as asm #replace assignment1 with the name of your .py file if you change the name

class TestAssignment(unittest.TestCase):
    x = np.array([2.92, 0.84, 2.69, 2.42, 1.83, 1.22, 0.10, 1.32, 0.56, -0.35])
    output = np.array([np.nan, 2.276     , 1.9418    , 2.09759   , 2.2145045 , 2.15016897, 1.87410876, 1.2467503 , 1.00158683, 0.64973438])
    mape = 272.61
    l_zero = 2
    
    def test_get_name(self):
        name = asm.getName()
        self.assertNotEqual(name, "Lionel Messi", "Please enter your name correctly in getName function")
        
    def test_student_ID(self):
        studentID = asm.getStudentID()
        self.assertNotEqual(studentID, "XXXXXXXXX", "Please enter your student ID correctly in getStudentID function")
        self.assertEqual(len(studentID), 9, "Make sure your student ID is 9 digits!")
   
    def test_output_type(self):
        result = asm.double_exponential_smoothing(self.x, self.l_zero)
        self.assertIsInstance(result, np.ndarray, "The output must be numpy array if mape =False")
        
        result = asm.double_exponential_smoothing(self.x, self.l_zero,mape=True)
        self.assertIsInstance(result, tuple, "The output must be tuple if mape =True")

    def test_same_length(self):
        result = asm.double_exponential_smoothing(self.x, self.l_zero)
        self.assertEqual(len(result), len(self.x) , "The length of x and predictions must be the same")
        
    def test_exceptions(self):
        self.assertRaises(ValueError, asm.double_exponential_smoothing, self.x, self.l_zero, alpha=5)
        self.assertRaises(ValueError, asm.double_exponential_smoothing, self.x, self.l_zero, beta=3)
    
    def test_correct_result(self):
        result = asm.double_exponential_smoothing(self.x, self.l_zero)
        print("Your output: ", result)
        print("Expected output: ", self.output)
        self.assertAlmostEqual(np.nansum(result - self.output), 0, msg= "The forecast results and the expected output do not match")
        
        
        result2 = asm.double_exponential_smoothing(self.x, self.l_zero, mape=True)
        self.assertAlmostEqual(result2[1], self.mape, msg= "Mape is missing or incorrect when mape=True")
        

if __name__ == '__main__':
    unittest.main()

