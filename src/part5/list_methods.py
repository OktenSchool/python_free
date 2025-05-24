list_1 = [11, 22, 11, 33, 44, 22]

print(len(list_1))
print(len('ahdahgdsf'))

list_1.append('new value')
print(list_1)
print(list_1.pop())
print(list_1)
print(list_1.count(33))
# print(list_1.remove(11))
# print(list_1)

# while 11 in list_1:
#     list_1.remove(11)
#
# print(list_1)

list_1.insert(0, 'new value')
# print(list_1)

list_1.reverse()
print(list_1)

list_1.sort()
print(list_1)
