import sys
import string
print("Enter the string with punctuation:")
for line in sys.stdin:
    s = line.translate(str.maketrans('', '', string.punctuation))
    print("String without punctuation:")
    print(s)