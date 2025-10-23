# Nikhil Bhiduri | 2501010128 | Calorie Tracker

def cal_trckr():
    print("=" * 50)
    print("Welcome to my Calorie Tracker")
    print("=" * 50)

    meal_names = []
    calorie_values = []

    try:
        num_meals = int(input("\nNo of meals to be recorded: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    for i in range(num_meals):
        print(f"\nMeal {i+1}:")
        meal = input("Enter meal name: ").strip()
        try:
            calories = float(input("Enter calorie amount: "))
        except ValueError:
            print("Invalid calorie input. Skipping this meal.")
            continue
        meal_names.append(meal)
        calorie_values.append(calories)

    total_calories = sum(calorie_values)
    average_calories = total_calories / len(calorie_values) if calorie_values else 0

    try:
        daily_limit = float(input("\nEnter your daily calorie limit: "))
    except ValueError:
        print("Invalid limit. Assuming no limit.")
        daily_limit = float('inf')

    print("\nSummary:")
    print("-" * 50)
    print(f"{'Meal':<30} {'Calories':>10}")
    print("-" * 50)
    for meal, cal in zip(meal_names, calorie_values):
        print(f"{meal:<30} {cal:>10.2f}")
    print("-" * 50)
    print(f"{'Total Calories':<30} {total_calories:>10.2f}")
    print(f"{'Average per Meal':<30} {average_calories:>10.2f}")
    print(f"{'Daily Limit':<30} {daily_limit:>10.2f}")
    print("-" * 50)

    if total_calories > daily_limit:
        print("Warning: You have exceeded your daily calorie limit!")
    else:
        print("Very good, you're under your daily limit!")
        
cal_trckr()