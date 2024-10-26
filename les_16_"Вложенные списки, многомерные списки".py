line = [1, 7, 6, 11, 3]

# img = [[1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3], [1, 7, 6, 11, 3]]

img = [line[:], line[:], line[:], line[:], line[:]]

print(img[0])
print(img[0][1])

img[1] = [0, 0, 0, 0]

print(img)

