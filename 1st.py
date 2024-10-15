def calculate_bmr(weight, height, age, gender):
    if gender.lower() == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    return bmr

def calculate_tdee(bmr, activity_level):
    activity_factors = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    return bmr * activity_factors[activity_level]

def main():
    gender = input("Enter your gender (male/female): ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))
    age = int(input("Enter your age: "))
    activity_level = input("Enter your activity level (sedentary, light, moderate, active, very active): ")

    bmr = calculate_bmr(weight, height, age, gender)
    tdee = calculate_tdee(bmr, activity_level)

    print(f"Your Basal Metabolic Rate (BMR) is {bmr:.2f} calories/day.")
    print(f"Your Total Daily Energy Expenditure (TDEE) is {tdee:.2f} calories/day.")

if __name__ == "__main__":
    main()
