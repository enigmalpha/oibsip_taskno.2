def calculate_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi
def classify_bmi(bmi):
    if bmi<18.5:
        return "Under Weight"
    elif bmi>=18.5 and bmi<24.9:
        return "Healthy Weight"
    elif bmi>=25.0 and bmi<29.9:
        return "Over Weight"
    elif bmi>30:
        return "Obese"
    return bmi
def main():
    weight = float(input("Enter your weight in Kilograms: "))
    height = float(input("Enter your height in meters: "))
    bmi = calculate_bmi(weight,height)
    category = classify_bmi(bmi)
    print(f"Your bmi is {bmi}")
    print(f"You are classified as {category}")
if __name__ == "__main__":
    main()
