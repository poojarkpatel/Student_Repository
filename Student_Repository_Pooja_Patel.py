"""
HW09
"""
from typing import Dict, DefaultDict, List
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Pooja_Patel import file_reader
import os
import sys


class Student:
    """
    The class stores all the values associated with the student.
    """
    PT_FIELD_NAMES = ['CWID', 'Name', 'Courses']

    def __init__(self, cwid: str, name: str, major: str) -> None:
        """init function of class student. it initializes values such as cwid,name,major,courses"""
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()

    def store_course_grade(self, course: str, grade: str) -> None:
        """ this student took course and earned grades"""
        self._courses[course] = grade

    def info(self):
        """ returns the info of student"""
        sorted_list: List[str] = sorted(self._courses.keys())
        return [self._cwid, self._name, sorted_list]

    def __str__(self):
        return self._cwid


class Instructor:
    PT_FIELD_NAMES = ['CWID', 'Name', 'Dept', 'Course', 'Students']

    def __init__(self, cwid: str, name: str, dept: str) -> None:
        """ init function of class instructor"""
        self._cwid: str = cwid
        self._name: str = name
        self._dept: str = dept
        self._courses: DefaultDict[str, int] = defaultdict(int)

    def store_course_student(self, course: str):
        """ stores total number of students associated with the course."""
        self._courses[course] += 1

    def info(self):
        """ returns the info of instructor"""
        return [self._cwid, self._name, self._dept, self._courses]


class Repository:
    """Store all students, instructors for a university and print pretty tables"""

    def __init__(self, path: str) -> None:
        """ init function of class repository"""
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._inst: Dict[str, Instructor] = dict()

        self._read_students(self._path)
        self._read_instructors(self._path)
        self._read_grades(self._path)

        self.student_pretty_table()
        self.instructor_pretty_table()

    def _read_students(self, path: str) -> None:
        """read each line from path/students.txt and create instance of class student"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._path, 'students.txt'), 3, "\t"):
                self._students[cwid] = Student(cwid, name, major)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_instructors(self, path: str) -> None:
        """read each line from path/instructors.txt and create instance of class student"""
        try:
            for cwid, name, dept in file_reader(os.path.join(self._path, 'instructors.txt'), 3, "\t"):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_grades(self, path: str) -> None:
        """ read student_cwid, course, grade, instructor_cwid """
        try:
            for cwid, major, grade, instructor_cwid in file_reader(os.path.join(self._path, 'grades.txt'), 4, "\t"):

                if cwid not in self._students.keys():
                    print(f"{cwid}is Unknown cwid. No such student found")
                else:
                    s: Student = self._students[cwid]
                    s.store_course_grade(major, grade)
                if instructor_cwid not in self._instructors.keys():
                    print(f"{instructor_cwid}is Unknown cwid. No such instructor found")
                else:
                    inst: Instructor = self._instructors[instructor_cwid]
                    inst.store_course_student(major)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def student_pretty_table(self):
        """ print pretty table of students"""
        d: Dict[str, Dict[str, any]] = dict()
        pt = PrettyTable(field_names=Student.PT_FIELD_NAMES)
        for stu in self._students.values():
            pt.add_row(stu.info())
            l = stu.info()
            d1: Dict[str, any] = {"Name": "", "Courses": []}
            d1["Name"] = l[1]
            d1["Courses"] = l[2]
            d[l[0]] = d1
        print(pt)
        return d

    def instructor_pretty_table(self) -> None:
        """ print pretty table of instructors"""
        d: Dict[str, Dict[str, any]] = dict()
        pt = PrettyTable(field_names=Instructor.PT_FIELD_NAMES)
        for inst in self._instructors.values():
            l = inst.info()
            for i in l[3].items():
                pt.add_row([l[0], l[1], l[2], i[0], i[1]])
                d1: Dict[str, str] = {"cwid": "", "Name": "", "Dept": "", "Students": ""}
                d1["cwid"] = l[0]
                d1["Name"] = l[1]
                d1["Dept"] = l[2]
                d1["Students"] = i[1]
            d[i[0]] = d1
        print(pt)
        return d


if __name__ == "__main__":
    """ main function"""
    stevens: Repository = Repository("/Users/poojapatel/python program/stevens")
