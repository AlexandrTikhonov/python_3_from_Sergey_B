# a = [(i, j) for i in range(3) for j in range(4)]
# print(a)

# #-----------------
# m, n = 3, 4
# matrix = [[a for a in range(m)] for b in range(n)]
# print(matrix)

# #-------------------
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = [[x ** 2 for x in row] for row in a]
# print(a)

# #---------------------
# a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# a = [[row[i] for row in a] for i in range(len(a[0]))]
# print(a)

#-----------------------
g = [u ** 2 for u in [x +1 for x in range(5)]]
print(g)