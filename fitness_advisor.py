# --------------------------------------------------
# Fitness Advisor
# Final Project for Code in Place 2026
#
# This program helps users track their health and
# fitness. It calculates BMI and BMR, tracks
# calories, steps, exercises, and weight history,
# and provides simple fitness recommendations.
# --------------------------------------------------


# Calculate Body Mass Index (BMI)
# BMI helps determine whether a person's weight
# is healthy for their height.
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi


# Calculate Basal Metabolic Rate (BMR)
# BMR is the number of calories the body needs
# each day to perform basic functions such as
# breathing and circulation while at rest.
def calculate_bmr(weight, height, age, gender):

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return bmr


# Convert BMI value into a category that is easier
# for users to understand.
def get_bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# Use previous weight measurements to estimate
# what the user's weight may be next week.
# This is a simple trend calculation.
def predict_weight(weight_history):

    if len(weight_history) < 2:
        return weight_history[-1]

    change = (
        weight_history[-1] - weight_history[0]
    ) / (len(weight_history) - 1)

    predicted_weight = weight_history[-1] + change

    return predicted_weight


# Provide fitness suggestions based on BMI and
# average daily steps.
def give_advice(bmi, average_steps):

    print("\nPersonalized Advice")

    if bmi < 18.5:
        print("- Consider increasing your calorie intake.")
        print("- Add strength training exercises.")

    elif bmi > 25:
        print("- Try increasing daily activity.")
        print("- Consider reducing calorie intake.")

    else:
        print("- Your BMI is in a healthy range.")

    if average_steps < 5000:
        print("- Try walking more each day.")

    elif average_steps >= 8000:
        print("- Great job staying active!")


def main():

    print("=" * 40)
    print("        FITNESS ADVISOR")
    print("=" * 40)

    # Collect basic information from the user

    name = input("Enter your name: ")

    age = int(input("Enter your age: "))

    gender = input(
        "Enter gender (male/female): "
    ).lower()

    weight = float(
        input("Enter your weight (kg): ")
    )

    height = float(
        input("Enter your height (cm): ")
    )

    # Calculate health metrics

    bmi = calculate_bmi(weight, height)

    bmr = calculate_bmr(
        weight,
        height,
        age,
        gender
    )

    print("\nChoose Activity Level")
    print("1. Sedentary")
    print("2. Lightly Active")
    print("3. Moderately Active")
    print("4. Very Active")

    activity = int(
        input("Enter choice: ")
    )

    # Activity level determines how many calories
    # are burned based on lifestyle.

    activity_levels = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725
    }

    daily_calories = (
        bmr * activity_levels[activity]
    )

    # Store calorie data for the last 7 days

    calorie_history = []

    print(
        "\nEnter calories consumed during the last 7 days"
    )

    for day in range(1, 8):

        calories = int(
            input("Day " + str(day) + ": ")
        )

        calorie_history.append(calories)

    # Store step data for the last 7 days

    step_history = []

    print(
        "\nEnter steps walked during the last 7 days"
    )

    for day in range(1, 8):

        steps = int(
            input("Day " + str(day) + ": ")
        )

        step_history.append(steps)

    # Allow the user to enter exercises until
    # they type "done"

    exercises = []

    print("\nExercise Log")
    print("Type 'done' when finished.")

    while True:

        exercise = input("Exercise: ")

        if exercise.lower() == "done":
            break

        exercises.append(exercise)

    # Store weight history for the previous weeks

    weight_history = []

    print(
        "\nEnter your weight history for the last 4 weeks"
    )

    for week in range(1, 5):

        weekly_weight = float(
            input("Week " + str(week) + ": ")
        )

        weight_history.append(weekly_weight)

    # Calculate averages

    average_calories = (
        sum(calorie_history)
        / len(calorie_history)
    )

    average_steps = (
        sum(step_history)
        / len(step_history)
    )

    # Predict future weight

    predicted_weight = predict_weight(
        weight_history
    )

    # Create a simple fitness score

    fitness_score = 0

    if 18.5 <= bmi <= 24.9:
        fitness_score += 40

    if average_steps >= 8000:
        fitness_score += 30

    if average_calories <= daily_calories:
        fitness_score += 30

    # Display final report

    print("\n" + "=" * 40)
    print("          FITNESS REPORT")
    print("=" * 40)

    print("Name:", name)
    print("Age:", age)

    print("\nBMI:", round(bmi, 2))
    print(
        "BMI Category:",
        get_bmi_category(bmi)
    )

    print("\nBMR:", round(bmr, 2))

    print(
        "Estimated Daily Calories:",
        round(daily_calories, 2)
    )

    print(
        "\nAverage Daily Calories:",
        round(average_calories, 2)
    )

    print(
        "Average Daily Steps:",
        round(average_steps, 2)
    )

    print("\nExercises Performed:")

    for exercise in exercises:
        print("-", exercise)

    print(
        "\nFitness Score:",
        fitness_score,
        "/100"
    )

    print(
        "\nPredicted Weight Next Week:",
        round(predicted_weight, 2),
        "kg"
    )

    give_advice(
        bmi,
        average_steps
    )

    print(
        "\nThank you for using Fitness Advisor!"
    )


if __name__ == "__main__":
    main()
