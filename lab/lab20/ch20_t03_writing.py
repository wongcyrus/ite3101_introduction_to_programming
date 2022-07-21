import os
my_list = [i ** 2 for i in range(1, 11)]

file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t03_output.txt")
my_file = open(file_path_name, "w")

# Add your code below!
