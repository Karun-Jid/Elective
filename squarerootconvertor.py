def square_root(number):
    if number < 0:
        return "Square root of negative numbers is not real."
    guess = number / 2.0
    for _ in range(20):
        guess = (guess + number / guess) / 2.0
    return guess

if __name__ == "__main__":
    num = float(input("Enter a number to find its square root: "))
    result = square_root(num)
    print(f"The square root of {num} is approximately {result:.2f}")
