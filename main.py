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
    file_name = 'data.json'
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
    print("hello")

def viewTransactions():
    print("hello")

def viewSummary():
    print("hello")

main()