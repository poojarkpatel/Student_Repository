""" HW08 implementation file"""
from datetime import datetime, timedelta
from typing import Tuple, List, Iterator, Dict, IO
from prettytable import PrettyTable
import os
import string

def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """The function uses date airthmetic operations and return a tuple"""
    date1:datetime = "Feb 27, 2020"
    date2:datetime = "Feb 27, 2019"
    date3:datetime = "Feb 1, 2019"
    date4:datetime = "Sep 30, 2019"
    dt1:datetime = datetime.strptime(date1,"%b %d, %Y")
    dt2:datetime = datetime.strptime(date2,"%b %d, %Y")
    dt3:datetime = datetime.strptime(date3,"%b %d, %Y")
    dt4:datetime = datetime.strptime(date4,"%b %d, %Y")
    num_days:int = 3
    three_days_after_02272000: datetime = dt1 + timedelta(days=num_days)
    three_days_after_02272017: datetime = dt2 + timedelta(days=num_days)
    days_passed_01012017_10312017: int = dt4 - dt3
    return(three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017.days)

def file_reader(path:str, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    """ The file_reader generator function reads field-separated text files and 
    yield a tuple with all of the values from a single line in the file on each call to next()"""
    try:
        fp:IO = open(path,"r")
    except FileNotFoundError:
        print("File not found")
    else:
        with fp:
            cwid:str = 0
            name:str = ""
            major:str = ""
            count:int = 0
            if header == True:
                count=count+1
                next(fp)
            for line in fp: 
                line1 = line.replace("\n","")
                item = tuple(line1.split(sep))
                count += 1
                try:
                    if len(item) != fields:
                        raise ValueError
                except ValueError:
                    print(f"Value error: {path} has {len(item)} fields on line {count} but expected {fields}")
                else:  
                    yield item
class FileAnalyzer:
    """The FileAnalyzer class 
    that given a directory name, searches that directory 
    for Python files (i.e. files ending with .py)."""
    def __init__(self, directory: str) -> None:
        """ init method of class FileAnalyzer"""
        self.directory:str = os.getcwd()
        self.directory: str = directory 
        self.files_summary: Dict[str, Dict[str, int]] = dict() 
        self.analyze_files() 

    def analyze_files(self) -> None:
        """ calculate a summary of the file including:  
            the file name
            the total number of lines in the file
            the total number of characters in the file
            the number of Python functions 
            the number of Python classes"""
        path:str = os.chdir(self.directory)
        file_list:list = os.listdir(path)
        func_count:int = 0
        class_count:int = 0
        char_count:int = 0
        lines_count:int = 0
        for item in file_list:
            file_name = item
            if item.endswith(".py"):
                try:
                    path1 = os.path.join(self.directory,item)
                    print(path1)
                    fp:IO = open(item,"r")
                except FileNotFoundError:
                    print("File not found")
                else:
                    with fp:
                        for line in fp:
                            lines_count += 1
                            line2 = str(line).strip()
                            if line2.startswith("def ") :
                                func_count += 1
                            elif str(line2).startswith("class "):
                                class_count += 1
                            for item in line:
                                for char in item:
                                    char_count += 1
                        Dict = dict({"lines": lines_count, "classes": class_count, "functions": func_count, "characters": char_count})
                        self.files_summary[file_name] = Dict
                        func_count,class_count,char_count,lines_count= 0,0,0,0
            else:
                continue   
        return self.files_summary
    def pretty_print(self) -> None:
        """ This function prints pretty table"""
        x:PrettyTable = PrettyTable()
        x.field_names:List[str] = ["File Name","Classes","Functions","Lines","Characters"]
        for key, value in self.files_summary.items():
            x.add_row([key,value["classes"],value["functions"],value["lines"],value["characters"]])
        print(x)

if __name__ == "__main__":
    date_arithmetic()
    print(list(file_reader("student_majors.txt",3,sep="|", header=True)))
    file_analyzer:FileAnalyzer = FileAnalyzer("/Users/poojapatel/python program/python")
    file_analyzer.pretty_print()


    

