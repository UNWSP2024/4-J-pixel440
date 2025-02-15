# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
    difference = 0.0
    spent = 1.0         #initialize for while loop
    total = 0.0

    ######################
budget=float(input("How much would you like to budget for the month?:"))

total_expenses=0

while True:

    expense = float(input("Enter an expense (or enter 0 to finish): $"))

    if expense == 0:
        break


    total_expenses += expense

    balance = budget - total_expenses


if balance > 0:
    print(f"You are ${balance:.2f} under your budget.")
elif balance < 0:
    print(f"You are ${-balance:.2f} over your budget.")
else:
    print("You have met your budget exactly")
    ######################


if __name__ == '__main__':
    main()
