# Write a python program to delete the set completely.
my_set = {1, 2, 3, 4, 5}

print("Set before deletion:", my_set)

# Delete the set completely
del my_set

# Trying to access the set after deletion will raise a NameError
print("Set after deletion:", my_set)
