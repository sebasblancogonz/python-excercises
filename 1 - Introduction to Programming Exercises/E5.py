small, big = .10, .25

small_count = int(input('How many <= 1L containers?: '))
big_count = int(input('How many > 1L containers?: '))

print('Refund for <= 1L containers: %.2f' % (small_count * small))
print('Refund for > 1L containers: %.2f' % (big_count * big))