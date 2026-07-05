hungry = input("Are you hungry? (yes/no) ")
if hungry.lower() == "yes":
    print("Let's get some food!")
    print("What type of food do you want? (pizza/sushi/burger)")
    print("You can choose from pizza, sushi, or burger.")
    print("Please enter your choice:")
    choice = input().lower()
    if choice == "pizza":
        print("You chose pizza!")
    elif choice == "sushi":
        print("You chose sushi!")
    elif choice == "burger":
        print("You chose burger!")
    else:
        print("Invalid choice.")
else:
    print("Alright, maybe later.")