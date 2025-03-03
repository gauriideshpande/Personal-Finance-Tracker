from datetime import datetime

date_format = '%d-%m-%Y'
categories = {"I": "Income", "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_string, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Invalid date format. Please enter date in dd-mm-yyyy format.')
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount = float(input('Enter amount: '))
        if amount <= 0:
            raise ValueError('Amount cannot be negative or zero.')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for Incomeor 'E' for Expense): ").upper()
    if category in categories:
        return categories[category]
    
    print("Invalid Category. Please enter 'I' for Income or 'E' for Expense.")
    return get_category()

def get_description():
    return input('Enter description (optional): ')
