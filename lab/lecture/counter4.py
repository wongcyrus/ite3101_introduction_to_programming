words = 'the cat sat on the mat'.split()
counts = {}

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

items = list(counts.items())
items.sort()

formatting = '{:3} {:1}'

for (word, number) in items:
    print(formatting.format(word, number))
