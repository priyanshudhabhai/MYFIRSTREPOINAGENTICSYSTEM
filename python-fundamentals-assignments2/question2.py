age = int(input("age: "))
has_id_input = input ("Has ID: ").lower()
has_id = has_id_input =="true"
if age >= 18 and has_id:
    print("Entry allowed")