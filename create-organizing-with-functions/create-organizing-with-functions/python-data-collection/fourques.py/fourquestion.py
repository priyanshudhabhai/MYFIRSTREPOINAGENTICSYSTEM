def calculate_average(user_list):
    averages = []
    for user in user_list:
        avg = sum(user["scores"]) / len(user["scores"])
        averages.append(avg)
    return averages

def check_admin(roles):
    return "admin" in roles

def main():
    users = [
{
"name": "Alice",
"scores": [80, 90, 77.5],
"roles": {"admin", "editor"}
},
{
"name": "Bob",
"scores": [70, 65, 80],
"roles": {"viewer"}
}
]

averages = calculate_average(user)

for i in range(len(users)):
    print(f"Name: {users[i]['name']}")
    print(f"Average Score: {averages[i]}")
    print(f"Admin Access: {check_admin(users[i]['roles'])}")
    print("-" * 20)

main()

