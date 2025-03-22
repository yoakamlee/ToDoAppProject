todos = ["Monster hunter", "tekken", "Path Of exile"]

todos.sort()

while True:
    user_input = input("Select an option: add, show, edit, complete, or exit: ")
    user_input.strip()

    match user_input:
        case "add":
            new_todo = input("Add a todo: ")
            print(f"New Todo added: {new_todo}")
            todos.append(new_todo)

        case "exit":
            break

print("Todo app exited")