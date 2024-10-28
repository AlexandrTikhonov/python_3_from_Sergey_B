a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

b = filter(lambda x: x % 2 == 0, a)

# for x in b:
#     print(x)

lst = list(b)
print(lst)