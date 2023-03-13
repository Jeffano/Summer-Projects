import pyqrcode
import PySimpleGUI as sg

layout = [[sg.Text("Enter Link:"), sg.Text(size = (50,1))],
          [sg.Input(key = '-link-')],
          [sg.Text(size=(50,1), key='-output-')],
          [sg.Button('Generate')], [sg.Button("EXIT")]]

window = sg.Window('Qr Code Generator', layout, [100,250])

while True:
    event, values = window.read()

    if event == 'Generate':
        input_link = values['-link-']
        response = "QR Code Has Been Generated"
        url = pyqrcode.create(input_link)
        url.svg("qrcode.svg", scale=10)
        window['-output-'].update(response)

    if event == "EXIT" or event == sg.WIN_CLOSED:
        break

window.close()
