#Travis Greenberg
#Exercise 9.2
#Reads and displays the contents of exercise 9.1
#5/3/2024

#opens the txt file in the read format
with open('grades.txt', 'r') as gradeBook:
    #creates variables
    grades = list(map(float, gradeBook.readlines()))  #reads everying in gradeBook, makes them floats, and converts into a list
    total = sum(grades)  #add all values 
    count = len(grades)  #counts all values
    average = total / count  #calculates average

print(f'Grades')
#prints each item in grades with 2 decimal points
for i in grades:  
    print(f'{i:.2f}')
#Displays total, count, and average with 2 decimal points
print(f'\nTotal: {total:.2f}')
print(f'Count: {count:.2f}')
print(f'Average: {average:.2f}')
