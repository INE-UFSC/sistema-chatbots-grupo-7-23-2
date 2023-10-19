import PySimpleGUI as sg

layout = [
    [sg.Text('', size=(40, 1))],
    [sg.Text('', (88, 21), key='bot')],
    [sg.InputText(f'', key='user'), sg.Button('Enviar')]
]


class Interface:
    def __init__(self, title:str, layout: list, font: tuple):
        self.title = title
        self.layout = layout
        self.font = font
