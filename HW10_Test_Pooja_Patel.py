import unittest
from HW10_Pooja_Patel import Student,Instructor,Repository
from typing import Dict,List

class TestRepository(unittest.TestCase):
    """Helps to test all the functions"""
    def test_student_pretty_table(self):
        """ The function helps to test student_pretty_table function"""

        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/HW10/stevens")
        expected:List = [['10103', 'Baldwin, C', ['CS 501', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.44],
                        ['10115', 'Wyatt, X', ['CS 545', 'SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], [], 3.81],
                        ['10172', 'Forbes, I', ['SSW 555', 'SSW 567'], ['SSW 540', 'SSW 564'], ['CS 501', 'CS 513', 'CS 545'], 3.88],
                        ['10175', 'Erickson, D', ['SSW 564', 'SSW 567', 'SSW 687'], ['SSW 540', 'SSW 555'], ['CS 501', 'CS 513', 'CS 545'], 3.58],
                        ['10183', 'Chapman, O', ['SSW 689'], ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'], ['CS 501', 'CS 513', 'CS 545'], 4.0],
                        ['11399', 'Cordova, I', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 3.0],
                        ['11461', 'Wright, U', ['SYS 611', 'SYS 750', 'SYS 800'], ['SYS 612', 'SYS 671'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.92],
                        ['11658', 'Kelly, P', [], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 0.0],
                        ['11714', 'Morton, A', ['SYS 611', 'SYS 645'], ['SYS 612', 'SYS 671', 'SYS 800'], ['SSW 540', 'SSW 565', 'SSW 810'], 3.0],
                        ['11788', 'Fuller, E', ['SSW 540'], ['SYS 612', 'SYS 671', 'SYS 800'], [], 4.0]]
        calculated = [student.info() for cwid, student in stevens._students.items()]
        self.assertEqual(calculated,expected)

    def test_instructor_pretty_table(self):
        """ The function helps to test instructor_pretty_table function"""
        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/HW10/stevens")

        expected:Dict = {'SSW 540': {'cwid': '98765', 'Name': 'Einstein, A', 'Dept': 'SFEN', 'Students': 3},
        'CS 545': {'cwid': '98764', 'Name': 'Feynman, R', 'Dept': 'SFEN', 'Students': 1},
        'SSW 689': {'cwid': '98763', 'Name': 'Newton, I', 'Dept': 'SFEN', 'Students': 1},
        'SYS 645': {'cwid': '98760', 'Name': 'Darwin, C', 'Dept': 'SYEN', 'Students': 1}}
        self.assertEqual(stevens.instructor_pretty_table(),expected)

    def test_majors_pretty_table(self):
        """ The function helps to test majors_pretty_table function"""
        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/HW10/stevens")
        expected:List =[['SFEN', ['SSW 540', 'SSW 555', 'SSW 564', 'SSW 567'],
                         ['CS 501', 'CS 513', 'CS 545']],
                        ['SYEN', ['SYS 612', 'SYS 671', 'SYS 800'],
                         ['SSW 540', 'SSW 565', 'SSW 810']]]
        calculated = stevens.majors_pretty_table()
        self.assertEqual(calculated,expected)

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)
