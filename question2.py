
accuracy_input = input("Enter the accuracy value: ")
if accuracy_input.replace('.', '', 1).isdigit():
accuracy = float(accuracy_input)
print(f"Model accuracy is {accuracy}")
else:
print("Please enter a numeric value.")
