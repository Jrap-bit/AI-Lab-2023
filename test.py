# # May 2021
# fibonacci = [0, 1]
# for i in range(2, 10):
#     fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
#
# index = 0
# for i in range(3, -1, -1):
#     for j in range(i, 4):
#         print(fibonacci[index], end=" ")
#         index += 1
#     print()

# a, b, c, r, tr = 0, 1, 0, 1, 6
#
# print(a)
# print(b, end=" ")
#
# while r < tr:
#     i = 1
#     while i <= r+1:
#         if r == 1 and i == 1:
#             i += 1
#             continue
#         c = a + b
#         print(c, end=" ")
#         a = b
#         b = c
#         i += 1
#     r += 1
#     print()
