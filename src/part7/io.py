# f = open('dictionary.txt', 'r', encoding='utf-8')
# print(f)
# 
# for line in f:
#     print(line)
#     
# f.close()

with open('dictionary.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line)