# Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset = {"Python", "Django", "JavaScript", "SQL"}

print("Before removing the last item:", thisset)

# Convert the set to a list and remove the last item
set_list = list(thisset)
set_list.pop()

# Convert the list back to a set
thisset = set(set_list)

print("After removing the last item:", thisset)
