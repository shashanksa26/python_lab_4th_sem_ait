class P:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        s = "{}".format(self.name)
        return s
    def check(self):
        pass
class N(P):
    def __init__(self, n):
        super().__init__("Number")
        self.n = n
    def check(self):
        s = str(self.n)
        r = s[::-1]
        if s == r: return True
class T(P):
    def __init__(self, s):
        super().__init__("String")
        self.s = s
    def check(self):
        r = self.s[::-1]
        if self.s == r: return True
n = N(987)
t = T("sos")
for p in [n, t]:
    if p.check() == True:
        print(p, "is a palindrome")
    else:
        print(p, "is NOT a palindrome")