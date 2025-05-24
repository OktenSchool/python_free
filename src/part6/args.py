def asd(a, b, *args):
    print(args)
    for item in args:
        print(item)




list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
res = [*list_1, *list_2]
