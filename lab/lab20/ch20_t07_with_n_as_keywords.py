import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t07o_output.txt")

with open(file_path_name, "w") as textfile:
    textfile.write("Success!")
