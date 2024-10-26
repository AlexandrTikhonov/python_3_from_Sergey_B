# a = 12
# b = 7
#
# # if a > b:
# #     res = a
# # else:
# #     res = b
#
# res = a if a > b else b
# print(res)

# #-----------------------
# s = "python"
# t = "upper"
#
# res = s.upper() if t == 'upper' else s
# print(res)

# #-----------------------
# a = 12
# b = 7
#
# # print(1, 2, a if a < b else b, 4, 5)
#
# # print("a - " + ("четное" if a % 2 == 0 else "нечетное") + " число")
#
# print(max(1, 4, 6, a if a > b else b, 5, 8))

#--------------------------
a = 12
b = 5
c = 4

d = (a if  a > c else c) if a > b else (b if b > c else c)

print(d)