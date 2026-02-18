employee_details = (101, "Sandhiya", "Engineering")
employee_roles = {"admin", "editor", "viewer"}

print("Employee ID:", employee_details[0])
print("Employee Name:", employee_details[1])
print("Employee Department:", employee_details[2])

is_admin = "admin" in employee_roles

if is_admin:
    print("Admin Access: Yes")
else:
    print("Admin Access: No")

