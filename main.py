""""
    simple budget tracker by Leon
"""

import os
import sys
import json
from datetime import datetime

def main():
    while True:
        os.system('clear')
        print("\t\t\t *** Simple Budget Tracker ***")

        print("\n 1.add Income")
        print(" 2.add Expense")
        print(" 3.view Transactions")
        print(" 4.view summary(total income, expense, balance)")
        print(" 5.exit\n")

        print("Choose action (use numbers).")
        choice = input()
        try:
            choice = int(choice)
        except:
            print("Not a value")

        match choice:
            case 1: addIncome()
            case 2: addExpense()
            case 3: viewTransactions()
            case 4: viewSummary()
            case 5: sys.exit()
            case _: 
                print("Invalid input( pick between 1 to 5)")
                choice = input('Go back? (yes/no)')
                if choice.lower() != 'yes':
                    sys.exit()
                
def addIncome():
    while True:
        os.system('clear')
        print("\t\t\t***Add Income***")
        
        print("Type: Income")

        #add category
        print("Choose category(use numbers):\n 1.home business \n 2.work business \n 3.part-time business")
        try:
            choice = int(input())
        except:
                addIncome()
        
        #based on choice categorize
        if choice == 1:
            category = 'Home Business'
        elif choice == 2:
            category = 'Work Business'
        elif choice == 3:
            category = 'Part-Time Business'
        else:
            print("Invalid choice(pick from 1 to 3)")
            choice = input("try again...(yes/no)")
            if choice != 'yes':
                main()
            else:
                addIncome()
 
        print(category)

        #add amount
        amount = float(input("Enter amount. \n"))

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

        print("Add another transaction? (yes/no)")
        choice = input()
        if choice != 'yes':
            break

def addExpense():
        while True:
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
            
            choice = input("add another expense (yes/no)")
            if choice.lower != 'yes':
                break

def viewTransactions():
    os.system('clear')
    print("\t\t\t***View Transactions\n")
    print("choose an action:\n 1.Income Transactions\n 2.Expenses\n 3.Totals and balance\n")

    try:
        choice = int(input())
        match choice:
            case 1: income() 
            case 2: expenses()
            case _: print("invalid input(choose between 1 to 2)")
    except:
        print("invalid input")
        print("try again...(yes/no)")
        ans = input()
        if ans != 'yes':
            goBack()
        else:
            viewTransactions()

#view transactions functions
def income():
    os.system('clear')
    print("\t\t\t*** show income ***")
    file_name = 'income.json'
    try:
        with open(file_name, 'r') as file:
            income_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    #load data from json file and print them out
    for i in income_data:
        print(f"Amount: {i['Amount']:8.2f}| Type: {i['Type']:6}| Category: {i['Category']:12}| Description: {i['Description']:}| Date/Time: {i['Date/Time']}|")

    goBack()

def expenses():
    os.system('clear')
    print("\t\t\t*** show expenses ***")
    file_name = 'expenses.json'
    try:
        with open(file_name, 'r') as file:
            expense_data = json.load(file)
    except FileNotFoundError:
        print("File does not exist")

    for i in expense_data:
        print(f"Amount: {i['amount']:8.2f}| Used for: {i['used for']}| Date/Time: {i['date-time']}|")

    goBack()

def viewSummary():
    os.system('clear')
    print("\t\t\t*** show summary ***")
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

    goBack()


#go back function
def goBack():
    print("\nGo back (yes/no)")
    ans = input()
    if ans.lower() != 'yes':
        sys.exit()
    else:
        main()

main()