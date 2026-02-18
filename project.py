import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = "Expense.csv"


def add_expenses():
    amount = input("Amount: ").strip()
    if amount == "":
        print("Expense cannot be empty")
        return
    try: 
        amount = float(amount)
        if amount <= 0:
            print("number must be positive")
    except ValueError:
        print("invalid number")
        return

    cat = input("Category: ")
    if cat == "":
        cat = "Others"

    date_input = input("Date (YYYY-MM-DD, leave empty for today): ").strip()
    if date_input == "":
        expense_date = expense_date.today()
    else:
        try:
            expense_date = pd.to_datetime(date_input).date()
        except ValueError:
            print("Invalid date format")
            return   

        df = pd.DataFrame([[amount, cat, expense_date]],
        columns=["Amount","Category", "Date"])
    
    try:
        old = pd.read_csv(data)
        new = pd.concat([old, df], ignore_index=True)
        new.to_csv(data, index=False)
    except:
        df.to_csv(data, index=False)
    print("Expense Added!")

def show_expense():
    df = pd.read_csv(data)
    print(df)

def stats():
    df = pd.read_csv(data)

    total = np.sum(df["Amount"])
    average = np.mean(df["Amount"])
    highest = np.max(df["Amount"])

    print("Total Expense:", total)
    print("Average:", average)
    print("Highest Expense", highest)

def category_stats():
    df = pd.read_csv(data)

    print(df.groupby("Category")["Amount"].sum())

def piechart():
    df = pd.read_csv(data)
    group = df.groupby("Category")["Amount"].sum()

    plt.figure()
    plt.pie(group.values,labels=group.index,autopct="%1.1f%%")
    plt.title("Category Based Chart")
    # plt.ylabel("Expenses")
    # plt.xlabel("Category")
    plt.show()

def monthly_expenses():
    try:
        df = pd.read_csv(data, parse_dates=["Date"])
    except FileNotFoundError:
        print("No data found.")
        return

    if df.empty:
        print("No expenses to analyze.")
        return

    # Convert Date to monthly period (YYYY-MM)
    df["Month"] = df["Date"].dt.to_period("M")

    monthly_total = df.groupby("Month")["Amount"].sum()

    print("\n--- Monthly Expenses ---")
    print(monthly_total)


def menu():
    print("""
1 Add Expense
2 Show Expense
3 Show Stats
4 Show Category Stats
5 Show piechart
6 show monthly expenses
7 Exit""")
    return input("Choose Option: ")

while True:
    choose = menu()

    if choose == "1": add_expenses()
    elif choose == "2": show_expense()
    elif choose == "3": stats()
    elif choose == "4": category_stats()
    elif choose == "5": piechart()
    elif choose == "6": monthly_expenses()
    elif choose == "7":break
    else:
        print("Invalid Operation")

    
