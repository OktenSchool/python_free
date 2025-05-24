users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
    {"id": 4, "name": "Diana"},
    {"id": 5, "name": "Eve"},
    {"id": 6, "name": "Frank"},
    {"id": 7, "name": "Grace"},
    {"id": 8, "name": "Hank"},
    {"id": 9, "name": "Ivy"},
    {"id": 10, "name": "Jack"}
]

ids = [
    {"id": 1},
    {"id": 2},
    {"id": 3},
    {"id": 4},
    {"id": 5},
    {"id": 6},
    {"id": 7},
    {"id": 8},
    {"id": 9},
    {"id": 10}
]

names_list = [
    {"name": "Alice"},
    {"name": "Bob"},
    {"name": "Charlie"},
    {"name": "Diana"},
    {"name": "Eve"},
    {"name": "Frank"},
    {"name": "Grace"},
    {"name": "Hank"},
    {"name": "Ivy"},
    {"name": "Jack"}
]


def printer(some_list):
    for element in some_list:
        print(element)


# printer(users)
# printer(names_list)

def calculator(num_1, num_2, action_str):
    result = None
    match action_str:
        case "+":
            result = num_1 + num_2
        case "-":
            result = num_1 - num_2
        case "*":
            result = num_1 * num_2
        case "/":
            result = num_1 / num_2
        case _:
            result = 'Error'

    return result


print()

x = calculator(10, 20, '+') / calculator(20, 30, '+')
