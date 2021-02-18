"""
Exercise 4, question 1
This program is using a few recursive functions to go over the two given lists of grades and teachers and printing
the name of the teacher with a list with all their students' ID numbers, the average and standard deviation.
"""

from statistics import mean, stdev

jctMarks = [[12345, 75, 'English'],
             [23452, 83, 'Physics'],
             [23560, 81, 'Statistics'],
             [23415, 61, 'Computer'],
             [23459, 90, 'Physics'],
             [12345, 75, 'Computer'],
             [23452, 100, 'Statistics']]

teacherName = [['Aharoni', 'English'],
               ['Melamed', 'Physics'],
               ['Kaner', 'Computer'],
               ['Zloti', 'Statistics'],
               ['Korman', 'Philosophy']]


def students(marks, subject):
    return list(map(lambda y: y[0], filter(lambda x: x[2] == subject, marks)))


def grades(marks, subject):
    return list(map(lambda y: y[1], filter(lambda x: x[2] == subject, marks)))


def builtStudentWithStatistics(subject, marks):
    listOfStudents = students(marks, subject)
    listOfGrades = grades(marks, subject)

    if len(listOfGrades) >= 1:
        avg = mean(listOfGrades)
    else:
        avg = 0

    if len(listOfGrades) >= 2:
        std = stdev(listOfGrades)
    else:
        std = 0

    return [listOfStudents, (avg, std)]


def myStudList(marks, names):
    lecturersList = [[l[0], builtStudentWithStatistics(l[1], marks)] for l in names]
    totalListOfGrades = list(map(lambda grd: grd[1], marks))
    totalAvg = mean(totalListOfGrades)
    totalStd = stdev(totalListOfGrades)
    return lecturersList, totalAvg, totalStd


def buildDict(lectWithData):
    lecturersList = [line[0] for line in lectWithData[0]]
    studentsList = [line[1][0] + [line[1][1]] for line in lectWithData[0]]
    return dict(zip(lecturersList, studentsList))


def main():
    dat = buildDict(myStudList(jctMarks, teacherName))
    for lect in dat:
        print(lect, dat[lect][:-1], dat[lect][-1])

main()
