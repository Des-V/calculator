# %%
# importing GUI package program
import PySimpleGUI as sg 

# Define the window's contents
layout = [
    [sg.Text(size=(27, 3),  background_color='black', text_color='white', key='-OUTPUT-')], 
    [sg.Button(size=(5, 1), button_text='AC',enable_events=True , key='-INPUT-'), 
    sg.Button(size=(5, 1), button_text='C',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='%',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='÷',enable_events=True , key='-INPUT-')],
    [sg.Button(size=(5, 1), button_text='7',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='8',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='9',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='x',enable_events=True , key='-INPUT-')],
    [sg.Button(size=(5, 1), button_text='4',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='5',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='6',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='-',enable_events=True , key='-INPUT-')],
    [sg.Button(size=(5, 1), button_text='1',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='2',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='3',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='+',enable_events=True , key='-INPUT-')],
    [sg.Button(size=(5, 1), button_text='0',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='.',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='=',enable_events=True , key='-INPUT-'),
    sg.Button(size=(5, 1), button_text='±',enable_events=True , key='-INPUT-')],
]


# Create the simple GUI main window of Calculator
# Add Calculator title 
window = sg.Window('Calculator', layout)

event, values = window.read() 

#event, values = sg.Window('Calculator', layout).read(close=True)
while True:
    # Check if user wants to quit by closing window
    if event == sg.WINDOW_CLOSED:
        break
    # Update 'output' text with 'input' value
    if event == '-INPUT-':
        window['-OUTPUT-'].update(values['-INPUT-'])

# Finalize 
window.close()


# %%
