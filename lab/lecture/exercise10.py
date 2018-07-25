text = input('Number? ')
number = float(text)

text = input('Tolerance? ')
tolerance = float(text)

if number < 0.0:
    print('Number must be positive!')
    exit()
elif number < 1.0:
    lower = number
    upper = 1.0
else:
    lower = 1.0
    upper = number

if tolerance < 5.0e-16:
    print('Tolerance cannot be smaller than 5.0e-16.')
    exit()

uncertainty = upper - lower

while uncertainty > tolerance:
    middle = (lower + upper) / 2

    if middle ** 2 < number:
        lower = middle
    else:
        upper = middle

    print(lower, upper)
    uncertainty = upper - lower
