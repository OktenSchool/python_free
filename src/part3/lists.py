cheks = [123, 234, 35, 456]

books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,

    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "year": 1960,

    }
]
print(books)
print(books[0]['title'])

books.append({
    "title": "1985",
    "author": "George Orwell",
    "year": 1959,

})
print(books)

user_2 = {
    "name": "Petya",
    "age": 33,
    "status": True,
    "wife": {
        "name": "Anna",
        "age": 31,
    },
    "skills": [
        {"lang": 'Python', "exp": 10},
        {"lang": 'Java', "exp": 11},
        {"lang": 'JS', "exp": 13}]
}

user_2_skill = user_2['skills'][2]
print(user_2_skill['lang'])
print(user_2_skill['exp'])

print(books)

