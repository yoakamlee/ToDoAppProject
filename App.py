while True:
    user_input = input("Select an option: add, show, edit, complete, or exit: ")
    user_input = user_input.strip().lower()

    if "add" in user_input:
        added_todo = user_input[4:]
        print(f"New Todo added: {added_todo}")

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        todos.append(added_todo)

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "show" in user_input:

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        striped_todos = [item.strip("\n").title() for item in todos]

        for index,item in enumerate(striped_todos):
            index = index + 1
            print(f"{index}: {item}")

    elif "edit" in user_input:
        num = int(user_input[5:])
        num = num - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        print(f"Todo chosen: {todos[num].strip("\n")}")
        todos[num] = input("Enter Todo: ").title() + "\n"

        with open("todos.txt", "w") as file:
            file.writelines(todos)

    elif "complete" in user_input:
        num = int(user_input[9:])
        num = num - 1

        with open("todos.txt", "r") as file:
            todos = file.readlines()

        print(f"Item selected is: {todos[num]}")
        todos.pop(num)

        with open("todos.txt","w") as file:
            file.writelines(todos)

        for item in todos:
            item = item.title().strip("\n")
            print(f"{item}")

    elif "exit" in user_input:
        break

    else:
        print(f"{user_input} unknown command!")

print("Todo app exited")