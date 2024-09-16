from prettytable import PrettyTable

def calculate_calories(age, sex, height, weight, body_fat_percentage, activity_level):
    # Calculate BMR using Katch-McArdle formula
    lean_body_mass = weight * (1 - body_fat_percentage / 100)
    BMR = 370 + (21.6 * lean_body_mass)
    
    # Define activity levels
    activity_multipliers = {
        'sedentary': 1.2,       # Little or no exercise
        'lightly_active': 1.375, # Light exercise/sports 1-3 days/week
        'moderately_active': 1.55, # Moderate exercise/sports 3-5 days/week
        'very_active': 1.725,    # Hard exercise/sports 6-7 days a week
        'extra_active': 1.9      # Very hard exercise/sports & physical job or 2x training
    }
    
    # Get activity multiplier
    if activity_level not in activity_multipliers:
        raise ValueError("Invalid activity level. Choose from: 'sedentary', 'lightly_active', 'moderately_active', 'very_active', 'extra_active'.")
    
    activity_multiplier = activity_multipliers[activity_level]
    
    # Calculate daily and weekly calories
    daily_calories = BMR * activity_multiplier
    weekly_calories = daily_calories * 7
    
    return daily_calories, weekly_calories

# Input data
age = int(input("Enter your age: "))
sex = input("Enter your sex (male/female): ").lower()
height = float(input("Enter your height in cm: ")) / 100  # Convert cm to meters
weight = float(input("Enter your weight in kg: "))
body_fat_percentage = float(input("Enter your body fat percentage: "))
activity_level = input("Enter your activity level (sedentary, lightly_active, moderately_active, very_active, extra_active): ").lower()

# Calculate
daily_calories, weekly_calories = calculate_calories(age, sex, height, weight, body_fat_percentage, activity_level)

# Create a PrettyTable object
table = PrettyTable()
table.field_names = ["Parameter", "Value"]

# Add rows to the table
table.add_row(["Age", age])
table.add_row(["Sex", sex.capitalize()])
table.add_row(["Height (m)", height])
table.add_row(["Weight (kg)", weight])
table.add_row(["Body Fat Percentage (%)", body_fat_percentage])
table.add_row(["Activity Level", activity_level.replace('_', ' ').capitalize()])
table.add_row(["Daily Caloric Requirement (kcal)", f"{daily_calories:.2f}"])
table.add_row(["Weekly Caloric Requirement (kcal)", f"{weekly_calories:.2f}"])

# Print the table
print(table)
