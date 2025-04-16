import TodoFunction
import FreeSimpleGUI as Gui

label = Gui.Text("Enter a todo:")
text_box = Gui.InputText(tooltip="Enter todo:")
add_button = Gui.Button("Add")

window = Gui.Window("Todo App", layout=[[label, text_box, add_button]])
window.read()
window.close()