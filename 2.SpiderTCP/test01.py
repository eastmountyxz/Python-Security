import re

pattern = re.compile('east')
match = pattern.match('eastmount!')
print(match.group())

word = re.findall('east', 'east mount')
print(word)
