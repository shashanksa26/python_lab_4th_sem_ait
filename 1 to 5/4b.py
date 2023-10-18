roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
s = input("Enter roman n: ").upper()
n = 0
for i in range(len(s)-1,-1,-1):
    m = roman[s[i]]
    if 3*m < n:
        n = n - m
    else:
        n = n + m
print(n)