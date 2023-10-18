a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
if a <= b and a <= c:
    avg = (b+c)/2
if b <= a and b <= c:
    avg = (a+c)/2
if c <= a and c <= b:
    avg = (a+b)/2
print('avg = ', avg)