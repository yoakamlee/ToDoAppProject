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