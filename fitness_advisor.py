# --------------------------------------------------
# Fitness Advisor
# Final Project for Code in Place 2026
#
# This program helps users track their health
# and fitness. It calculates BMI and BMR,
# estimates daily calorie needs, tracks calories,
# steps, water intake, exercises, and weight
# history, and provides personalized advice.
# --------------------------------------------------


# Calculate Body Mass Index (BMI)
def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    return bmi


# Calculate Basal Metabolic Rate (BMR)
# BMR estimates how many calories your body
# needs each day while at rest.
def calculate_bmr(weight, height, age, gender):

    if gender == "male":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)

    return bmr


# Return BMI category
def get_bmi_category(bmi):

    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal Weight"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


# Predict next week's weight using past trends
def predict_weight(weight_history):

    if len(weight_history) < 2:
        return weight_history[-1]

    average_change = (
        weight_history[-1] - weight_history[0]
    ) / (len(weight_history) - 1)

    predicted_weight = (
        weight_history[-1] + average_change
    )

    return predicted_weight


# Give personalized fitness advice
def give_advice(bmi, average_steps, average_water):

    print("\nPERSONALIZED ADVICE")

    if bmi < 18.5:
        print("- Consider increasing healthy calorie intake.")
        print("- Include strength training exercises.")

    elif bmi > 25:
        print("- Try increasing physical activity.")
        print("- Monitor your calorie intake carefully.")

    else:
        print("- Your BMI is in a healthy range.")

    if average_steps < 5000:
        print("- Try walking more each day.")
    elif average_steps >= 8000:
        print("- Great job staying active!")

    if average_water < 2:
        print("- Try drinking more water each day.")
    else:
        print("- Great job staying hydrated!")


def main():

    print("=" * 50)
    print("            FITNESS ADVISOR")
    print("=" * 50)

    # Collect user information

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

    # Calculate BMI and BMR

    bmi = calculate_bmi(weight, height)

    bmr = calculate_bmr(
        weight,
        height,
        age,
        gender
    )

    # Activity level selection

    print("\nChoose Your Activity Level")
    print("1. Sedentary")
    print("2. Lightly Active")
    print("3. Moderately Active")
    print("4. Very Active")

    activity = int(
        input("Enter choice (1-4): ")
    )

    activity_levels = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725
    }

    daily_calories = (
        bmr * activity_levels[activity]
    )

    # Fitness goal

    print("\nChoose Your Fitness Goal")
    print("1. Lose Weight")
    print("2. Maintain Weight")
    print("3. Gain Weight")

    goal = int(
        input("Enter choice (1-3): ")
    )

    if goal == 1:
        target_calories = daily_calories - 500
        goal_name = "Lose Weight"

    elif goal == 2:
        target_calories = daily_calories
        goal_name = "Maintain Weight"

    else:
        target_calories = daily_calories + 500
        goal_name = "Gain Weight"

    # Track calorie intake

    calorie_history = []

    print(
        "\nEnter calories consumed during the last 7 days"
    )

    for day in range(1, 8):

        calories = int(
            input("Day " + str(day) + ": ")
        )

        calorie_history.append(calories)

    # Track daily steps

    step_history = []

    print(
        "\nEnter steps walked during the last 7 days"
    )

    for day in range(1, 8):

        steps = int(
            input("Day " + str(day) + ": ")
        )

        step_history.append(steps)

    # Track water intake

    water_history = []

    print(
        "\nEnter water intake for the last 7 days (liters)"
    )

    for day in range(1, 8):

        water = float(
            input("Day " + str(day) + ": ")
        )

        water_history.append(water)

    # Exercise log

    exercises = []

    print("\nExercise Log")
    print("Type 'done' when finished.")

    while True:

        exercise = input("Exercise: ")

        if exercise.lower() == "done":
            break

        exercises.append(exercise)

    # Weight history

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

    average_water = (
        sum(water_history)
        / len(water_history)
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

    if average_water >= 2:
        fitness_score += 15

    if average_calories <= target_calories:
        fitness_score += 15

    # Display report

    print("\n" + "=" * 50)
    print("             FITNESS REPORT")
    print("=" * 50)

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
        "Fitness Goal:",
        goal_name
    )

    print(
        "Target Calories:",
        round(target_calories, 2)
    )

    print(
        "\nAverage Daily Calories:",
        round(average_calories, 2)
    )

    print(
        "Average Daily Steps:",
        round(average_steps, 2)
    )

    print(
        "Average Water Intake:",
        round(average_water, 2),
        "liters"
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
        average_steps,
        average_water
    )

    print("\nThank you for using Fitness Advisor!")


if __name__ == "__main__":
    main()
