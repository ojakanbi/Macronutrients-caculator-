# Macro enhancement
def user_name(name):  # function to get the username
    username = (name.strip().title())
    return username


def menu_options():  # function to show the different menu option
    menu_items = ['About', 'Macro', 'Exit']  # list of menu
    for count, items in enumerate(menu_items, start=1):  # for loop that counts and prints the items in the list
        print(f"Menu options {str(count)}: {str(items)}")


def title_menu(menu):  # function to make the first letter of a word capital
    return menu.title()


def about_menu(menu_option, items):  # function for the about menu option
    if menu_option == items[0]:
        print(f"This software is to help Calculate your macronutrients {user_name(get_name)}")


def break_down(user, calorie):  # function to calculate the calorie  breakdown in the macro menu
    return (user / 100) * calorie


def grams(down, grams_ca):  # function to calculate the grams in macro menu
    return down // grams_ca


def macro_menu(menu_option, menu_items):  # function for when the user chooses the macro menu
    while menu_option != 'Exit':  # loop to essentially loop out of the function
        if menu_option == menu_items[1]:
            calorie_intake = 0
            while calorie_intake < 800 or calorie_intake > 5000:  # user cannot select inbetween this range, or it prints error message
                calorie_intake = int(input(f"\t What is your desired calorie intake {user_name(get_name)}"))

                if (calorie_intake <= 800) or (
                        calorie_intake >= 5000):  # error message when it's not in the specified range
                    print("\tWe recommend your calorie should be less than 5000 and greater than 800, try again!")

                elif 800 < calorie_intake < 5000:  # when it falls within the range, it runs all code in the branch
                    print("Perfect " + user_name(
                        get_name) + " That's it! \n\tNow time to enter your desired calorie intake for each macronutrients.")
                    macro_nutrients = 0
                    while macro_nutrients != 100:  # loop to keep the user in this if macro nutrients does not equally 100
                        user_desired_fats = input("Please enter desired calories intake for fats:\n Ex| 20%: ")
                        user_desired_fats = user_desired_fats[0:2]  # if user decide to not put the percent
                        user_desired_fats = int(user_desired_fats)

                        user_desired_protein = input("Please enter desired calories intake for protein:\n Ex| 20%: ")
                        user_desired_protein = user_desired_protein[0:2]
                        user_desired_protein = int(user_desired_protein)

                        user_desired_carbs = input("Please enter desired calories intake for carbs:\n Ex| 20%:")
                        user_desired_carbs = user_desired_carbs[0:2]
                        user_desired_carbs = int(user_desired_carbs)

                        macro_nutrients = user_desired_fats + user_desired_protein + user_desired_carbs  # to add up to equal 100 to stop the while loop
                        if macro_nutrients != 100:  # to print an error message for percentage to be equal 100
                            print(f"Calorie percentage has to be fully equal to 100% {user_name(get_name)}, try again!")
                        else:
                            fats_breakdown = break_down(user_desired_fats, calorie_intake)
                            print("Fats breakdown:", fats_breakdown)

                            protein_breakdown = break_down(user_desired_protein, calorie_intake)
                            print("Protein breakdown:", protein_breakdown)

                            carbs_breakdown = break_down(user_desired_carbs, calorie_intake)
                            print("Carbs breakdown:", carbs_breakdown)

                            fats_grams = grams(fats_breakdown, 9)  # gets the grams for each macro nutrient
                            protein_grams = grams(protein_breakdown, 4)
                            carbs_grams = grams(carbs_breakdown, 4)

                            print("Fats Gram Allowance:", fats_grams, "per gram")
                            print("Protein Grams Allowance:", protein_grams, "per gram")
                            print("Carbs Gram Allowance:", carbs_grams, "per gram")

        menu_option = input("Exit or Macro")  # to see what the user want to do and essential get out of the function
        menu_option = menu_option.title()


def choice(menu_option, menu_items):  # function that holds the menu options functions to see what the user want
    while menu_option != menu_items[2]:  # will excute code below if it is not = to exit
        if menu_option == menu_items[0]:
            about_menu(menu_option, menu_items)
            menu_option = input("Exit or Macro: ")
            menu_option = menu_option.title()
        elif menu_option == menu_items[1]:
            macro_menu(menu_option, menu_items)
            menu_option = input("Are you sure you want to Exit out of Macro, say Exit: ")
            menu_option = menu_option.title()

    print(f"Thank you {user_name(get_name)}!, for using my software")  # leaving the function and the software


# what actual prints to the user
get_name = input("Hey, What is your full name:")
print(f"Welcome to Emlo Fitness Group - Macro Calculator {user_name(get_name)}")

print(f"Here are your Menu options {user_name(get_name)}")

menu_options()
menu_choice = input(f"Choose a menu option {user_name(get_name)} \n EX: 'About' \n Menu Option:")
menu_items = ['About', 'Macro', 'Exit']

choice(title_menu(menu_choice), menu_items)  # runs the calculator


# Automatic String Manipulation Utility

# Task 1.
def user_name(name):  # function to get the username
    username = (name.strip().title())
    return username


def get_user_input(userinput):  # function to get the string from the user
    global temp_user_input
    print(welcome_message)
    print("\nTo get started, input a string of your choice. \n"
          "EX: 'Hello world, I am Coding'"
          )
    ending_loop = 0
    while ending_loop == 0:  # loop to validate that the user is using at least 15 characters
        temp_user_input = str(input(userinput))
        if temp_user_input == "":  # if the user did not enter anything
            print("You did not enter anything, try again.")
        elif len(temp_user_input) < 15:  # code to make sure that the user enter at least 15 chr
            print("Make sure your string is at least 15 characters long, try again.")
        else:  # when all has been checked, then prints the users input
            print(f"Your string: {temp_user_input}")
            ending_loop += 1
            temp_user_input = temp_user_input.lower()

    return temp_user_input
