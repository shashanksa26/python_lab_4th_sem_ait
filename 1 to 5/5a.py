import re
def isphonenumber(s):
    r = s.split("-")
    if len(r[0]) != 3 or not r[0].isdigit():
        return False
    if len(r[1]) != 3 or not r[1].isdigit():
        return False
    if len(r[2]) != 4 or not r[2].isdigit():
        return False
    return True
def isphonenumber_re(s):
    regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = regex.search(s)
    return mo != None
# without regular expression
rv = isphonenumber('415-555-4242')
print('1. Phone number found: ', rv)
# with regular expression
rv = isphonenumber_re('My phone number 415-555-4242.')
print('2. Phone number found: ', rv)
