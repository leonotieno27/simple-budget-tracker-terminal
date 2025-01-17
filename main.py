""""
    simple budget tracker by Leon
"""

import os
import sys

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
    print("hello")

def addExpense():
    print("hello")

def viewTransactions():
    print("hello")

def viewSummary():
    print("hello")

main()