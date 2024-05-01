from functions import *
import os

os.system("cls") 

print("Welcome to the calculator!")

while True:
    first_number = float(input("\nType the first number: "))

    print("[+] -> Sum \n[-] -> Subtraction \n[*] -> Multiplication \n[/] -> Division")

    while True:
        Operation_choice_type = input("\nEnter the symbol of the type of operation you want to perform: ")
        if Operation_choice_type in ["+", "-", "*", "/"]:
            break
        else:
            print("\nThe value entered is not available in the calculator.")
            print("Please try type +, -, * or / again.")
    second_number = float(input("Type the second number: "))
    if Operation_choice_type == "+":
        answer = sum(first_number, second_number)
        print(f"The result of the sum is {answer}")

    elif Operation_choice_type == "-":
        answer = sub(first_number, second_number)
        print(f"The result of the subtraction is {answer}")

    elif Operation_choice_type == "*":
        answer = times(first_number, second_number)
        print(f"The result of the multiplication is {answer}")

    elif Operation_choice_type == "/":
        answer = division(first_number, second_number)
        print(f"The result of the division is {answer}")

    while True:
        exit_or_continue = int(input("\nDo you want to perform any further operations? \n\n0 - Yes | 1 - No: "))
        if exit_or_continue == 0:
            break
        elif exit_or_continue == 1:
            exit()
        else: 
            print("Invalid choice. Please enter a valid option.")