# Use a file handler to open a file for writing
write_file = open("ch020_t06o_output.txt", "w")

# Open the file for reading
read_file = open("ch020_t06o_output.txt", "r")

# Write to the file
write_file.write("Not closing files is VERY BAD.")

# Try to read from the file
print(read_file.read())
