import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t09o_output.txt")

with open(file_path_name, "w") as my_file:
    my_file.write("My Data!")
