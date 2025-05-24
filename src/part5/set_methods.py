# set_1 = {1, 2, 3}
# # print(set_1)
# # set_1.add(4)
# # set_1.add(5)
# # print(set_1)
# # # set_1.clear()
# # # s = set_1.copy()
# # set_1.remove(3)
# # print(set_1)
# # print(set_1.pop())
# # print(set_1)

union = {11, 22}.union({33, 44})
print(union)

difference = {11, 66, 22, 33, 4, 5}.difference({22, 33})
print(difference)

# a = {1, 2, 3, 4}
# b = {2, 3, 4}
# c = {3, 4, 5}
# 
# intersection = a.intersection(b, c)
# print(intersection)


a = {1, 2, 3}
b = {3, 4, 5}
symmetric_difference = a.symmetric_difference(b)
print(symmetric_difference)

a.update(b)
print(a)
