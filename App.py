def get_todos(filepath="todos.txt"):
    """Reads a text file from the filepath passed to it"""
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_args, filepath="todos.txt"):
    """Writes to a text file from the file path passed
    to it, also takes in a list of items
    """
    with open(filepath, "w") as file_local:
        file_local.writelines(todos_args)


while True:
    user_input = input("Select an option: add, show, edit, complete, or exit: ")
    user_input = user_input.strip().lower()

    if user_input.startswith("add"):
        added_todo = user_input[4:]
        print(f"New Todo added: {added_todo}")

        todos = get_todos()

        todos.append(added_todo + "\n")

        write_todos(todos)

    elif user_input.startswith("show"):

        todos = get_todos()

        striped_todos = [item.strip("\n").title() for item in todos]

        for index,item in enumerate(striped_todos):
            index = index + 1
            print(f"{index}: {item}")

    elif user_input.startswith("edit"):
        try:
            num = int(user_input[5:])
            num = num - 1

            todos = get_todos()

            print(f"Todo chosen: {todos[num].strip("\n")}")
            todos[num] = input("Enter Todo: ").title() + "\n"

            write_todos(todos)

        except ValueError:
            print("Unknown Command! Invalid Value")
            continue

        except IndexError:
            print("Unknown Command! not within range of the current list!")
            continue

    elif user_input.startswith("complete"):
        try:
            num = int(user_input[9:])
            num = num - 1

            todos = get_todos()

            print(f"Item selected is: {todos[num]}")
            todos.pop(num)

            write_todos(todos)

            for item in todos:
                item = item.title().strip("\n")
                print(f"{item}")

        except IndexError:
            print("Unknown Command! not within range of the current list!")
            continue

        except ValueError:
            print("Unknown Command! not within range of the current list!")
            continue

    elif user_input.startswith('exit'):
        break

    else:
        print(f"{user_input} unknown command!")

print("Todo app exited")