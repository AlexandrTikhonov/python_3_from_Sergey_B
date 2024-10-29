# a = [True, True, True, True]          #                     all
#
# b = all(a)
# print(b)

# #-----------------------
# a1 = [True, False, True, True]
#
# b1 = all(a1)
# print(b1)

# #-------------------------
# a = [0, 1, 2.5, 'python', '', [], [1, 2], {}]
#
# b = all(a)
# print(b)  # --> False

# #-------------------------
# a = [1, 2.5, 'python', [1], [1, 2]]
#
# # b = all(a)
# # print(b)  # --> True
#
# all_res = True                                 # <-- если бы не было f-ции all() решение было бы таким
# for x in a:
#     all_res = all_res and bool(x)
#
# print(all_res)

# #=============================================================           any
# a = [False, False, False, False]
#
# b = any(a)
# print(b)

# #-----------------------
# a = [False, True, False, False]
#
# b = any(a)
# print(b)

# #-------------------------
# a = [0, False, [], '', {}]
#
# # b = any(a)
# # print(b)  # --> False
#
# any_res = False                                 # <-- если бы не было f-ции any() решение было бы таким
# for x in a:
#     any_res = any_res or bool(x)
#
# print(any_res)

# #--------------------                    КРЕСТИКИ - НОЛИКИ                   --------------------------
# def true_x(a):
#     return a == 'x'
# P = ['x', 'x', 'o', 'o', 'x', 'o', 'x', 'x', 'x']
#
# row_1 = all(map(true_x, P[:3]))                # сначала было так -->     row_1 = all(map(lambda x: x == 'x', P[:3]))
# row_2 = all(map(true_x, P[3:6]))
# row_3 = all(map(true_x, P[6:]))
#
# col_1 = all(map(true_x, P[::3]))
# col_2 = all(map(true_x, P[1::3]))
# col_3 = all(map(true_x, P[2::3]))
#
#
# print(row_1, row_2, row_3)
# print(col_1, col_2, col_3)
# # print(row_3)
#
# #         ОСТАЛОСЬ ПРОВЕРИТЬ ДИАГОНАЛИ

#----------------------------------            САПЕР        -------------------------------------------
N = 10
P = [0] * (N*N)

P[4] = '*'

loss = any(map(lambda x: x == '*', P))
print(loss)
