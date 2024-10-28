from pip._internal import pyproject

file = open('pyproject.toml', encoding='utf-8')

# print(file.read(15))
# print(file.read(5))
# print(file.read(5))

# pos = file.tell()
# print(pos)

#----------------------
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())

# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')

#-----------------------
# for line in file:
#     print(line, end='')

s = file.readlines()
print(s)

file.close()