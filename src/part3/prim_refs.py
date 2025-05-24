from copy import deepcopy


# a = 10
# b = a
# b = 100500
#
# print(a)
# print(b)
#
# user = {"name": "vasya"}
# user_2 = user
#
# user_2['age'] = 31
#
# print(user_2)
# print(user)
#
# nums = [1, 2, 3]
# nums_2 = nums
# nums_2.append(4)
# print(nums)


original_1 = {"a": 10, "b": 20, 'bio': {'name': 'vasya'}}
# original_2 = original_1

result = {**original_1}
# print(result == original_1)
# print(result is original_1)
# print(original_1 is original_2)

print(original_1)
print(result)
print(result is original_1)
print(result == original_1)

print(original_1['bio'])
print(result['bio'])

print(result['bio'] == original_1['bio'])
print(result['bio'] is original_1['bio'])



copy = deepcopy(original_1)
print(copy['bio'] is original_1['bio'])
