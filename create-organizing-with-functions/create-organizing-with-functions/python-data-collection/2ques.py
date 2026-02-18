contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Sandhiya": "9988776655"
    }

print("All contacts:", contacts)
name = input("Enter a name to search: ")
if name in contacts:
    print(f"phone number:{contacts[name]}")
else:
    print("contact not found")    
              
    