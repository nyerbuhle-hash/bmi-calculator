def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """
    Calculate BMI using the formula:
    BMI = weight (kg) / height (m)^2
    """
    return weight_kg / (height_m ** 2)


def bmi_category(bmi: float) -> str:
    """
    Determine the BMI category based on the calculated BMI.
    Categories follow the standard WHO guidelines.
 
    Args:
        bmi (float): The calculated BMI value.
 
    Returns:
        str: The BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"
 
 
def main():
    try:
        height = float(input("Enter your height in metres: "))
        weight = float(input("Enter your weight in kilograms: "))
 
        bmi = calculate_bmi(weight, height)
        category = bmi_category(bmi)
 
        print(f"Your BMI is: {round(bmi, 2)} ({category})")
 
    except ValueError:
        print("Invalid input. Please enter numbers only.")
 
 
if __name__ == "__main__":
    main()
