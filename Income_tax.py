def calculate(amount, percent): 
    """Calculate the percentage of a given amount."""
    return (amount * percent) / 100

def calculate_income_tax(total_income: float) -> float: 
    """Calculate the income tax based on the total annual income."""
    if total_income <= 250000: 
        return 0
    elif total_income <= 500000: 
        return calculate(total_income - 250000, 5) 
    elif total_income <= 750000: 
        return calculate(total_income - 500000, 10) + 12500
    elif total_income <= 1000000: 
        return calculate(total_income - 750000, 15) + 37500
    elif total_income <= 1250000: 
        return calculate(total_income - 1000000, 20) + 75000
    elif total_income <= 1500000: 
        return calculate(total_income - 1250000, 25) + 125000
    else: 
        return calculate(total_income - 1500000, 30) + 187500

if __name__ == '__main__': 
    # Get user input for annual income
    total_income = float(input("What's your annual income?\n>>> ")) 
    
    # Calculate the income tax
    tax = calculate_income_tax(total_income) 
    
    # Print the total tax applicable
    print(f"Total tax applicable on ₹{total_income} is ₹{tax:.2f}")
