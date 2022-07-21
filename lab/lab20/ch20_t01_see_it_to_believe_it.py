import os

file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "inputs/ch20_t01o_output.txt")

my_list = [i ** 2 for i in range(1, 11)]
# Generates a list of squares of the numbers 1 - 10

f = open(file_path_name, "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()
