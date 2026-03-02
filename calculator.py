"""
Project: Simple Calculator
Author: Rahila S
Description:
A basic calculator program that performs
addition, subtraction, multiplication, and division.
Created for GitHub Setup Activity.
"""

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


def main():
    print("=== Simple Calculator ===")

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("\nResults:")
        print("Addition:", add(num1, num2))
        print("Subtraction:", subtract(num1, num2))
        print("Multiplication:", multiply(num1, num2))
        print("Division:", divide(num1, num2))

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()
