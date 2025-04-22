import TodoFunction
import FreeSimpleGUI as Gui

label = Gui.Text("Enter a todo:")
text_box = Gui.InputText(tooltip="Enter todo:", key="todo")
add_button = Gui.Button("Add")

list_box = Gui.Listbox(values=TodoFunction.get_todos(),
                       key="items",
                       enable_events=True,
                       size=(45, 10))

edit_button = Gui.Button("Edit")

window = Gui.Window("Todo App", layout=[[label], [text_box, add_button], [list_box, edit_button]])

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["items"])

    match event:
        case "Add":
            todos = TodoFunction.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)

            TodoFunction.write_todos(todos)
            window["items"].update(values=todos)

        case "Edit":
            todo_to_edit = values["items"][0]
            new_todo = values["todo"] + "\n"

            todos = TodoFunction.get_todos()

            index = todos.index(todo_to_edit)
            todos[index] = new_todo

            TodoFunction.write_todos(todos)
            window["items"].update(values=todos)

        case "items":
            window["todo"].update(value=values["items"][0])

        case Gui.WIN_CLOSED:
            break

window.close()