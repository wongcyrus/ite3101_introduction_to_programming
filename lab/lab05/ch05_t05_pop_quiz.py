print('Welcome to the Pig Latin Translator!')

# Start coding here!
original = input("Enter a word:")

if len(original) > 0 and original.isalpha():
    print(original)
else:
    print("empty")
