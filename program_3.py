# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
total_rainfall=0
total_months=0

number_of_years=int(input("Enter the number of years:"))

for years in range(1, number_of_years + 1):
    print(f"Year {years}:")

    for months in range(1, 13):
        rainfall = float(input(f"Enter rainfall for month {months} (inches):"))

        total_rainfall+=rainfall
        total_months+=1

average=total_rainfall/total_months if total_months > 0 else 0


print(f"Number of months = {total_months}")
print(f"Total rainfall = {total_rainfall}inches")
print(f"Monthly average = { average:.2f} inches")
    ######################    


if __name__ == '__main__':
    main()
