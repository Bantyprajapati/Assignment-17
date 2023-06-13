# Write a python program to add items from another set to the current set. thisset = {"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}
thisset = {"Java", "Python", "SQL"}
secondset = {"C", "Cpp", "NoSQL"}

print("Before adding items:", thisset)

# Add items from secondset to thisset
thisset.update(secondset)

print("After adding items:", thisset)
