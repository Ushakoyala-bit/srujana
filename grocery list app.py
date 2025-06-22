grocery_list = []

while True:
    print("\noptions: add / remove / show / exit")
    action = input("what would you like to do? ")

    if action == "add":
        item = input("enter item to add: ")
        grocery_list.append(item)
        print(f"{item} added")

    elif action == "remove":
        item = input("enter item to remove: ")
        if item in grocery_list:
            grocery_list.remove(item)
            print(f"{item} removed")
        else:
            print("item not found")

    elif action == "show":
        print("your grocery list:")
        for item in grocery_list:
            print(f"- {item}")

    elif action == "exit":
        break

    else:
        print("invalid option")