# Program #2: Movie Tix
# Write a program that has the user input various movie names and how many 
# tickets are desired for each movie.  
# At the end of the program it prints out the total number of tickets desired by the user.  
# Use either a "for loop" or "while loop" to accomplish this.

def main():
    ######################
total=0

number_of_movies=int(input("How many movies do you want to watch?:"))

for num in range(number_of_movies):
    movie=input(f"What is the name of movie #{num + 1}?: ")
    number_of_tickets=int(input(f"How many tickets to '{movie}' do you want?:"))
    total+=number_of_tickets


print(f"Total number of tickets requested: {total}")
    ######################


if __name__ == '__main__':
    main()
