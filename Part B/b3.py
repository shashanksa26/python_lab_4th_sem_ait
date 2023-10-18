s = input("Enter score: ")
score = float(s)
if 0.0 <= score <= 1.0:
    if score < 0.6:
        g = 'F'
    elif 0.6 <= score < 0.7:
        g = 'D'
    elif 0.7 <= score < 0.8:
        g = 'C'
    elif 0.8 <= score < 0.9:
        g = 'B'
    else:
        g = 'A'
    print("Grade =", g)
else:
    print("Input Error.")