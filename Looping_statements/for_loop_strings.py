""" 1 to 10 """

# for num in range(1, 11):
#     print(num)


""" 10 to 1 """
# for num in range(10, 0, -1):
#     print(num)


""" -1 to -10 """
# for num in range(-1, -11, -1):
#     print(num)

""" -10 to -1 """
# for num in range(-10, 0):
#     print(num)

""" even numbers  from 1 to 10 """

# for num in range(1, 11):
#     if num % 2 == 0:
#         print(num)

""" traversing through strings """
string = "python"

# for item in range(len(string)):
#     print(string[item], end=" ")
# print()
# for char in string:
#     print(char, end=" ")

""" traversing through lists """
list_ = [10, 20, 30, 40]
#
# for ele in list_:
#     print(ele, end=" ")
#
# print()
#
# for index in range(len(list_)):
#     print(list_[index], end=" ")

""" traversing through sets """
# set_ = {"hai", "hello", "how", "are", "you"}

# for ele in set_:
#     print(ele, end=" ")

""" traversing through dictionaries """
# d = {"one": 1, "two": 2, "three": 3}
#
# for key in d:
#     print(key, d[key], sep="-->")

""" to print index and character in a string """
# s = "hello"

# for item in range(len(s)):
#     print(item, s[item])

# for index, item in enumerate(s):
#     print(index, "-->", item)

""" traversing a string in reversed order """
# string = "hai"

# for item in range(len(string)-1, -1, -1):
#     print(string[item], end=" ")
#
# print()
#
# for char in string[::-1]:
#     print(char, end=" ")
#
# print()
# for item in reversed(string):
#     print(item, end=" ")


""" count the number of characters in a string """
# string = "hello world"

# count = 0
# for _ in string:
#     count += 1

# print(count)

""" print even indexed characters in the string """
# string = "hello world"
#
# for item in range(0, len(string), 2):
#     print(string[item], end=" ")
# print()
# for ele in string[::2]:
#     print(ele, end=" ")

""" print the digits in the string """
s = "hello 123 hai4%978"
count = 0

for char in s:
    if "0" <= char <= "9":  # if char.isdigit():
        count += 1

# print(count)

























