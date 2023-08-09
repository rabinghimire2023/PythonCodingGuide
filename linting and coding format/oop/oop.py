"""Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.
"""
class University:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    def add_department(self, department):
        self._departments.append(department)

    def display_details(self):
        print(f"University Name: {self._name}")
        print(f"Location: {self._location}")
        print("Departments:")
        for department in self._departments:
            print(f"  - {department.get_name()}")

class Department(University):
    def __init__(self, name, location, dept_name, head):
        super().__init__(name, location)
        self._dept_name = dept_name
        self._head = head
        self._courses_offered = []

    def add_course(self, course):
        self._courses_offered.append(course)

    def get_name(self):
        return self._dept_name

    def display_details(self):
        print(f"Department Name: {self._dept_name}")
        print(f"Head of Department: {self._head}")
        print("Courses Offered:")
        for course in self._courses_offered:
            print(f"  - {course}")

# Example usage
if __name__ == "__main__":
    # Creating a University object
    university = University("Tribhuvan University", "Kathmandu")

    # Creating Department objects
    dept1 = Department("Tribuvan University", "Kathmandu", "Computer Science", "Dr. Rabin Ghimire")
    dept2 = Department("Purwanchal University", "Biratnagar", "Mathematics", "Prof. Ram shrestha")

    # Adding courses to departments
    dept1.add_course("Introduction to Programming")
    dept1.add_course("Data Structures and Algorithms")
    dept2.add_course("Calculus")
    dept2.add_course("Linear Algebra")

    # Adding departments to the university
    university.add_department(dept1)
    university.add_department(dept2)

    # Displaying university and department details
    university.display_details()
    print("\n---\n")
    dept1.display_details()
    print("\n---\n")
    dept2.display_details()

#ouput
#University Name: Tribhuvan University
# Location: Kathmandu
# Departments:
#   - Computer Science
#   - Mathematics

# ---

# Department Name: Computer Science
# Head of Department: Dr. Rabin Ghimire
# Courses Offered:
#   - Introduction to Programming
#   - Data Structures and Algorithms

# ---

# Department Name: Mathematics
# Head of Department: Prof. Ram shrestha
# Courses Offered:
#   - Calculus
#   - Linear Algebra

"""Build a Python class to represent a simple banking system. Create a class for a
BankAccount, and another for Customer. The BankAccount class should have a
constructor to initialize the account details (account number, balance, account type).
The Customer class should have a constructor to set the customer's details (name,
age, address) and create a BankAccount object for each customer. Implement a
destructor for both classes to display a message when objects are destroyed."""
class BankAccount:
    def __init__(self, account_number, balance, account_type):
        self.account_number = account_number
        self.balance = balance
        self.account_type = account_type

    def __del__(self):
        print(f"Bank account with account number {self.account_number} has been closed.")

class Customer:
    def __init__(self, name, age, address, account_number, balance, account_type):
        self.name = name
        self.age = age
        self.address = address
        self.bank_account = BankAccount(account_number, balance, account_type)

    def __del__(self):
        print(f"Customer {self.name} with account number {self.bank_account.account_number} has been removed.")

# Example usage
if __name__ == "__main__":
    # Creating a Customer object with a BankAccount
    customer1 = Customer("Rabin Ghimire", 30, "Imadol", "12345678", 1000.0, "Savings")
    customer2 = Customer("Swastika Dhakal", 25, "Itahari", "87654321", 500.0, "Checking")

    # Accessing customer details and bank account details
    print("Customer 1 Details:")
    print(f"Name: {customer1.name}")
    print(f"Age: {customer1.age}")
    print(f"Address: {customer1.address}")
    print(f"Account Number: {customer1.bank_account.account_number}")
    print(f"Balance: {customer1.bank_account.balance}")
    print(f"Account Type: {customer1.bank_account.account_type}")

    print("\nCustomer 2 Details:")
    print(f"Name: {customer2.name}")
    print(f"Age: {customer2.age}")
    print(f"Address: {customer2.address}")
    print(f"Account Number: {customer2.bank_account.account_number}")
    print(f"Balance: {customer2.bank_account.balance}")
    print(f"Account Type: {customer2.bank_account.account_type}")

    # Deleting objects (this will trigger the destructors)
    del customer1
    del customer2

#ouput
# Customer 1 Details:
# Name: Rabin Ghimire
# Age: 30
# Address: Imadol
# Account Number: 12345678
# Balance: 1000.0
# Account Type: Savings

# Customer 2 Details:
# Name: Swastika Dhakal
# Age: 25
# Address: Itahari
# Account Number: 87654321
# Balance: 500.0
# Account Type: Checking
# Customer Rabin Ghimire with account number 12345678 has been removed.
# Bank account with account number 12345678 has been closed.
# Customer Swastika Dhakal with account number 87654321 has been removed.
# Bank account with account number 87654321 has been closed.