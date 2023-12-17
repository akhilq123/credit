import PySimpleGUI as sg
import time

# Display a simple clock with Pysinmplegui

# GUI SETUP:

sg.theme('DarkTeal 7')  # Set Theme
fonts = ('Any', 30)

layout = [[sg.Text('Current Time is :',
                   size=(20, 2),
                   justification='center',
                   font=fonts)],
          [sg.Text('', size=(20, 2), font=fonts,
                   justification='center', key='timetext')],
          [sg.Exit(font=fonts, key='Exit')]]

window = sg.Window('Clock', layout, finalize=True)


window['timetext'].update(time.strftime('%H:%M:%S'))

# GUI MAIN LOOP :

while True:
    # GUI Button management
    event, values = window.read(timeout=10)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    # Update the time :
    # window['timetext'].update(time.strftime('%H:%M:%S'))

window.close()