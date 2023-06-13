# Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

print("Before adding items:", thisset)

# Add elements from mylist to thisset
thisset.update(mylist)

print("After adding items:", thisset)
