import PySimpleGUI as sg

layout = [[sg.Text("Google Photos Export Fixer")], [sg.Text("Choose a folder contaning the export data (json) and images (jpg): "), sg.Input(), sg.FileBrowse()]]

# Create the window
window = sg.Window("Export Fixer", layout, size=(600,150))

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Close" or event == sg.WIN_CLOSED:
        break


window.close()
