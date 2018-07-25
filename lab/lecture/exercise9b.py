text = input('Number? ')
number = float(text)

if number < 0.0:
    print('Number must be positive!')
    exit()
elif number < 1.0:
    lower = number
    upper = 1.0
else:
    lower = 1.0
    upper = number

text = input('Tolerance? ')
tolerance = float(text)

if tolerance <= 0.0:
    print('Tolerance must be positive!')
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
