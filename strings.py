string = """hai
welcome to python"""

# print(string)


sentence = "This is my dad's car"
# print(len(sentence))


s = "hai \\tha\\nk you"
# print(s)

s = R"hai \tha\nk you"
# print(s)

a = r"\n"
# print(a)


# name = "lily"
# string = f"this flower is {name}"
# print(string)

num = 17823954
list_ = []
count = 0

while num:
    last = num % 10
    num = num // 10
    count -= 1
    list_.insert(0, (last, count))

for item in range(0, len(list_), 2):
    print(list_[item][0])













