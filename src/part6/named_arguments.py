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


calculator(10, 20, '+')
values_for_calualation_1 = dict(num_1=10, action_str='+', num_2=20)
print(calculator(**values_for_calualation_1))
print(calculator(num_1=10, action_str='+', num_2=20))
