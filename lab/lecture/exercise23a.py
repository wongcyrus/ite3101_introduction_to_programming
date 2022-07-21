# Establish a dictionary which translates 'cat', 'dog', and 'mouse' from English into Spanish
en_to_es = {'cat': 'gato', 'dog': 'perro', 'mouse': 'ratón'}

# Establish an empty dictionary to contain translations from Spanish into English:
es_to_en = {}

# Run through the (key, value) pairs in the dictionary en_to_es,
# creating the reversed dictionary.
for (english, spanish) in en_to_es.items():
    es_to_en[spanish] = english

# Print the reversed dictionary
print(es_to_en)
