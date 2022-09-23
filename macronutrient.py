# EmLo Fitness Group - Marco Calculator

username = input("Hey, what is your first name:")  # get the username to input in the welcoming line
username = (username.strip().title())  # use strip to remove all the white spaces
print("Welcome to EmLo Fitness Group - Macro Calculator " + username)

print("Here are your Menu options " + username)
menu_items = ['About', 'Macro', 'Exit']  # list of menu items
for count, items in enumerate(menu_items, start=1):  # for loop that counts and prints the items in the list
    output = "Menu Option " + str(count) + ":" + str(items)
    print("\t", output)

print("\n")
menu_option = input(
    "Choose a menu option " + username + "\n EX:'About' \n Menu Option:")  # ask the user for menu option
menu_option = menu_option.title()  # automatically change the first letter of the menu option to cap as it is seen in
# list

while menu_option != menu_items[2]:  # loop to run when the user does not exit the software
    if menu_option == menu_items[0]:  # however, if they select about as an option
        print("This software is to help calculate your macronutrients " + username)

    if menu_option == menu_items[1]:  # however, if they select the macro as an option
        calorie_intake = 0
        while calorie_intake < 800 or calorie_intake > 5000:  # user cannot select inbetween this range, or it prints error message
            calorie_intake = int(input("\tWhat is your desired calorie intake " + username + ":"))

            if (calorie_intake < 800) or (calorie_intake > 5000):  # error message when it's not in the specified range
                print("\t \t We recommend your calorie should be less than 5000 and greater than 800, try again!")

            elif 800 < calorie_intake < 5000:  # when it falls within the range, it runs all code in the branch
                print(
                    "Perfect " + username + " That's it! \n\tNow time to enter your desired calorie intake for each macronutrients.")
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
                        print("Calorie percentage has to be fully equal to 100%, try again!")
                    else:
                        fats_breakdown = (user_desired_fats / 100) * calorie_intake
                        print("Fats breakdown:", fats_breakdown)
                        protein_breakdown = (user_desired_protein / 100) * calorie_intake
                        print("Protein breakdown:", protein_breakdown)
                        carbs_breakdown = (user_desired_carbs / 100) * calorie_intake
                        print("carbs breakdown:", carbs_breakdown)

                        fats_grams = fats_breakdown // 9   # gets the grams for each macro nutrient
                        protein_grams = protein_breakdown // 4
                        carbs_grams = carbs_breakdown // 4

                        print("Fats Gram Allowance:", fats_grams, "per gram")
                        print("Protein Grams Allowance:", protein_grams, "per gram")
                        print("Carbs Gram Allowance:", carbs_grams, "per gram")

    menu_option = input("Exit or Macro")
    menu_option = menu_option.title()

print("Thank you for using my software")
