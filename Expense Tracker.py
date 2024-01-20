import numpy as np
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

GROCERY = []
TRANSPORT = []
VEGETABLES = []
RENT = []
ELECTRICITY = []
COST = []
DATES = []
TIMES = []
EXPENSE_TYPE = []

def add_expense(grocery, transport, vegetables, rent, electricity, cost, date_time, expense_type):
    GROCERY.append(grocery)
    TRANSPORT.append(transport)
    VEGETABLES.append(vegetables)
    RENT.append(rent)
    ELECTRICITY.append(electricity)
    COST.append(cost)
    DATES.append(date_time.date())
    TIMES.append(date_time.time())
    EXPENSE_TYPE.append(expense_type)

while True:
    print("This is Household Expense Tracker:")
    print('1. Add GROCERY')
    print('2. Add TRANSPORT')
    print('3. Add VEGETABLES')
    print('4. Add RENT')
    print('5. Add ELECTRICITY')
    print('6. Show And Save The Household Expenses')
    print('0. Exit')

    choice = int(input('Choose the choice:\n'))
    print()

    if choice == 0:
        print("Exiting from the program")
        break
    elif choice in range(1, 6):
        expense_type = ""
        if choice == 1:
            print("Adding GROCERY")
            expense_type = "GROCERY"
        elif choice == 2:
            print("Adding TRANSPORT")
            expense_type = "TRANSPORT"
        elif choice == 3:
            print("Adding VEGETABLES")
            expense_type = "VEGETABLES"
        elif choice == 4:
            print("Adding RENT")
            expense_type = "RENT"
        elif choice == 5:
            print("Adding ELECTRICITY")
            expense_type = "ELECTRICITY"

        grocery = input(f'Enter the {expense_type}:\n')
        amount = int(input(f'Enter the {expense_type} amount:\n'))

        # Prompt for both date and time
        date_str = input('Enter the date (YYYY-MM-DD): ')
        time_str = input('Enter the time (HH:MM): ')
        
        # Convert date and time strings to datetime object
        date_time = datetime.strptime(date_str + ' ' + time_str, '%Y-%m-%d %H:%M')

        add_expense(grocery, 0, 0, 0, 0, amount, date_time, expense_type)

    elif choice == 6:
        # Create a new DataFrame for visualization
        visualization_data = pd.DataFrame({
            'Expense Type': EXPENSE_TYPE,
            'Cost': COST,
            'Date': DATES,
            'Time': TIMES
        })

        # Use Seaborn for visualization
        plt.figure(figsize=(10, 6))
        sns.barplot(x='Expense Type', y='Cost', data=visualization_data)
        plt.title('Household Expenses Visualization')
        plt.show()

        # Save the report as CSV
        expense_report = pd.DataFrame({
            'GROCERY': GROCERY,
            'TRANSPORT': TRANSPORT,
            'VEGETABLES': VEGETABLES,
            'RENT': RENT,
            'ELECTRICITY': ELECTRICITY,
            'COST': COST,
            'DATES': DATES,
            'TIMES': TIMES,
            'EXPENSE_TYPE': EXPENSE_TYPE
        })
        expense_report.to_csv('expense.csv', index=False)
        print(expense_report)

    else:
        print("You have chosen an incorrect option. Choose from 0 to 6 only.")

    print()
