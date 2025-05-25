#Finding the factorial of a number

def main():
    factorial(5)

def factorial(n):
    a = 1
    for i in range(1, n+1):
        a *= i
    print(f"The factorial of {n} is: {a}")

main()