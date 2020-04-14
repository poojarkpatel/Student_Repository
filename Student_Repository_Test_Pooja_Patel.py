import unittest
from Student_Repository_Pooja_Patel import Student,Instructor,Repository
from typing import Dict,List

class TestRepository(unittest.TestCase):
    """Helps to test all the functions"""
    def test_student_pretty_table(self):
        """ The function helps to test student_pretty_table function"""

        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/Student_Repository/stevens",
                                         "/Applications/DataGrip.app/Contents/bin/Student_Repository.db")
        expected: List = [['10103', 'Jobs, S', ['CS 501', 'SSW 810'], ['SSW 540', 'SSW 555'], [], 3.38],
                          ['10115', 'Bezos, J', ['SSW 810'], ['SSW 540', 'SSW 555'],  ['CS 501', 'CS 546'], 4.0],
                          ['10183', 'Musk, E', ['SSW 555', 'SSW 810'], ['SSW 540'],['CS 501', 'CS 546'], 4.0],
                          ['11714', 'Gates, B', ['CS 546', 'CS 570', 'SSW 810'], [], [], 3.5]]
        calculated = [student.info() for cwid, student in stevens._students.items()]
        self.assertEqual(calculated, expected)

    def test_instructor_pretty_table(self):
        """ The function helps to test instructor_pretty_table function"""
        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/Student_Repository/stevens",
                                         "/Applications/DataGrip.app/Contents/bin/Student_Repository.db")

        expected: Dict = {'CS 546': {'cwid': '98764', 'Name': 'Cohen, R', 'Dept': 'SFEN', 'Students': 1},
                         'SSW 555': {'cwid': '98763', 'Name': 'Rowland, J', 'Dept': 'SFEN', 'Students': 1},
                         'CS 570': {'cwid': '98762', 'Name': 'Hawking, S', 'Dept': 'CS', 'Students': 1}}
        self.assertEqual(stevens.instructor_pretty_table(), expected)

    def test_majors_pretty_table(self):
        """ The function helps to test majors_pretty_table function"""
        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/Student_Repository/stevens",
                                         "/Applications/DataGrip.app/Contents/bin/Student_Repository.db")
        expected: List =[['CS', ['CS 546', 'CS 570'], ['SSW 565', 'SSW 810']],
                        ['SFEN', ['SSW 540', 'SSW 555', 'SSW 810'], ['CS 501', 'CS 546']]]
        calculated = stevens.majors_pretty_table()
        self.assertEqual(calculated,expected)

    def test_new_student_grades_table_db(self,):
        """The function tests new_student_grades_table_db function"""
        stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/Student_Repository/stevens",
                                         "/Applications/DataGrip.app/Contents/bin/Student_Repository.db")
        expected: List = [('Bezos, J', '10115', 'SSW 810', 'A', 'Rowland, J'),
                          ('Bezos, J', '10115', 'CS 546', 'F', 'Hawking, S'),
                          ('Gates, B', '11714', 'SSW 810', 'B-', 'Rowland, J'),
                          ('Gates, B', '11714', 'CS 546', 'A', 'Cohen, R'),
                          ('Gates, B', '11714', 'CS 570', 'A-', 'Hawking, S'),
                          ('Jobs, S', '10103', 'SSW 810', 'A-', 'Rowland, J'),
                          ('Jobs, S', '10103', 'CS 501', 'B', 'Hawking, S'),
                          ('Musk, E', '10183', 'SSW 555', 'A', 'Rowland, J'),
                          ('Musk, E', '10183', 'SSW 810', 'A', 'Rowland, J')]
        calculated = stevens.new_student_grades_table_db("/Applications/DataGrip.app/Contents/bin/Student_Repository.db")
        self.assertEqual(expected,calculated)

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)
