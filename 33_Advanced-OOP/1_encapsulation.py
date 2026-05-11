#33     Object-Oriented Programming (OOP): A programming style that organizes code into objects, which are instances of classes. 
#       OOP allows for encapsulation, inheritance, abstraction and polymorphism, making it easier to manage and reuse code.
#* Encapsulation (suitcase): The bundling all the methods and attributes inside a class, and restricting access to some of the object's components.
#* Inheritance (family traits): The mechanism by which a class(subclass) can inherit attributes and methods from another class(superclass).
#* Abstraction (remote control): The process of hiding complex implementation details and showing only the essential features of an object by calling its methods.
#* Polymorphism (shape-shifting): The ability of an object to take many forms. It allows objects of different types to be treated as instances of the same type through a common interface.

#1* Encapsulation Example using single underscore(protected attributes, which can be accessed within the class and its subclasses) and double underscore(private attributes, which can only be accessed within the class itself)
class Wallet:
   def __init__(self, balance):
       self.__balance = balance # Private attribute

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount # Add to the balance safely

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount # Remove from the balance safely

try:
    account = Wallet(100)
    # This line normally crashes the program
    print(account.__balance) 
except AttributeError:
    print("Error: You cannot access '__balance' directly because it is private.")

# To access the balance, we can create a method that returns it:
class Wallet:
   def __init__(self, balance):
       self.__balance = balance

   def deposit(self, amount):
       if amount > 0:
           self.__balance += amount

   def withdraw(self, amount):
       if 0 < amount <= self.__balance:
           self.__balance -= amount

   def get_balance(self):
       return self.__balance # Method to access the private attribute

acct_one = Wallet(100)  # Create an instance of the Wallet class with an initial balance of 100
acct_one.deposit(50)
print(acct_one.get_balance()) # Output: 150

acct_two = Wallet(450)
acct_two.withdraw(28)
print(acct_two.get_balance()) # Output: 422

acct_two.deposit(150)
print(acct_two.get_balance()) # Output: 572

# Defining a private(__validate) method to check if every deposit or withdrawal amount is a positive number:
class Wallet:
   def __init__(self):
       self.__balance = 0

   def __validate(self, amount):
       if amount <= 0:
           raise ValueError("Amount must be a positive number")

   def deposit(self, amount):
       self.__validate(amount) # Validate the amount before depositing
       self.__balance += amount

   def withdraw(self, amount):
       self.__validate(amount) # Validate the amount before withdrawing
       if amount > self.__balance:
           raise ValueError("Insufficient funds")
       self.__balance -= amount

   def get_balance(self):
       return self.__balance

my_wallet = Wallet()

while True:
    print("----- Wallet Menu -----")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Select an option (1-4): ")

    if choice == "4":
        print("Exiting the wallet menu. Goodbye!")
        break

    try:
        if choice in ["1", "2"]:
            amount = float(input("Enter the amount: "))
            if choice == "1":
                my_wallet.deposit(amount)
                print(f"Deposit successful ${amount}")
            else:
                my_wallet.withdraw(amount)
                print(f"Withdrawal successful ${amount}")
        if choice == "3":
            print(f"Current balance: ${my_wallet.get_balance()}")
        else:
            print("Invalid choice. Please pick 1, 2, 3, or 4.")

    except ValueError as e:
        print(f"Error: {e}")