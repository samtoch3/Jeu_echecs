import PySimpleGUI as sg


layout1 = [
    [sg.Text('JEU D\'ECHECS', font='Arial 12', text_color='white', background_color='blue')],
    [sg.Image(r'chess.png', background_color='blue', size=(970, 600))],
    [sg.Button('Start', key='_START_')]
]

# Create the Window
window = sg.Window('Jeu d\'echecs', layout1, font=("Helvetica", 14), size=(970, 700), element_justification='c', background_color='blue')
window.set_icon('chess.ico')

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    if event == '_START_':
        print('Commencez à jouer !')