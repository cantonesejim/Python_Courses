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
        output_of_list = ""
        counter=0
        limit = len(countries) - 1
        while counter <= (limit):
            output_of_list = output_of_list + " on ".join(countries[counter]) + "\n"
            counter = counter + 1
        print("The Countries you have visited: \n" + output_of_list)
    else:
        print("INVALID")
    user_input = input("Enter 'a' to add another country, 'l' to list the countries you've visited, or 'q' to quit: ")