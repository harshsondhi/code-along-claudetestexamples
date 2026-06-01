TAX_RATE = None  # Set this once you know the tax rate (e.g., 0.08 for 8%)

def calculate_tax(amount):
    if TAX_RATE is None:
        raise ValueError("TAX_RATE has not been set.")
    return amount * TAX_RATE

def calculate_total(amount):
    tax = calculate_tax(amount)
    return amount + tax

if __name__ == "__main__":
    amount = float(input("Enter the amount: "))
    total = calculate_total(amount)
    print(f"Tax: {calculate_tax(amount)}")
    print(f"Total: {total}")
