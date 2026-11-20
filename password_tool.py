import os

FILE_NAME = "expenses.txt"

def load_expenses():
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                expenses.append({"category": category, "amount": float(amount)})
    return expenses

def save_expense(category, amount):
    with open(FILE_NAME, "a") as file:
        file.write(f"{category},{amount}\n")

def main():
    expenses = load_expenses()
    
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spent")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            category = input("Enter category (e.g., Food, Travel, Books): ").strip()
            try:
                amount = float(input("Enter amount (₹): "))
                expenses.append({"category": category, "amount": amount})
                save_expense(category, amount)
                print("Expense saved successfully!")
            except ValueError:
                print("Invalid amount. Please enter a number.")
                
        elif choice == "2":
            if not expenses:
                print("No expenses recorded yet.")
            else:
                print("\nRecorded Expenses:")
                for idx, item in enumerate(expenses, start=1):
                    print(f"{idx}. {item['category']} - ₹{item['amount']:.2f}")
                    
        elif choice == "3":
            total = sum(item["amount"] for item in expenses)
            print(f"\nTotal Amount Spent: ₹{total:.2f}")
            
        elif choice == "4":
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    main()
