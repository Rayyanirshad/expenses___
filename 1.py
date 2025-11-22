# No libraries imported! We will use standard file handling and basic strings.

DATA_FILE = "expenses.txt"

def load_expenses():
    """
    Loads expenses from a simple text file.
    File format per line: date|category|description|amount
    """
    expenses = []
    try:
        # Try to open the file to read
        with open(DATA_FILE, "r") as file:
            for line in file:
                # Remove whitespace like enter keys
                line = line.strip() 
                if not line:
                    continue # Skip empty lines
                
                # Split the text by the symbol "|"
                parts = line.split("|")
                
                # We expect 4 parts. If not, skip this line to avoid errors
                if len(parts) == 4:
                    expense = {
                        "date": parts[0],
                        "category": parts[1],
                        "description": parts[2],
                        "amount": float(parts[3])
                    }
                    expenses.append(expense)
    except FileNotFoundError:
        # If file doesn't exist, just return an empty list
        return []
        
    return expenses

def save_expenses(expenses):
    """
    Saves the list of expenses to a text file.
    """
    with open(DATA_FILE, "w") as file:
        for item in expenses:
            # Create a string line: date|category|description|amount
            line = f"{item['date']}|{item['category']}|{item['description']}|{item['amount']}\n"
            file.write(line)

def add_expense(expenses):
    print("\n--- Add New Expense ---")
    
    # 1. Get Date manually since we removed datetime library
    date_entry = input("Enter the date (e.g., 2023-10-25): ").strip()
    if not date_entry:
        date_entry = "Unknown-Date"

    # 2. Get Description
    description = input("What did you buy?: ").strip()
    if not description:
        print("Description cannot be empty.")
        return

    # 3. Get Amount
    while True:
        try:
            amount_str = input("How much did it cost?: ")
            amount = float(amount_str)
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")

    # 4. Get Category
    category = input("Enter category (Food, Bills, etc): ").strip()
    if not category:
        category = "Uncategorized"

    # Add to list
    expense = {
        "date": date_entry,
        "description": description,
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses(expenses):
    print("\n--- Your Expenses ---")
    
    if not expenses:
        print("No expenses recorded yet.")
        return

    # Simple print layout without fancy libraries
    print("Date         | Category        | Description          | Amount")
    print("-" * 65)

    total_amount = 0

    for item in expenses:
        # We limit the length of strings so the table looks okay
        # .ljust(12) adds spaces to the right to make the column 12 chars wide
        d = item['date'][:12].ljust(12)
        c = item['category'][:15].ljust(15)
        desc = item['description'][:20].ljust(20)
        amt = item['amount']
        
        print(f"{d} | {c} | {desc} | ${amt:.2f}")
        total_amount += amt

    print("-" * 65)
    print(f"Total Spent: ${total_amount:.2f}")

def main():
    expenses = load_expenses()

    while True:
        print("\n=== EXPENSE TRACKER (No Libraries) ===")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Enter choice: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()