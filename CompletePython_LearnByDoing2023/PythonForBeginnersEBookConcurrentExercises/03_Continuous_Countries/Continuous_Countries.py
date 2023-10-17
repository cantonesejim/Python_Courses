countries = []
print("Welcome to the countries app.")
print("You have visited 0 countries so far.")

user_input = input("Enter 'a' to add a country you've visited, or 'q' to quit: ")

while user_input != "q":
    if user_input == "a":
        user_country = input("Country name: ")
        countries.append(user_country)
        #Date visited: 
        print("You have added " + user_country + " to your list. You have visited " + str(len(countries)) +" countries.")
    elif user_input == "l":
        output_of_list = "\n".join(countries)
        print("The Countries you have visited: \n" + output_of_list)
    else:
        print("INVALID")
    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")