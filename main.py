""""
    simple budget tracker by Leon
"""

import os
import sys
import json
from datetime import datetime

def main():
    os.system('clear')
    print("\t\t\t *** Simple Budget Tracker ***")

    print("\n 1.add Income")
    print(" 2.add Expense")
    print(" 3.view Transactions")
    print(" 4.view summary(total income, expense, balance)")
    print(" 5.exit\n")

    print("Choose action (use numbers).")
    choice = input()
    choice = int(choice)

    match choice:
        case 1: addIncome()
        case 2: addExpense()
        case 3: viewTransactions()
        case 4: viewSummary()
        case 5: sys.exit()
        case _: print("Invalid input( pick between 1 to 5)")


def addIncome():
    os.system('clear')
    print("\t\t\tAdd Income")

    #add amount
    amount = float(input("Enter amount. \n"))

    #print to confirm amount
    print(amount)
    print("Type: Income")

    #add category
    print("Choose category(use numbers):\n 1.home business \n 2.work business \n 3.part-time business")
    choice = int(input())
    
    #based on choice categorize
    if choice == 1:
        category = 'Home Business'
    elif choice == 2:
        category = 'Work Business'
    elif choice == 3:
        category = 'Part-Time Business'
    
    print(category)

    #add  description
    print("Add description about the transaction:")
    description = input()

    #adding time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    new_data = {'Amount':amount,'Type':'Income','Category': category, 'Description':description, 'Date/Time': date_time}
   
   #add data to file
    file_name = 'income.json'
    try:
        with open(file_name,"r") as file:
            try:
                list_data = json.load(file)
            except json.JSONDecodeError:
                list_data = []
    except FileNotFoundError:
        list_data = []

    list_data.append(new_data)
    with open(file_name, 'w') as file:
        json.dump(list_data, file, indent=5)


def addExpense():
    os.system('clear')
    print("\t\t\t***Add Expense")

    print("What did you use the money for: ")
    ans = input()
    print("amount used: ")
    amount = int(input())

    #adding time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    new_data = {'amount': amount, 'used for':ans, 'date-time':date_time}

    #add data to file
    file_name = 'expenses.json'
    try:
        with open(file_name,"r") as file:
            try:
                list_data = json.load(file)
            except json.JSONDecodeError:
                list_data = []
    except FileNotFoundError:
        list_data = []

    list_data.append(new_data)
    with open(file_name, 'w') as file:
        json.dump(list_data, file, indent=5)

def viewTransactions():
    os.system('clear')
    print("\t\t\t***View Transactions\n")
    print("choose an action:\n 1.Income Transactions\n 2.Expenses\n 3.Totals and balance\n")

    choice = int(input())
    match choice:
        case 1: income()
        case 2: expenses()
        case 3: totalsAndBalance()
        case _: print("invalid input(choose between 1 to 3)")

#view summary
def viewSummary():
    print("hello")

#view transactions functions
def income():
    file_name = 'income.json'
    try:
        with open(file_name, 'r') as file:
            income_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    #load data from json file and print them out
    for i in income_data:
        print(f"Amount: {i['Amount']:8.2f}| Type: {i['Type']:6}| Category: {i['Category']:12}| Description: {i['Description']:}| Date/Time: {i['Date/Time']}|")

def expenses():
    file_name = 'expenses.json'
    try:
        with open(file_name, 'r') as file:
            expense_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    for i in expense_data:
        print(f"Amount: {i['amount']:8.2f}| Used for: {i['used for']}| Date/Time: {i['date-time']}|")

def totalsAndBalance():
    #income data file load
    file_name = 'income.json'
    try:
        with open(file_name, 'r') as file:
            income_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    #expenses file load
    file_name = 'expenses.json'
    try:
        with open(file_name, 'r') as file:
            expenses_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    #Total Income
    amount = 0
    for i in income_data:
        amount += i['Amount']
    print(f"Total Income is: {amount}")

    #Total Expenses
    expenses = 0
    for i in expenses_data:
        expenses += i['amount']
    print(f'Total Expense is: {expenses}')

    #Balances Income-expense
    balance = amount - expenses
    if balance < 0:
        print(f"You have a debt of: {balance}")
    elif balance == 0:
        print(f"You have no balance")
    else:
        print(f"You have a balance of: {balance}")

main()