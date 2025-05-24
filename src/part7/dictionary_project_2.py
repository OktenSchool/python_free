def load_dict_from_file(filename):
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.strip().split('=')
            print(parts)
            if len(parts) == 2:
                eng, ukr = parts
                # eng = parts[0]
                # urk = parts[1]
                result[eng.lower()] = ukr.lower()
    return result


dictionary = load_dict_from_file('dictionary.txt')

while True:

    word = input('Enter eng word \n')

    if word == 'quit' or word == 'exit':
        print('good bye!')
        break

    translation = dictionary.get(word)
    if translation is not None:
        print(translation)
    else:
        print('there is no translation')
