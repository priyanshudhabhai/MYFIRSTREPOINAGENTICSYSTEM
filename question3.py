name = input("Enter your name: ")
age_input = input("Enter your age: ")
age = int(age_input)
is_active_input = input("Are you an active user? (True/False): ")
is_active = is_active_input == "True"
print(f"User {name} is {age} years old. Active status: {is_active}")
