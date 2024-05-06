#Travis Greenberg
#Exercise 9.1
#Makes a text file for entering grades
#5/3/2024

#creates the variables and the list 
grades = []
keepgoing = -1
grade = 0

#while loop for inputing grades
while keepgoing != grade:
    grade = float(input('Enter the student\'s grade(or enter -1 when finished): '))  #promts the user to enter grades
    if grade == keepgoing: #breaks when user enters -1
        break
    elif grade < -1:
        print('Enter a positive number or -1 to exit')
        continue
 
    grades.append(grade)  #adds each grade to the grades list
    
with open('grades.txt', 'w') as gradeBook:  #creates the grades.txt file as writeable
    for grade in grades:
        gradeBook.write(f'{grade}\n')  #writes each grade to a new line
