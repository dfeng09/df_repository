from dataclasses import dataclass

class Student:
    student_num = 0#类属性
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        Student.student_num += 1
    
    @classmethod
    def add_students(cls, add_num):
        cls.student_num += add_num
    
    @classmethod
    def from_string(cls, info):
        name, sex = info.split(' ')
        return cls(name, sex)
    
    @staticmethod
    def name_len(name):
        return len(name)
    

    
    