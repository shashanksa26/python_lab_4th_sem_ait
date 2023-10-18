s = input("Enter s: ")
w=d=u=l = 0
for c in s:
    if c.isspace(): 
        w += 1
    if c.isdigit():
        d += 1
    if c.isupper():
        u += 1
    if c.islower():
        l += 1
print("Words: ", w+1, ", Digits: ", d, ", Upper: ", u, ", Lower:", l)