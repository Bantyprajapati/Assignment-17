# Write a python program to store your own information {name, age, gender, so on..}
# Create an empty dictionary to store your information
my_information = {}

# Prompt user for information
my_information['name'] = input("Enter your name: ")
my_information['age'] = input("Enter your age: ")
my_information['gender'] = input("Enter your gender: ")
# You can add more fields as per your requirement

# Print the stored information
print("My Information:")
for key, value in my_information.items():
    print(key.capitalize() + ": " + str(value))
