# The program asks the user for input N (positive integer) and reads it
# Then the program asks the user to provide N numbers (one by one) and reads all of them (again, one by one)
# In the end, the program asks the user for input X (integer) and outputs: "-1" if there were no such X among N read numbers, or the index (from 1 to N) of this X if the user inputed it before.

def module_4():
    N = int(input("Please enter a positive integer N: "))
    print(f"Your N is: {N}")

    numbers = []
    for i in range(N):
        num = int(input(f"Please enter number {i + 1}: "))
        numbers.append(num)
    for num in numbers:
        print(f"You entered number: {num}")

    X = int(input("Please enter an integer X: "))
    if X in numbers:
        index = numbers.index(X) + 1  # +1 to convert from 0-based to 1-based index
        print(f"The index of X is: {index}")
    else:
        print("-1")

if __name__ == "__main__":
    module_4()  