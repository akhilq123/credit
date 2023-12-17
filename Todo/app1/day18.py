import PySimpleGUI as sg
import layout

from modules import functions
import time
sg.theme("LightBlue2")

clock = sg.Text("",key= 'time1')
time1 = sg.Text("Clock",key='clock')
text1 = sg.Text("Type in a To-Do")
input1 = sg.InputText(tooltip="Enter a To-Do",key='todo')
todo_list = sg.Listbox(values=functions.get_todo()
                       ,key = 'todos'
                       ,enable_events=True
                       ,size=(40,10))
button1 = sg.Button("Add",image_source="/Users/akhilputhukkattuvinayan/Downloads/1649999-200.png")
button2 = sg.Button("Edit")
button3 = sg.Button("Complete")
button4 = sg.Button("Exit")

window = sg.Window("To Do List"
                   ,layout=[[time1,clock],[text1, input1,button1], [todo_list, button2, button3], [button4]]
                   ,font=('Helvetica',20))

while True :
    event,value = window.read(timeout=100)
    window["time1"].update(value=time.strftime("%A %B %d %Y,%H:%M:%S"))
    match event :
        case "Add" :
            content = functions.get_todo()
            content.append(value['todo'] + "\n")
            functions.write_todo(content)
            window['todos'].update(values=content)
        case "Edit" :
            try:
                content = functions.get_todo()
                index = content.index(value['todos'][0])
                content[index] = value['todo'] + "\n"
                functions.write_todo(content)
                window['todos'].update(values=content)
            except IndexError :
                sg.popup("Please select an item first",font=('Helvetica',20))
        case 'todos' :
            window['todo'].update(value=value['todos'][0])
        case 'Complete' :
            try:
                file_to_complete = value['todos'][0]
                content = functions.get_todo()
                index = content.index(value['todos'][0])
                content.remove(file_to_complete)
                functions.write_todo(content)
                window['todos'].update(values=content)
                window['todo'].update(value='')
            except IndexError :
                sg.popup("Please select an Item first",font=('Helvetica',20))
        case "Exit":
            break
        case sg.WINDOW_CLOSED :
            break
print("Bye")
window.close()