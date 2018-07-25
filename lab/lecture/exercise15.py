foo = [4, 6, 2, 7, 3, 1, 9, 4, 2, 7, 4, 6, 0, 2]
bar = foo[3:12:3]
bar[2] += foo[4]
foo[0] = bar[1]
print(bar)
