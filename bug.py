def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    return sum(numbers) / len(numbers)

# Incorrect usage leading to ZeroDivisionError
my_numbers = []
average = calculate_average(my_numbers)
print(f"Average: {average}")

#Correct Usage
my_numbers = [10,20,30,40,50]
average = calculate_average(my_numbers)
print(f"Average: {average}")