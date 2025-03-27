
while True:
    user_input = input("Select an option: add, show, edit, complete, or exit: ")
    user_input = user_input.strip().lower()

    match user_input:
        case "add":
            added_todo = input("Add a todo: ").title() + "\n"
            print(f"New Todo added: {added_todo}")

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            todos.append(added_todo)

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "show":

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            edited_todos = [item.strip("\n").title() for item in todos]

            for index,item in enumerate(edited_todos):
                index = index + 1
                print(f"{index}: {item}")

        case "edit":
            num = int(input("Enter Item Number: "))
            num = num - 1

            with open("todos.txt", "r") as file:
                todos = file.readlines()

            print(f"Todo chosen: {todos[num].strip("\n")}")
            todos[num] = input("Enter Todo: ").title() + "\n"

            with open("todos.txt", "w") as file:
                file.writelines(todos)

        case "complete":
            num = int(input("Enter Item Number: "))
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

        case "exit":
            break

print("Todo app exited")