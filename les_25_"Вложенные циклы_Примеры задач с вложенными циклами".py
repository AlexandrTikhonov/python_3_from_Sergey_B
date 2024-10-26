# for i in range(1, 4):
#     for j in range(1, 6):
#         # print(i, j, end=' ')
#         print(f"i = {i}, j = {j}", end=' ')
#     print()

# #------------------
# a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
# b = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]]
# c = []
#
# for i, row in enumerate(a):
#     r = []
#     for j, x in enumerate(row):
#         r.append(x + b[i][j])
#
#     c.append(r)
#
# print(c)

# #-------------------------------
# t = ['4545 5454 4545 4554'
#      '4554 5445  4554 5454'
#      '5454  4554  5454 5454'
#      '4545' '4545' '5454' '5454'
#      '4545''4545' '5445' '4545'
#      ]
#
# for i, line in enumerate(t):
#     while line.count('  '):
#         line = line.replace('  ', ' ')
#
#     t[i] = line
#
# print(t)

# #--------------------------------
# n, m = list(map(int, input("Введите n и m: ").split()))
#
# zeros = []
# for i in range(m):
#     zeros.append([0] * n)
#
# print(zeros)
#
# for i in range(m):
#     for j in range(n):
#         zeros[i][j] = 1
#
# print(zeros)

#----------------------------
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for r in A:
    for x in r:
        print(x, end='\t')
    print()
print()

for i in range(len(A)):
    for j in range(i+1, len(A)):
        A[i][j], A[j][i] = A[j][i], A[i][j]

for r in A:
    for x in r:
        print(x, end='\t')
    print()