def calculate_parking_cost(day_of_week, parking_time):
    rates = {
        "monday": 2.00,
        "tuesday": 2.00,
        "wednesday": 2.00,
        "thursday": 2.50,
        "friday": 2.50,
        "saturday": 3.00,
        "sunday": 3.00
    }

    day_of_week_lower = day_of_week.lower()
    if day_of_week_lower in rates and parking_time > 0:
        full_hours = int(parking_time)
        fractional_hours = parking_time - full_hours

        if fractional_hours > 0.0833:  # 5 minutes in hours
            full_hours += 1

        total_cost = rates[day_of_week_lower] * full_hours
        return total_cost

    return "Error: Incorrect input"

# Get user input
day = input("Enter the day of the week: ")
time = float(input("Enter the parking time in hours: "))

# Calculate and display parking cost
cost = calculate_parking_cost(day, time)
print("The parking cost is:", cost)