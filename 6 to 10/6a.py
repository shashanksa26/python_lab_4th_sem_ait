filename = input("Enter file name: ")
s = input("Enter no. of lines: ")
n = int(s)
with open(filename, 'r') as file:
    lines = [line for line in file][:n]
for line in lines:
    print(line, end="")
# Word frequency
word = input("Enter word for occurence: ")
counts = dict()
for line in lines:
    words = line.split()
    for w in words:
        if w != word:
            continue
        counts[word] = counts.get(word, 0) + 1
print(counts)