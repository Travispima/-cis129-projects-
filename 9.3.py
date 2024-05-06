#Travis Greenberg
#5/4/2024
#Exercise 9.3
#Program to write student data into a csv file

import csv

#initializes variables and the list 
studentExams = []
keepGoing = 'exit'
firstName = ''

#while loop that prompts the teacher to enter student info. First name, last name, and the three exams
while firstName.lower() != keepGoing:
    firstName = input('First name (enter "exit" to end program): ')
    if firstName.lower() == keepGoing:  #ends loop if exit is entered
        break
    lastName = input('Last name: ')
    exam1 = float(input('Exam 1: '))
    exam2 = float(input('Exam 2: '))
    exam3 = float(input('Exam 3: '))

    studentExams.append([firstName, lastName, exam1, exam2, exam3])  #adds the inputed data into the studentExams list

with open('grades.csv', 'w', newline='') as exams:  #creates a writeable csv file
    writer = csv.writer(exams)
    for record in studentExams:
        writer.writerow(record)  #writes the info from studentExams into the csv file
