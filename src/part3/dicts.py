# user_1_name = "Vasya"
# user_1_age = 31
# user_1_status = True

# user_1 = dict(name="Vasya", age = 31, status = True)
# user_1 = {
#     "name": "Vasya",
#     "age":12,
#     "status": True
# }
# print(user_1)
# print(user_1['name'])
# print(user_1['age'])
# 
# if user_1['age'] > 18:
#     print('adult content')
# 
# user_1['age'] = 33
# print(user_1)
# 
# user_1['aka'] = "Doctor"
# print(user_1)


user_2 = {
    "name": "Petya",
    "age": 33,
    "status": True,
    "wife": {
        "name": "Anna",
        "age": 31,
    },
    "main_skill": dict(language="python", exp=12)
}

print(user_2['wife']['name'])
print(user_2['main_skill']['language'])
