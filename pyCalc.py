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
    [sg.Text('', key='-DISPLAY-', size=(24, 1), font=('Digital 7', 20),
             justification='right', background_color='black', text_color='white',)],
    [sg.Button('AC', **bt),
     sg.Button('C', **bt),
     sg.Button('%', **bo),
     sg.Button('/', **bo)],
    [sg.Button('7', **bn),
     sg.Button('8', **bn),
     sg.Button('9', **bn),
     sg.Button('*', **bo)],
    [sg.Button('4', **bn),
     sg.Button('5', **bn),
     sg.Button('6', **bn),
     sg.Button('-', **bo)],
    [sg.Button('1', **bn),
     sg.Button('2', **bn),
     sg.Button('3', **bn),
     sg.Button('+', **bo)],
    [sg.Button('0', **bn),
     sg.Button('.', **bo),
     sg.Button('=', **bt),
     sg.Button('±', **bo)],
]


# Create the simple GUI main window of Calculator
# Add Calculator title, layout and enable keyboard events
window = sg.Window('Calculator', layout,
                   return_keyboard_events=True, finalize=True)

# Update_display function format string input and update the window['-DISPLAY-'] in the layout


display = ''  # Store the inputed values from buttons

while True:

    event, values = window.read()
    print(event)  # Log the event

    # Check if user wants to quit by closing window
    if event == sg.WINDOW_CLOSED or event == None:
        break

    # Check if event happened in the following buttons
    if event in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '/', '*']:
        display += event
        if event not in ['+', '-', '/', '*']:
            window['-DISPLAY-'].update(event)

    elif event == '=':
        display = eval(display)
        window['-DISPLAY-'].update(display)

    elif event == 'AC':
        display = 0
        window['-DISPLAY-'].update(display)

# Finalize
window.close()

exit()
# %%
