#this code suckssss
# Expense Tracker Application

from datetime import datetime, timedelta

expenses = []
categories = set()

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    amount = input("Enter expense amount: ")
    category = input("Enter expense category: ")
    description = input("Enter expense description: ")
    
    expense = f"{date}|{amount}|{category}|{description}"
    expenses.append(expense)
    categories.add(category)
    print("Expense added successfully!")

def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return
    
    for expense in expenses:
        date, amount, category, description = expense.split('|')
        print(f"Date: {date}, Amount: ${amount}, Category: {category}, Description: {description}")

def generate_report():
    if not expenses:
        print("No expenses recorded.")
        return
    
    report_type = input("Enter report type (weekly/monthly): ").lower()
    end_date = datetime.now()
    
    if report_type == 'weekly':
        start_date = end_date - timedelta(days=7)
    elif report_type == 'monthly':
        start_date = end_date - timedelta(days=30)
    else:
        print("Invalid report type. Please enter 'weekly' or 'monthly'.")
        return
    
    total_spending = 0
    category_spending = {}
    
    for expense in expenses:
        date, amount, category, _ = expense.split('|')
        expense_date = datetime.strptime(date, "%Y-%m-%d")
        
        if start_date <= expense_date <= end_date:
            amount = float(amount)
            total_spending += amount
            category_spending[category] = category_spending.get(category, 0) + amount
    
    print(f"\n{report_type.capitalize()} Spending Report:")
    print(f"Total Spending: ${total_spending:.2f}")
    print("\nSpending by Category:")
    for category, amount in category_spending.items():
        print(f"{category}: ${amount:.2f}")

def visualize_trends():
    if not expenses:
        print("No expenses recorded.")
        return
    
    print("Spending Trends (Last 7 days):")
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)
    
    daily_spending = {(start_date + timedelta(days=i)).strftime("%Y-%m-%d"): 0 for i in range(8)}
    
    for expense in expenses:
        date, amount, _, _ = expense.split('|')
        expense_date = datetime.strptime(date, "%Y-%m-%d")
        
        if start_date <= expense_date <= end_date:
            daily_spending[date] += float(amount)
    
    for date, amount in daily_spending.items():
        bar = '#' * int(amount / 10)  # Scale the bar
        print(f"{date}: {bar} ${amount:.2f}")

def save_expenses():
    filename = input("Enter filename to save expenses (e.g., expenses.txt): ")
    with open(filename, 'w') as f:
        for expense in expenses:
            f.write(expense + '\n')
    print(f"Expenses saved to {filename}")

def load_expenses():
    global expenses, categories
    filename = input("Enter filename to load expenses from: ")
    try:
        with open(filename, 'r') as f:
            expenses = [line.strip() for line in f.readlines()]
        categories = set(expense.split('|')[2] for expense in expenses)
        print(f"Expenses loaded from {filename}")
    except FileNotFoundError:
        print("File not found.")

def main_menu():
    while True:
        print("\n--- Expense Tracker Application ---")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Generate spending report")
        print("4. Visualize spending trends")
        print("5. Save expenses to file")
        print("6. Load expenses from file")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            visualize_trends()
        elif choice == '5':
            save_expenses()
        elif choice == '6':
            load_expenses()
        elif choice == '7':
            print("Thank you for using the Expense Tracker Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()