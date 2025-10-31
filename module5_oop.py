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
        
    def process(self):
        print("Starting number processing...")
        self.initialize_n()
        self.initialize_numbers(self.number_size)
        self.find_number()
        print("Processing complete.")
    
    def __repr__(self):
        return f"NumberProcessor(numbers={self.numbers})"
    

