line='''

'''
deletestr=' '
# s = 'abc'
s = line.translate(str.maketrans('', '', deletestr))
print(s)
# # s = 'ABc'
# s = line.translate(str.maketrans('ab', 'AB', deletestr))
# print(s)