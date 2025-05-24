# print('asjhdgahgd')
# print(len([11,22,33,44]))


lower_str = "HELLO".lower()
print(lower_str)
str_upper = lower_str.upper()
print(str_upper)

print("   text   ".strip())
print("----asd---".strip("-"))

# print("txteee".find("f"))
# print("txteee".index("f"))

print("hello okten".replace('hello', 'python'))

print("python".startswith('py'))
print("python".endswith('ho'))
print("banana".count("a"))
print("asd".isalnum())
print("123".isdigit())
print("jhfhgf".isalpha())

print("one,two,three".split(","))
split = "vasya-31".split('-')
print(split)
user = dict(name=split[0], age=split[1])
print(user)
