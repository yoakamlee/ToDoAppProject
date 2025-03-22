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
            for index,item in enumerate(todos):
                index = index + 1
                print(f"{index}: {item}")

        case "edit":
            num = int(input("Enter Item Number: "))
            num = num - 1
            print(f"Todo chosen: {todos[num]}")
            todos[num] = input("Enter Todo: ").title()

        case "complete":
            num = int(input("Enter Item Number: "))
            num = num - 1
            print(f"Item selected is: {todos[num]}")
            todos.pop(num)
            for item in todos:
                print(item)

        case "exit":
            break

print("Todo app exited")