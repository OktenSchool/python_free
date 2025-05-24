# a = 30
# b = 20
#
# if a > b:
#     print(' a is greater than b')
# else:
#     print(' b is greater than a')


color = input('enter some data \n')
is_clear_road = 'yes'

# if color == 'red':
#     if is_clear_road == 'yes':
#         print('go!')
#     else:
#         print('stop')
#
# elif color == 'green':
#     if is_clear_road == 'yes':
#         print('go')
#     else:
#         print('stop')
#
# elif color == 'yellow':
#     print('wait')
# else:
#     print('?????????')


if color == 'red' and is_clear_road == 'yes':
    print('go')
elif color == 'red' and is_clear_road != 'yes':
    print('stop')
elif color == 'green' and is_clear_road == 'yes':
    print('go')
elif color == 'green' and is_clear_road != 'yes':
    print('wait / stop')
elif color == 'yellow' and is_clear_road == 'yes':
    print('go')
else:
    print('?????????')

