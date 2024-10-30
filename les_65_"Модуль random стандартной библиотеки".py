import random

# a1 = random.random()
# print(a1)
#
# a2 =  random.uniform(1, 5)
# print(a2)
#
# a3 = random.randint(-5, 5)
# print(a3)
#
# a4 = random.randrange(-3, 10, 1)
# print(a4)
#
# a5 = random.gauss(0, 3.5)
# print(a5)
#
# #--------------------------------------------
# lst = [4, 5, 0, -1, 10, 76, 3]
# b = random.choice(lst)
# print(b)
#
# random.shuffle(lst)
# print(lst)
#
# b2 = random.sample(lst, 3)
# print(b2)

#------------------------------
random.seed(123)
c = [random.randint(0, 10) for i in range(20)]
print(c)