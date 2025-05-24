dictionary = {
    "apple": "яблуко",
    "house": "будинок",
    "sun": "сонце",
    "water": "вода",
    "book": "книга"
}

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
