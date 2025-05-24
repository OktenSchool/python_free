numbers = [1, 2, 3, 4, 5]
# print(numbers)
# print(1,2,3,4,5)
# print(numbers[0],numbers[1],numbers[2],numbers[3],numbers[4])

# print(*numbers)
# print(1,2,3,4,5)

# a = [1, 2]
# b = [3, 4]
# # result = [a[0],a[1],b[0],b[1]]
# result = [*b, *a]
# print(result)
# print(len(result))

original_0 = {"a": 10, "b": 20}
original_1 = {"c": 10, "d": 20}
original2 = {**original_0, **original_1}
print(original2)

