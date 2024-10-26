digs = [1, -54, 3, 1, 23, 1, 43, -45, 0]

digs.append(100)

print(digs)

digs.insert(3, -50)

print(digs)

digs.remove(23)

print(digs)

d = digs.pop(3)
# pop() без аргумента удалит последнее число списка

print(d)
print(digs)

c = digs.copy()
print(c)

print(digs.count(1))
print(digs.reverse())
