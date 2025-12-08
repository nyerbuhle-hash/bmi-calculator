# bmi-calculator

A clean, well-structured Python BMI (Body Mass Index) calculator.
This project includes BMI calculation, category classification, and modern Python practices used in software and machine learning engineering.

## 📌 Features
- Calculates BMI using the standard formula
- Determines WHO-based BMI categories
- Uses modular, reusable functions
- Includes type hints for clarity and safety
- Handles invalid user input
- Clean and professional project structure

## 🧮 BMI Formula

$begin:math:display$
BMI \= \\frac\{weight\\ \(kg\)\}\{height\\ \(m\)\^2\}
$end:math:display$

## 🧠 How the Code Works

This project is structured into small, modular functions:

### **1. `calculate_bmi(weight_kg: float, height_m: float) -> float`**
- Takes weight and height
- Returns the BMI
- Reusable anywhere (web apps, APIs, ML models)

### **2. `bmi_category(bmi: float) -> str`**
- Takes the BMI value
- Returns the correct category:
- Underweight
- Normal weight
- Overweight
- Obesity

### **3. `main()`**
- Handles user input
- Calls the calculation and category functions
- Prints the final result

This style follows real ML engineering workflows: **separate, clear modules that each do one job**.

## 💻 How to Run

Make sure Python is installed, then run:

```bash
python bmi_calculator.py
```

## 🖥️ Example Output

When you run the program, it should look like this:

```text
Enter your height in metres: 1.75
Enter your weight in kilograms: 70
Your BMI is: 22.86 (Normal weight)
```

If the user enters invalid input:

```text
Enter your height in metres: abc
Enter your weight in kilograms: 70
Invalid input. Please enter numbers only.
```
