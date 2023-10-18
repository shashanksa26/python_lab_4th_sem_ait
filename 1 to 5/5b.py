import re
file = open("5b.txt")
content = file.read()
regex = re.compile(r'\+\d{12}')
print(regex.findall(content))
regex = re.compile(r'[\w]+@gmail\.com')
print(regex.findall(content))