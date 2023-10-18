line='a.b.c!'
deletestr='.!'
# s = 'abc'
s = line.translate(str.maketrans('', '', '.!'))
print(s)
# s = 'ABc'
s = line.translate(str.maketrans('ab', 'AB', deletestr))
print(s)