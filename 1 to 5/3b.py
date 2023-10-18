import difflib
s1 = input("Enter s1: ")
s2 = input("Enter s2: ")
rv = difflib.SequenceMatcher(None, s1, s2)
print("Similarity Metric: ", rv.ratio())