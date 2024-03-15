#Travis Greenberg
#Bottle Return Program
#3/13/2024
#Counts bottles returned and amount to be paid out

#initialize variables
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = "y"

while keep_going == "y": #allows the program to loop multiple times
    for counter in range(7): #makes the block itirate 7 times
        counter += 1
        today_bottles = int(input(f'Enter number of bottles for day #{counter}: '))
        total_bottles += today_bottles
        total_payout = total_bottles * .10

    #displays bottles collected and the amount paid out
    print(f'\nThe total number of bottles collected is {total_bottles:,}')
    print(f'The total paid out is ${total_payout:,.2f}')

    #resets variables to their initial values
    counter = 1
    total_bottles = 0
    total_payout = 0

    #asks user if they want to add more data
    keep_going = input('Do you want to enter another week\'s worth of data? (Enter y or n): ')
