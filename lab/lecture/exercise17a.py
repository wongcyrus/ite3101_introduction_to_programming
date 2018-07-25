number_as_text = input('Starting number? ')
number = int(number_as_text)

# Open a file called output.txt for writing:
output = open('output.txt', 'w')

while number != 1:
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1

    # Write the number to output, converted to a string.
    output.write(str(number))
    # Explicitly end the line / start a new line
    output.write('\n')
    # print(number)

# Close the output file:
output.close()
