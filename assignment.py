def main():
    factorial(5)
    handle_errors()

#Finding the factorial of a number
def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    print(f"The factorial of {n} is: {a}")

#Handling errors
def handle_errors():
    try:
        x = int(input("Enter a number\n"))
        # if not type(x) is int:
        #     raise ValueError("X should be an integer")
    except ValueError:
        print("X should be an integer")
    else:
        print(f"The value {x} is an integer")

main()