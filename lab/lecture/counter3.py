words = 'the cat sat on the mat'.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

items = list(counts.items())
items.sort()

for (word, number) in items:
    print(word, number)
