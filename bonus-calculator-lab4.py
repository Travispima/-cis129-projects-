#Module 4 Lab-4
#Travis Greenberg
#2/22/2024
#This program determines how large store and employee bonuses are

#holds the store bonus amount
storeAmount = int()

#holds the individual bonus amount
empAmount = int()

#holds the percent of increase
salesIncrease = float()

#asks for monthly sales amount
monthlySales = float(input('Enter the monthly sales $'))

#determines the storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0

#gets the percent of increase in sales
salesIncrease = float(input('Enter percent of sales increase: '))
salesIncrease = salesIncrease / 100

#determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

#prints the bonus information
print(f'The store bonus amount is ${storeAmount}')
print(f'The employee bonus amount is ${empAmount}')
if storeAmount == 6000 and empAmount == 75:
    print('\nCongrats! You have reached the highest bonus amounts possible!')
