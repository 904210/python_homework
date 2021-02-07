def my_func_one(a, b):
    """function exponentiation"""

    print(f'{a} ** {b} = ', a ** b)


def my_func_two(x, y):
    """function exponentiation"""

    result = x
    for _ in range(y - 1):
        result *= x
    print(f'{x} ** {y} = ', result)


help(my_func_one)
numbers_one = [2, 3, 4]
numbers_two = [2, 3, 4]

# static test my_func_one
print('\nstart of the static test my_func_one:')
for i in numbers_one:
    for j in numbers_two:
        my_func_one(i, j)

# static test my_func_two
print('\nstart of the static test my_func_two:')
for i in numbers_one:
    for j in numbers_two:
        my_func_two(i, j)

# manual test my_func_one:
print('\nstart of the manual test my_func_one:')
my_func_one(int(input('input number: ')), int(input('input degree: ')))

# manual test my_func_two:
print('\nstart of the manual test my_func_two:')
my_func_one(int(input('input number: ')), int(input('input degree: ')))
