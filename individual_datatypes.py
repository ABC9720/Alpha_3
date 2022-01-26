x = 10
# print(x)

# int class constructor
# a = int(20)
# print(a)
#
# print(type(x))
# print(type(a))
# print(dir(x))
# print(dir(a))

# a = 10
# b = 7
#
# print(a // b)
# print(a % b)
#
# print(divmod(a, b))
#
# x = 9
# y = 21
#
# print(abs(x - y))

########################################################

a = 1.256

# print(round(a, 1))

import math
# print(math.trunc(a))

##############################################################
# c = 1 + 2j
# print(c)
#
# c = complex(2+5J)
# print(c)
#
# c = complex(8, 3)
# print(c)

##############################################################

"""         Integers        """

a = 10
# print(float(a))
# print(complex(a))
# print(bool(a))


"""         Float          """

b = 7.65
# print(int(b))
# print(complex(b))
# print(bool(b))


"""         complex         """
c = 5 + 9j

# print(int(c))     # TypeError
# print(float(c))   # TypeError
# print(bool(c))

"""         boolean         """

# default values

# print(bool(0))
# print(bool(0.0))
# print(bool(0j))

# print(int(True))
# print(int(False))
# print(float(True))
# print(float(False))
# print(complex(True))
# print(complex(False))


p = 67

# print(type(p) == int)
# print(type(p) == float)

print(isinstance(p, int))
print(isinstance(10+0j, complex))
print(isinstance(p, (float, complex, bool)))



















