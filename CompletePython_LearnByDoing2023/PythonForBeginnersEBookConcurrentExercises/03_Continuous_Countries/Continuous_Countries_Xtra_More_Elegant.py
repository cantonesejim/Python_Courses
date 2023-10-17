countries = []
print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, or 'q' to quit: ")

while user_input != "q":
    if user_input == "a":
        user_country = input("Country name: ")
        user_date = input("Date visited: ")
        total_input = [user_country, user_date]
        countries.append(total_input)
        print("You have added " + user_country + " to your list. You have visited " + str(len(countries)) +" countries.")
    elif user_input == "l":
        print("The Countries you have visited: \n")
        for data in countries:
            print(f" {data[0]} on {data[1]} \n")
    else:
        print("INVALID SELECTION")
    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")