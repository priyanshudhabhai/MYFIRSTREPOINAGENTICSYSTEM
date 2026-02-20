numbers = []

with open("numbers.txt", "r") as file:
    print("File opened successfully")
    for line in file:
        value = line.strip()
        if value:
            numbers.append(int(value))

print(f"Read {len(numbers)} numbers")

total_count = len(numbers)
total_sum = sum(numbers)
average_value = total_sum / total_count if total_count > 0 else 0

with open("results.log", "a") as log_file:
    
    log_file.write("File opened successfully\n")
    log_file.write(f"Read {total_count} numbers\n")
    log_file.write(f"Sum: {total_sum}\n")
    log_file.write(f"Average: {average_value}\n")
    log_file.write("Processing completed\n")
    
    print(f"Sum: {total_sum}")
    print(f"Average: {average_value}")
    print("Processing completed")
