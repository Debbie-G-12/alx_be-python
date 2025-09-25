if choice == '1':
    item = input("Enter item to add: ")
    shopping_list.append(item)

elif choice == '2':
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print(f"{item} not found in list.")
