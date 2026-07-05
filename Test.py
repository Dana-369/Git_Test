hungry = input("Are you hungry? (yes/no) ")
if hungry.lower() == "yes":
    print("Let's get some food!")
    print("What type of food do you want? (pizza/sushi/burger)")
    print("You can choose from pizza, sushi, or burger.")
<<<<<<< HEAD

=======
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
>>>>>>> anime
else:
    print("Alright, maybe later.")
    print("What would you like to do instead? (read/watch/go for a walk)")