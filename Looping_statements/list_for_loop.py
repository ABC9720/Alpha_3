# l = ["python", 10, 3.2, "selenium", "Java"]

""" traversing through list """

# for item in l:
#     print(item, end=" ")
#
# print()
#
# for i in range(len(l)):
#     print(l[i], end=" ")


""" print index and its corresponding item in the list """
# l = ["python", 10, 3.2, "selenium", "Java"]

# for i in range(len(l)):
#     print("index is:", i)
#     print("element is:", l[i])


# for index, item in enumerate(l):
#     print(index, item)

""" traversing through a list in reversed order """

# l = ["python", 10, 3.2, "selenium", "Java"]

# # using range
# for i in range(len(l)-1, -1, -1):
#     print(l[i], end=" ")
#
# print()
# # using slicing
# for i in l[::-1]:
#     print(i, end=" ")
#
# print()
# # using reversed()
# for i in reversed(l):
#     print(i, end=" ")

""" print even indexed elements in the list """

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# # using range
#
# for i in range(0, len(l), 2):
#     print(l[i], end=" ")
# print()
#
# # using slicing
# for i in l[::2]:
#     print(i, end=" ")
# print()
#
# # using condition
# for i in range(len(l)):
#     if i % 2 == 0:
#         print(l[i])

""" print integers in a list """

# l = ["python", 10, 3.2, "selenium", "Java"]
#
# for item in l:
#     if isinstance(item, int):
#         print(item)

""" print only numeric datatypes"""

# l = ["python", 10, 3.2, "selenium", "Java"]

# for i in l:
#     if isinstance(i, (int, float, complex)):
#         print(i)

""" print length of each string in the list """

# l = ["python", "Node JS", "selenium", "Java"]

# for item in l:
#     print((item, len(item)))

""" print the strings with even length """

l = ["python", "Node JS", "selenium", "Java"]








