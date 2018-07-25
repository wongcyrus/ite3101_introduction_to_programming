numbers = [0, 1, 2, 3, 4, 5]

total = 0
total_so_far = []

for number in numbers:
    total += number
    total_so_far.append(total)

print(total_so_far)
