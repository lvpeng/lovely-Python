squares = [1, 4, 9, 16, 25]

# Search
# 1.single: indexing returns the item
squares[0]
[1]

squares[-1] #python 特有 , js 返回 undefined
[25]

# 2. multi : search some portion of slicing

>>> squares[2:4] #python
[9, 16]

> squares.slice(2,4) # javascript  api: arr.slice(begin, end) (end is not included)
[9, 16]

>>> squares[:] #all slice return a new list .this meaning a new (shadow) copy of the list
[1, 4, 9, 16, 25]


# Update
# in python , list is mutable type unlike string, i.e. so it's content can change
# this is same as javascript
