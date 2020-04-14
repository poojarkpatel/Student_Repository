"""
HW10
"""
from typing import Dict, DefaultDict, List,Tuple,Set
from collections import defaultdict
from prettytable import PrettyTable
from HW08_Pooja_Patel import file_reader
import os
import sys

class Student:
    """
    The class stores all the values associated with the student.
    """
    PT_FIELD_NAMES = ['CWID', 'Name', 'Courses','Remaining Required','Remaining Elective','GPA']

    def __init__(self, cwid: str, name: str, major: str, required:list, electives:list) -> None:
        """init function of class student. it initializes values such as cwid,name,major,courses"""
        self._cwid: str = cwid
        self._name: str = name
        self._major: str = major
        self._courses: Dict[str, str] = dict()
        self._required: List[str] = required
        self._electives: List[str] = electives
        self.completed: Set = set()
        self.gpa: float = 0.0
        self.passing_grade:Dict = {'A': 4.0,'A-': 3.75,'B+': 3.25,'B': 3.0,'B-': 2.75,'C+': 2.25,'C': 2.0}
        self.l: List = list()

    def store_course_grade(self, course: str, grade: str) -> None:
        """ this student took course and earned grades"""

        if grade in self.passing_grade.keys():
            self._courses[course] = grade
            self.completed = {course for course,grade in self._courses.items() if grade in self.passing_grade.keys()}
            self.l.append(self.passing_grade[grade])

    def info(self):
        """ returns the info of student"""
        sorted_list: List[str] = sorted(self._courses.keys())
        if len(self.l) != 0:
            self.gpa = sum(self.l) / len(self.l)
        self._required = set(self._required) - set(self.completed)
        if set(self._electives).intersection(self.completed):
            self._electives = set()

        return [self._cwid, self._name, sorted_list,sorted(list(self._required)),sorted(list(self._electives)),round(self.gpa,2)]

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
class Major:
    PT_FIELD_NAMES = ['Major','Required Courses','Electives']

    def __init__(self, major:str):
        """ init function of class major """
        self._major:str = major
        self._required:Set = set()
        self._electives:Set = set()
        self._courses: Dict[str,List] = dict()

    def add_course(self,type:str,course:str):
        """ Add required and elective courses """
        if type == "R":
            self._required.add(course)
        if type == "E":
            self._electives.add(course)

    def info(self):
        """ returns the info of major"""
        self._courses["R"] = list(self._required)
        self._courses["E"] = list(self._electives)
        return list(self._required), list(self._electives)

class Repository:
    """Store all students, instructors for a university and print pretty tables"""

    def __init__(self, path: str) -> None:
        """ init function of class repository"""
        self._path: str = path
        self._students: Dict[str, Student] = dict()
        self._instructors: Dict[str, Instructor] = dict()
        self._inst: Dict[str, Instructor] = dict()
        self._majors: Dict[str, Major] = dict()

        self._read_majors(self._path)
        self._read_students(self._path)
        self._read_instructors(self._path)
        self._read_grades(self._path)

        self.student_pretty_table()
        self.instructor_pretty_table()
        self.majors_pretty_table()

    def _read_majors(self, path: str) -> None:
        """ read student_cwid, course, grade, instructor_cwid """
        try:
            for major, subject_type, course in file_reader(os.path.join(self._path, 'majors.txt'), 3, "\t", True):
                if major not in self._majors.keys():
                    self._majors[major] = Major(major)
                self._majors[major].add_course(subject_type,course)

        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_students(self, path: str) -> None:
        """read each line from path/students.txt and create instance of class student"""
        try:
            for cwid, name, major in file_reader(os.path.join(self._path, 'students.txt'), 3, ";",True):
                required, elective = self._majors[major].info()
                self._students[cwid] = Student(cwid, name, major,required,elective)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_instructors(self, path: str) -> None:
        """read each line from path/instructors.txt and create instance of class student"""
        try:
            for cwid, name, dept in file_reader(os.path.join(self._path, 'instructors.txt'), 3, "|",True):
                self._instructors[cwid] = Instructor(cwid, name, dept)
        except (FileNotFoundError, ValueError) as e:
            print(e)
            sys.exit()

    def _read_grades(self, path: str) -> None:
        """ read student_cwid, course, grade, instructor_cwid """
        try:
            for cwid, major, grade, instructor_cwid in file_reader(os.path.join(self._path, 'grades.txt'), 4, "|",True):

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
        pt = PrettyTable(field_names=Student.PT_FIELD_NAMES)
        for stu in self._students.values():
            pt.add_row(stu.info())
        print(pt)

    def instructor_pretty_table(self) -> None:
        """ print pretty table of instructors """
        d: Dict[str, Dict[str, any]] = dict()
        pt = PrettyTable(field_names=Instructor.PT_FIELD_NAMES)
        for inst in self._instructors.values():
            l: List = inst.info()
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

    def majors_pretty_table(self) :
        """ print pretty table of majors """
        pt = PrettyTable(field_names=Major.PT_FIELD_NAMES)
        l: List = list()
        for major in self._majors:
            required_electives_list = self._majors[major].info()
            pt.add_row([major, required_electives_list[0], required_electives_list[1]])
            l.append([major, sorted(required_electives_list[0]), sorted(required_electives_list[1])])
        return sorted(l)

if __name__ == "__main__":
    """ main function"""
    stevens: Repository = Repository("/Users/poojapatel/PycharmProjects/HW10/stevens")
