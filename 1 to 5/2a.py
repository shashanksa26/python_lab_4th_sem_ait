def f(n):
    if n == 0 or n == 1:
        return n
    return f(n-1) + f(n-2)
n = int(input("Enter n: "))
if n > 0:
    r = f(n)
    print(f"fibonacci ={r}")
else:
    print("n = ", n, "Enter n > 0")