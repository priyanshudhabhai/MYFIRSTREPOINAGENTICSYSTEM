balance = int(input("Balance: "))
Withdrawal = int(input("withdrawal: "))
Verified_input = input("Verified (True/False): ").strip()
is_verified = Verified_input.lower() == "true"
if is_verified and Withdrawal <= balance:
    print("Transaction successful")
else:
    print("Transaction denied")    