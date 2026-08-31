print("Shift Earnings Tracker")
print()

date = input("Enter the shift date: ")
job = input("Enter the job name: ")
hours = float(input("Enter the hours worked: "))
earnings = float(input("Enter the amount earned: $"))
hourly_rate = earnings / hours

print()
print("Shift Summary")
print(f"Date: {date}")
print(f"Job: {job}")
print(f"Hours worked: {hours}")
print(f"Amount earned: ${earnings}")
print(f"Hourly earnings: ${hourly_rate:.2f}")
