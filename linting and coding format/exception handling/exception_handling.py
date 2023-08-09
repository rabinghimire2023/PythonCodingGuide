"""EXception handling assignment 
"""
#Write a Python program that takes two integers as input and performs division
#(num1 / num2). Handle the ZeroDivisionError and display a custom error message
#when the second number is zero
def division(numb1:int,numb2:int):
    """Division operation

    Args:
        numb1 (int): _description_
        numb2 (int): _description_

    Returns:
        _type_: _description_
    """
    try:
        division_result = numb1/numb2
        return division_result
    except ZeroDivisionError:
        print("Error:Division by zero!")
        return None
    print(division(5,5)) #output: 1.0
print(division(5,0)) #output: Error:Division by zero! --None

#Implement a program that takes user input for a filename, opens the file in read
#mode, and displays its contents. Handle the FileNotFoundError and display an error
#message if the file is not found.
def read_file(file_name:str):
    """Read file.

    Args:
        file_name (str): filename
    """
    try:
        with open(file_name,'r',encoding="utf-8") as file:
            content=file.read()
            print(f"filename is {file_name}")
            print(content)
    except FileNotFoundError:
        print("Error:File not found")
filename=input(str("Enter filename:"))
read_file(filename)

#output:
#Enter filename:rabin
#Error:File not found

#Write a Python program that takes a user input and converts it to an integer. Handle
#the ValueError and display a custom error message when the input cannot be
#converted to an integer.
def converted_integer(usr_input:int):
    """Integer converted.

    Args:
        usr_input (int): user input

    Returns:
        result_: ouptut result
    """
    try:
        result_=int(usr_input)
        return result_
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        return None
user_input = input("Enter an integer: ")
result = converted_integer(user_input)
if result is not None:
    print(f"The converted integer is: {result}")
#output:
#Enter an integer: 34
#The converted integer is: 34

#Enter an integer: 56.23
#Error: Invalid input. Please enter a valid integer.

#Write a Python program that takes two integers as input and performs division (num1
#/ num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and
#display appropriate error messages.

def perform_division(number1, number2):
    """Division operation

    Args:
        number1 (int): first number.
        number2 (int): second number

    Returns:
        result2(int): output result
    """
    try:
        result2 = number1 / number2
        return result2
    except ValueError:
        print("Error: Invalid input. Please enter valid integers.")
        return None
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
result = perform_division(num1, num2)
if result is not None:
    print(f"The result of division is: {result}")
#output:
# Enter the first number: 23
#Enter the second number: 0
#Error: Cannot divide by zero.

#Enter the first number: 23
#Enter the second number: 23
#The result of division is: 1.0

#Write a Python program that takes user input for age. Create a custom exception
#InvalidAgeError to handle cases where the age is below 0 or above 120.
class InvalidAgeError(Exception):
    """Custom exception

    Args:
        Exception : exception.
    """
def check_age(age_check):
    """Check age

    Args:
        age_check (int): age

    Raises:
        InvalidAgeError: custom exception

    Returns:
        age_check: 
    """
    try:
        if age_check < 0 or age_check > 120:
            raise InvalidAgeError
        return age_check
    except InvalidAgeError as exception:
        print(exception,"Error: Invalid age.")
        return None
age = int(input("Enter ager: "))
check_result = check_age(age)
if check_result is not None:
    print(f"Your age: {check_result}")
#output:
#Enter ager: 125
#Error: Invalid age.

#Enter ager: 20
#Your age: 20

#Implement a program that reads user input for a password. Create a custom
#exception WeakPasswordError to handle cases where the password is shorter
#than 8 characters.

class WeakPasswordError(Exception):
    """Custom exception
    """
def check_password_strength(pwd:str):
    """Check pssword strength.

    Args:
        pwd (str): password.

    Raises:
        WeakPasswordError: custom exception.

    Returns:
        pwd(str): password.
    """
    try:
        if len(pwd) < 8:
            raise WeakPasswordError("Weak password. Password must be at least 8 characters long.")
        return pwd
    except WeakPasswordError as exception:
        print(exception)

password = input("Enter your password: ")
password = check_password_strength(password)
if password is not None:
    print("Password set successfully!")
#ouput:
# Enter your password: 12
#Weak password. Password must be at least 8 characters long.

#Enter your password: 12346789
#Password set successfully!
