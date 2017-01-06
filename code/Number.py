# Number
# +, -, * and / is also work like other language
#
# The return type of a division (/) operation depends on its operands.
# If both operands are of type int, floor division is performed and an int is returned.
# If either operand is a float, classic division is performed and a float is returned.
# The // operator is also provided for doing floor division no matter what the operands are.
# The remainder can be calculated with the % operator:

>>> 17 / 3  # int / int -> int
5
>>> 17 / 3.0  # int / float -> float
5.666666666666667
>>> 17 // 3.0  # explicit floor division discards the fractional part
5.0
>>> 17 % 3  # the % operator returns the remainder of the division
2
>>> 5 * 3 + 2  # result * divisor + remainder
17

# With Python, it is possible to use the ** operator to calculate powers [1]:

>>>
>>> 5 ** 2  # 5 squared
25
>>> 2 ** 7  # 2 to the power of 7
128

# In interactive mode, the last printed expression is assigned to the variable _.
# This means that when you are using Python as a desk calculator, it is somewhat easier to continue calculations,

>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
