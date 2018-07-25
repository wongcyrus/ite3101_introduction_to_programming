text = input('Number? ')
number = float(text)

if number < 1.0:
    lower = number
    upper = 1.0
else:
    lower = 1.0
    upper = number

tolerance = 1.0e-15
uncertainty = upper - lower

while uncertainty > tolerance:
    middle = (lower + upper) / 2

    if middle ** 2 < number:
        lower = middle
    else:
        upper = middle

    print(lower, upper)
    uncertainty = upper - lower
