
# # # list() #ordered sequence of objects
# amazon_cart = ['notebook', 'sunglasses']
# # Data Structure
# print(amazon_cart[1])


#  Matrix

matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
]
print(matrix[0][1])
matrix.append([9, 10])
print(matrix)
matrix.insert(4, [11, 12])
print(matrix)
matrix.pop(-1)
print(matrix)
matrix.insert(4, [9, 10])
print(matrix)
matrix.clear()
print(matrix)
basket = [3, 12, 56, 12, 1, 56, 7]
print(basket)
# basket.sort()
print(sorted(basket))
print(basket)


# List unpacking

a, b, c, *other, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(other)
print(d)
