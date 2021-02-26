# %%
# importing GUI package program
import PySimpleGUI as sg

# style Buttons
bt = {'size': (10, 1), 'button_color': ('black', '#ECA527')}  # Style Text
bo = {'size': (10, 1), 'button_color': (
    'black', '#F1EABC')}  # Style Operators +-%/*
bn = {'size': (10, 1), 'button_color': (
    'black', '#F8F8F8')}  # Style Numbers (1-9)

# Define the window's contents
layout = [
    [sg.Text('', key='DISPLAY', size=(24, 1), font=('Digital 7', 20),
             background_color='black', text_color='white',)],
    [sg.Button(button_text='AC', key='-AC-', **bt),
     sg.Button(button_text='C', key='-C-', **bt),
     sg.Button(button_text='%', key='-PERCENTAGE-', **bo),
     sg.Button(button_text='÷', key='-DIVIDE-', **bo)],
    [sg.Button(button_text='7', key='-NUM-', **bn),
     sg.Button(button_text='8', key='-NUM-', **bn),
     sg.Button(button_text='9', key='-NUM-', **bn),
     sg.Button(button_text='x', key='-MULTIPLY-', **bo)],
    [sg.Button(button_text='4', key='-NUM-', **bn),
     sg.Button(button_text='5', key='-NUM-', **bn),
     sg.Button(button_text='6', key='-NUM-', **bn),
     sg.Button(button_text='-', key='-DIFFERENCE-', **bo)],
    [sg.Button(button_text='1', key='-NUM-', **bn),
     sg.Button(button_text='2', key='-NUM-', **bn),
     sg.Button(button_text='3', key='-NUM-', **bn),
     sg.Button(button_text='+', key='-SUM-', **bo)],
    [sg.Button(button_text='0', key='-NUM-', **bn),
     sg.Button(button_text='.', key='-DOT-', **bo),
     sg.Button(button_text='=', key='-EQUAL-', **bt),
     sg.Button(button_text='±', key='-±-', **bo)],
]


# Create the simple GUI main window of Calculator
# Add Calculator title, layout and enable keyboard events
window = sg.Window('Calculator', layout,
                   return_keyboard_events=True, finalize=True)

display = ''  # Store the inputed values from buttons

while True:

    event, values = window.read()
    # Check if user wants to quit by closing window
    if event == sg.WINDOW_CLOSED:
        break

    elif event in '0123456789':
        display = values['-DISPLAY-']
        display += event
        window.FindElement('DISPLAY').update(display)

# Finalize
window.close()


# %%
