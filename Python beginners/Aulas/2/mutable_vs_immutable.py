# Mutable data types = lists, dictionaries and sets
# vs
# Immutable data types = can't be changed 

################################################################
# Mutable
#   [0  1  2]
s = [1, 2, 3]
s[1] = 5
print (s) # 1, 5, 3

# Examples
my_list = ['a', 'b', 'c']
your_list = my_list
my_list[1] = 'z' # Changed both lists ['a', 'z', 'c']

################################################################
# Immutable
#   (0  1  2)
t = (1, 2, 3)
t[1] = 5
print (t) # ERROR, value imutable

t = (1, 5, 3) 
print (t) # Set value again