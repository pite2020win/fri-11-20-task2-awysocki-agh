#!/usr/bin/env python3

class Student:
    def __init__(self, name, surname):
        self._name = name
        self._surname = surname

    def __str__(self):
        return '{}_{}'.format(self._name, self._surname)

class Class:
    def __init__(self, students):
        self._students = students
        self._grades = {}

        for student in self._students:
            key = str(student)
            self._grades[key] = []

    def get_average_over_class(self):
        pass

    def get_average_for_student(self, key):
        pass    
        

class School:
    def __init__(self):
        self.classes = {}

    def add_class(self, class_name, new_class):
        self.classes[class_name] = new_class


if __name__ == '__main__':    

    students = []
    students.append(Student("Jan", "Kowalski"))
    students.append(Student("Stachu", "Nowak"))

    new_class = Class(students)

    school = School()
    school.add_class('1a', new_class)
