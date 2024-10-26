# d = [1, 2, 3, 4, 5]

# p = 1
# for x in d:
#     p *= x
#     print(x)
# print(p)

# for i in range(len(d)):
#     print(i + 1)

# #------------------
# for i in "python":
#     print(i)

#-------------------
# S = 1/2 + 1/3 + 1/4 + .... +1/1000

S = 0
for i in range(2,1001):
    S += 1/i

print(S)
