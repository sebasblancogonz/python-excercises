acre = 4046.85

width = float(input('Write the with of the room (in meters): '))
length = float(input('Write the length of the room (in meters): '))

area = width * length

print('The area is: %.2f acres' % (area/acre))