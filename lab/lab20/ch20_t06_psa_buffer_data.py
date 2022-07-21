import os
file_path_name = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), "outputs/ch20_t06o_output.txt")

# Use a file handler to open a file for writing
write_file = open(file_path_name, "w")

# Open the file for reading
read_file = open(file_path_name, "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

# Try to read from the file
print(read_file.read())
