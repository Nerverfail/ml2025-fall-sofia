# 1. Create a Python program:

# The program asks the user for input N (positive integer) and reads it

# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)

# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputted it before.

# The basic functionality of data processing (data initialization, data insertion, data search) should be done via Object-Oriented Programming Paradigm (i.e. using Classes)

# Name this program "module5_oop.py" and upload it to the above-mentioned repo.

# 2. Create the functionality outside of the main running code: i.e., create the module with the Class described in the item above, and name this module "module5_mod.py" + create the main program "module5_call.py" that uses the Class description from the "*_mod" file.  Upload everything to the above-mentioned repo.


class NumberProcessor:
    def __init__(self):
        self.number_size = 0
        self.numbers = []

    def initialize_n(self):
        while True:
            try:
                n = int(input("Enter a positive integer N: "))
                if n > 0:
                    self.number_size = n
                    return n
                else:
                    print("N must be a positive integer. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def initialize_numbers(self, n):
        while len(self.numbers) < n:
            try:
                number = int(input("Enter a number: "))
                self.numbers.append(number)
                print(f"Number {number} added.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
        print(f"All {n} numbers have been added: {self.numbers}")

    def find_number(self):
        try:
            x = int(input("Enter an integer X to search for: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            return
        if x in self.numbers:
            print(self.numbers.index(x) + 1)
            return self.numbers.index(x) + 1
        else:
            print(-1)
            return -1
    
    def __repr__(self):
        return f"NumberProcessor(numbers={self.numbers})"
    

