from lecture.exercise20 import file_stats

filename = input('File name? ')
(file_lines, file_words, file_chars) = file_stats(filename)
print(filename, file_lines, file_words, file_chars)
