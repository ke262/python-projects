num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\n--- Comparison Result ---")

if num1 == num2:
    print(f"Both number are equal: {num1}")
elif num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num2} is greater than {num1}")

if num1 == 0 or num2 == 0:
    print("\nAt leat one number is zero.")
else:
    print("\nBoth numbers are non-zero.")