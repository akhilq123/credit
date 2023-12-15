import modules.functions

import PySimpleGUI as sg
label = sg.Text("Type in a TO-Do ")
input_box = sg.InputText(tooltip="Enter a To Do")
add = sg.Button("Add")

window = sg.Window('My To', layout=[[label,input_box,add]])
window.read()
window.close()
