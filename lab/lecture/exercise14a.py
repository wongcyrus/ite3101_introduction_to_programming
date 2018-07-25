list1 = [0.3, 0.0, 0.4]
list2 = [0.2, 0.5, 0.6]

sum = 0.0

for index in range(len(list1)):
    difference = list1[index] - list2[index]
    sum += difference ** 2

print(sum)
