def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to avoid ZeroDivisionError
    return sum(numbers) / len(numbers)

my_numbers = []
average = calculate_average(my_numbers)
print(f"Average: {average}")  # Output: 0

my_numbers = [10,20,30,40,50]
average = calculate_average(my_numbers)
print(f"Average: {average}") # Output: 30.0