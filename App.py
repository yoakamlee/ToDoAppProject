todos = ["Monster hunter", "Tekken", "Path Of Exile"]

todos.sort()

while True:
    user_input = input("Select an option: add, show, edit, complete, or exit: ")
    user_input.strip().lower()

    match user_input:
        case "add":
            new_todo = input("Add a todo: ").title()
            print(f"New Todo added: {new_todo}")
            todos.append(new_todo)

        case "show":
            print(todos)

        case "exit":
            break

print("Todo app exited")