import math

history = []


# BASIC OPERATIONS 

def addition():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    result = a + b
    print("result:", result)
    history.append(f"{a} + {b} = {result}")


def subtraction():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))
    result = a - b
    print("result:", result)
    history.append(f"{a} - {b} = {result}")


def multiplication():
    a = float(input("enter first number: "))
    b = float(input("Enter second number: "))
    result = a * b
    print("Result:", result)
    history.append(f"{a} × {b} = {result}")


def division():
    a = float(input("enter first number: "))
    b = float(input("enter second number: "))

    if b == 0:
        print("error: Cannot divide by zero!")
        return

    result = a / b
    print("Result:", result)
    history.append(f"{a} ÷ {b} = {result}")


def modulus():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if b == 0:
        print("Error: Cannot divide by zero!")
        return

    result = a % b
    print("Result:", result)
    history.append(f"{a} % {b} = {result}")


def power():
    a = float(input("Enter base: "))
    b = float(input("Enter power: "))

    result = a ** b
    print("Result:", result)
    history.append(f"{a} ^ {b} = {result}")


# SCIENTIFIC OPERATIONS

def square_root():
    a = float(input("enter number: "))

    if a < 0:
        print("Error: Square root of negative number is not possible.")
        return

    result = math.sqrt(a)
    print("Result:", result)
    history.append(f"√{a} = {result}")


def factorial():
    a = int(input("Enter a positive integer: "))

    if a < 0:
        print("Error: Factorial cannot be negative.")
        return

    result = math.factorial(a)
    print("Result:", result)
    history.append(f"{a}! = {result}")


def logarithm():
    a = float(input("Enter number: "))

    if a <= 0:
        print("Error: Logarithm requires a positive number.")
        return

    print("\n1. Natural Log (ln)")
    print("2. Log base 10")

    choice = input("Choose: ")

    if choice == "1":
        result = math.log(a)
        print("Result:", result)
        history.append(f"ln({a}) = {result}")

    elif choice == "2":
        result = math.log10(a)
        print("Result:", result)
        history.append(f"log10({a}) = {result}")

    else:
        print("Invalid choice!")


# TRIGONOMETRY

def trigonometry():

    angle = float(input("Enter angle in degrees: "))

    radians = math.radians(angle)

    print("\n1. sin")
    print("2. cos")
    print("3. tan")

    choice = input("Choose: ")

    if choice == "1":
        result = math.sin(radians)
        print("sin(", angle, ") =", result)
        history.append(f"sin({angle}) = {result}")

    elif choice == "2":
        result = math.cos(radians)
        print("cos(", angle, ") =", result)
        history.append(f"cos({angle}) = {result}")

    elif choice == "3":
        if abs(math.cos(radians)) < 1e-10:
            print("Error: tan is undefined at this angle.")
            return

        result = math.tan(radians)
        print("tan(", angle, ") =", result)
        history.append(f"tan({angle}) = {result}")

    else:
        print("Invalid choice!")


# PERCENTAGE

def percentage():

    number = float(input("Enter number: "))
    percent = float(input("Enter percentage: "))

    result = (number * percent) / 100

    print(percent, "% of", number, "=", result)
    history.append(f"{percent}% of {number} = {result}")


#  DISCOUNT

def discount():

    price = float(input("Enter original price: "))
    discount_percent = float(input("Enter discount percentage: "))

    discount_amount = price * discount_percent / 100
    final_price = price - discount_amount

    print("Discount amount:", discount_amount)
    print("Final price:", final_price)

    history.append(
        f"Price={price}, Discount={discount_percent}%, Final={final_price}"
    )


# BMI

def bmi():

    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))

    if height <= 0:
        print("Invalid height!")
        return

    result = weight / (height ** 2)

    print("BMI:", round(result, 2))
    history.append(f"BMI = {round(result, 2)}")


# HISTORY 

def show_history():

    if len(history) == 0:
        print("\nNo calculations yet.")
        return

    print("\n========== CALCULATION HISTORY ==========")

    for i in range(len(history)):
        print(i + 1, ".", history[i])


def clear_history():

    history.clear()
    print("History cleared successfully!")


# ---------------- MAIN MENU ----------------

while True:

    print("\n")
    print("---------------------------------")
    print("          🧮 SMART CALCULATOR")
    print("----------------------------------")

    print("1.  Addition")
    print("2.  Subtraction")
    print("3.  Multiplication")
    print("4.  Division")
    print("5.  Modulus")
    print("6.  Power")
    print("7.  Square Root")
    print("8.  Factorial")
    print("9.  Logarithm")
    print("10. Trigonometry")
    print("11. Percentage")
    print("12. Discount Calculator")
    print("13. BMI Calculator")
    print("14. View History")
    print("15. Clear History")
    print("16. Exit")

    choice = input("\nEnter your choice: ")

    try:

        if choice == "1":
            addition()

        elif choice == "2":
            subtraction()

        elif choice == "3":
            multiplication()

        elif choice == "4":
            division()

        elif choice == "5":
            modulus()

        elif choice == "6":
            power()

        elif choice == "7":
            square_root()

        elif choice == "8":
            factorial()

        elif choice == "9":
            logarithm()

        elif choice == "10":
            trigonometry()

        elif choice == "11":
            percentage()

        elif choice == "12":
            discount()

        elif choice == "13":
            bmi()

        elif choice == "14":
            show_history()

        elif choice == "15":
            clear_history()

        elif choice == "16":
            print("\nThank you for using Smart Calculator!")
            print("Goodbye")
            break

        else:
            print("Invalid choice! Please select 1–16.")

    except ValueError:
        print("Error: Please enter a valid number.")

    except OverflowError:
        print("Error: Number is too large.")
