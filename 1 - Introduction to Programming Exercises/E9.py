deposit = float(input('Type the amount of money deposited: '))

first_year = deposit + (deposit *.4)
second_year = first_year + (first_year *.4)
third_year = second_year + (second_year *.4)

print('Savings on the 1st year: %.2f' % (first_year))
print('Savings on the 2nd year: %.2f' % (second_year))
print('Savings on the 3rd year: %.2f' % (third_year))