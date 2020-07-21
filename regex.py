import re

pattern = re.compile(r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$")

string = 'search this inside of this text please! Luis'
password = 'Password123@'

# a = pattern.search(string)
# b = pattern.findall(string)
# c = pattern.fullmatch(string)
d = pattern.fullmatch(password)

print(d.group())