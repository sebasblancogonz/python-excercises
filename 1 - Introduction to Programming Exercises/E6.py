meal_price = float(input('Type the cost of the meal: '))
taxes = 0.21 * meal_price
tips = 0.18 * meal_price

print('Cost of the meal (without taxes): %.2f' % (meal_price))
print('Taxes (21%%): %.2f' % (taxes))
print('Tips (18%%): %.2f' % (tips))
print('Total cost of the meal: %.2f' % (meal_price + taxes + tips))