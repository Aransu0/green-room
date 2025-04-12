inventory = []


def start_game():
    print("You wake up in a locked room...")
    while True:
        print("\nWhat do you want to do?")
        print("1. Check the desk")
        print("2. Check the box")
        print("3. Try the door")
        choice = input("> ")
        match (choice):
            case "1":
                check_desk()
            case "2":
                check_box()
            case "3":
                if "key" in inventory:
                    print("You used the key and escaped! You win!")
                    break
                else:
                    print("The door is locked.")
            case _:
                print("Invalid choice.")


def check_desk():
    print("You find a small key in the drawer.")
    if "key" not in inventory:
        inventory.append("key")


def check_box():
    print("The box has a riddle: What has hands but can’t clap?")
    answer = input("Your answer: ").lower()
    if "clock" in answer:
        print("Correct! Inside the box is... a cookie. Yum.")
    else:
        print("Wrong answer. Try again later.")


start_game()
