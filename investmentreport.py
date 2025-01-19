print("Welcome to the Investment Report Generator!")

initial_investment = float(input("Enter the initial investment amount: "))
annual_rate = float(input("Enter the annual interest rate (in %): "))
years = int(input("Enter the number of years for the investment: "))

annual_rate = annual_rate / 100

print("\nInvestment Details")
print("Initial Investment: $", initial_investment)
print("Annual Interest Rate: ", annual_rate * 100, "%")
print("Number of Years: ", years)

print("\nYear\tStarting Balance\tInterest Earned\tEnding Balance")

starting_balance = initial_investment

year = 1
while year <= years:
    interest_earned = starting_balance * annual_rate
    ending_balance = starting_balance + interest_earned
    print(f"{year}\t${starting_balance:.2f}\t\t${interest_earned:.2f}\t\t${ending_balance:.2f}")
    starting_balance = ending_balance
    year += 1

print("\nThank you for using the Investment Report Generator!")
