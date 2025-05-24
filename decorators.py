def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


#
# def log_call(func, a, b):
#     def wrapper():
#         result = func(a, b)
#         print(f" call function with name {func.__name__} result={result}")
#         return result
#
#     return wrapper()
#
#
# call1 = log_call(add, 1, 2)
# print(call1)
# call2 = log_call(multiply, 1, 2)
# print(call2)


def log_call(func):

    def wrapper(a,b):
        result = func(a, b)
        print(f" call function with name {func.__name__} result={result}")
        return result

    return wrapper


# add_with_wrapper = log_call(add)
# add_with_wrapper(10,20)

@log_call
def add_new(a,b):
    return a + b

add_new(100,200)






