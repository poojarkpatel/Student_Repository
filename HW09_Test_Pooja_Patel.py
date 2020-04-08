import unittest
from Student_Repository_Pooja_Patel.py import Student,Instructor,Repository
from typing import Dict,List

class TestRepository(unittest.TestCase):
    """Helps to test all the functions"""
    def test_student_pretty_table(self):
        """ The function helps to test student_pretty_table function"""

        stevens: Repository = Repository("/Users/poojapatel/python program/stevens")
        expected:Dict = {'10103': {'Name': 'Baldwin, C', 'Courses': ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687']}, 
        '10115': {'Name': 'Wyatt, X', 'Courses': ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687']},
        '10172': {'Name': 'Forbes, I', 'Courses': ['SSW 555', 'SSW 567']}, 
        '10175': {'Name': 'Erickson, D', 'Courses': ['SSW 564', 'SSW 567', 'SSW 687']}, 
        '10183': {'Name': 'Chapman, O', 'Courses': ['SSW 689']}, '11399': {'Name': 'Cordova, I', 'Courses': ['SSW 540']}, 
        '11461': {'Name': 'Wright, U', 'Courses': ['SYS 611', 'SYS 750', 'SYS 800']}, 
        '11658': {'Name': 'Kelly, P', 'Courses': ['SSW 540']}, 
        '11714': {'Name': 'Morton, A', 'Courses': ['SYS 611', 'SYS 645']}, 
        '11788': {'Name': 'Fuller, E', 'Courses': ['SSW 540']}}
        self.assertEqual(stevens.student_pretty_table(),expected)

    def test_instructor_pretty_table(self):
        """ The function helps to test instructor_pretty_table function"""
        stevens: Repository = Repository("/Users/poojapatel/python program/stevens")

        expected:Dict = {'SSW 540': {'cwid': '98765', 'Name': 'Einstein, A', 'Dept': 'SFEN', 'Students': 3}, 
        'CS 545': {'cwid': '98764', 'Name': 'Feynman, R', 'Dept': 'SFEN', 'Students': 1}, 
        'SSW 689': {'cwid': '98763', 'Name': 'Newton, I', 'Dept': 'SFEN', 'Students': 1}, 
        'SYS 645': {'cwid': '98760', 'Name': 'Darwin, C', 'Dept': 'SYEN', 'Students': 1}}

        self.assertEqual(stevens.instructor_pretty_table(),expected)
if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)   