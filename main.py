def get_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))

            if value > 0:
                return value

            print("Please enter a number greater than zero.") 
        except ValueError:
            print("Please enter a valid number.")

print("Shift Earnings Tracker")
print()

date = input("Enter the shift date: ")
job = input("Enter the job name: ")
hours = get_positive_number("Enter the hours worked: ")
earnings = get_positive_number("Enter the amount earned: $")
hourly_rate = earnings / hours

print()
print("Shift Summary")
print(f"Date: {date}")
print(f"Job: {job}")
print(f"Hours worked: {hours}")
print(f"Amount earned: ${earnings}")
print(f"Hourly earnings: ${hourly_rate:.2f}")
