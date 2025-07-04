import numpy as np
import json
import os

# Load personal data from external config file
config_file = 'personal_config.json'
if os.path.exists(config_file):
    with open(config_file, 'r') as f:
        config = json.load(f)
        print("Config loaded successfully")
    savings = config['savings']
    monthly_income = config['monthly_income']
    monthly_expenses = config['monthly_expenses']
    savings_interest_percentage = config['savings_interest_percentage']
    investment_returns_percentage = config['investment_returns_percentage']
else:
    # Fallback default values if config file doesn't exist
    print(f"Warning: {config_file} not found. Using default values.")
    savings = 10000
    monthly_income = 0
    monthly_expenses = 500
    savings_interest_percentage = 2
    investment_returns_percentage = 5

# simulate for how long it will take to reach 0
month = 0
while savings > 0:
    monthly_income_excluding_expenses = monthly_income - monthly_expenses
    savings += monthly_income_excluding_expenses
    monthly_interest_on_savings = savings * savings_interest_percentage / (100 * 12)
    monthly_investment_returns = savings * investment_returns_percentage / (100 * 12)
    monthly_savings_profit = monthly_interest_on_savings + monthly_investment_returns
    savings +=  monthly_savings_profit
    month += 1
    if savings <= 0:
        if month/12 < 1:
            print(f"You will run out of money in {month} months")
        else:
            years = month // 12
            months = month % 12
            if months == 0:
                print(f"You will run out of money in {years} years")
            else:
                print(f"You will run out of money in {years} years {months} months")
        break
    elif month == 12*10:
        print(f"You will have {savings} left in 10 years")
        break





