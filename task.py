#!/usr/bin/env python3

import logging
import json
import statistics as stat
import random


def import_data():
    with open('schools.json') as f:
        schools = json.load(f)
    return schools


def add_student(school_class, student_name):
    new_student = {
        'grades': {key: [] for key in school_class['subjects']},
        'attendance': []
    }
    school_class['students'][student_name] = new_student


def add_grade(school_class, student_name, sub_name, grade):
    try:
        school_class['students'][student_name]['grades'][sub_name].append(
                grade)
    except KeyError as err:
        missed_key = str(err)[1:-1]

        if missed_key == student_name:
            logging.error('Student {} not found'.format(missed_key))

        elif missed_key == sub_name:
            logging.error('Subject {} not present for this student'.format(
                    missed_key))


def register_attendace(school_class, student, value):
    try:
        school_class['students'][student]['attendance'].append(value)
    except KeyError:
        logging.error('Student {} not found'.format(student))


def get_student_average(student):
    grades = student['grades']
    subject_means = [stat.mean(grade) for grade in grades.values()]
    return stat.mean(subject_means)


def get_students_avg_list(school_class):
    students = school_class['students']
    return [get_student_average(student) for student in students.values()]


def get_class_average(school_class):
    return stat.mean(get_students_avg_list(school_class))


def get_school_average(school):
    students_means = []
    for school_class in school.values():
        students_means.extend(get_students_avg_list(school_class))

    return stat.mean(students_means)


def get_student_attendance_percentage(student):
    att = student['attendance']
    print(att)
    return stat.mean(att) * 100


if __name__ == '__main__':
    schools = import_data()

    first_a = schools['first']['1a']

    sample_student_name = 'SampleName SampleSurname'
    add_student(first_a, sample_student_name)
    add_grade(first_a, sample_student_name, 'math', 2.0)
    add_grade(first_a, sample_student_name, 'math', 3.0)
    add_grade(first_a, sample_student_name, 'physics', 4.0)
    add_grade(first_a, sample_student_name, 'history', 5.0)

    add_grade(first_a, sample_student_name, 'now_should_rise', 5.0)

    for _ in range(5):
        attendance = random.choice([True, False])
        register_attendace(first_a, sample_student_name, attendance)

    sample_student = first_a['students'][sample_student_name]

    print('Sample student attendance: {}%'.format(
            get_student_attendance_percentage(sample_student)))
    print('Sample student avg grade: {}'.format(
            get_student_average(sample_student)))
    print('Class avg grade: {}'.format(get_class_average(first_a)))
    print('School avg grade: {}'.format(get_school_average(schools['first'])))
