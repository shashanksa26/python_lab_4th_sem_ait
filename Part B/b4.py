# Lambda function
incr = lambda x: x+1
n = incr(5)
print(n)
# Function with defaults
def f(a, b, c=2):
    a = a*c
    b = b*c
    return (a,b)
r = f(2,3) # default multiplier is 2
print(r)
r = f(2,3, 3)
print(r)
# None is equivalent to undefined.
# Cannot perform any operation
print(None)