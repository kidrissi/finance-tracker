from datetime import datetime

date_format = "%d-%m-%Y"


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(date_format)
    try:
        valid_date = datetime.strptime(date_str, date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print("invalid date format . Please enter date dd-mm-YYYY format!")
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("The amount must be positive and no-zero")
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    pass


def get_description():
    pass
