import PySimpleGUI as sg
import os

DEFAULT_TITLE = "Google Photos Export Fixer"
DEFAULT_MESSAGE = "Choose a folder containing the export data (json) and images (jpg): "
DEFAULT_SUBMIT = "Submit"
DEFAULT_X = 1000
DEFAULT_Y = 300
DIR_KEY = "DIR"
INVALID_INPUT = "Please select a valid directory/folder containing the json and jpg files.."


class MainWindow:
    def __init__(self, title=DEFAULT_TITLE, message=DEFAULT_MESSAGE, submit_button=DEFAULT_SUBMIT, x_size=DEFAULT_X, y_size=DEFAULT_Y, invalid_input=INVALID_INPUT):
        self._window = None
        self._title = title
        self._message = message
        self._submit_button = submit_button
        self._x_size = x_size
        self._y_size = y_size
        self._invalid_input = invalid_input

    def start(self):
        layout = [[sg.Text(self._title)], [sg.Text(self._message), sg.Input(
        ), sg.FolderBrowse(key=DIR_KEY)], [sg.Button(self._submit_button)]]

        self._window = sg.Window(
            self._title, layout, size=(self._x_size, self._y_size))

        self._run_loop()

    def _run_loop(self):
        while True:
            event, values = self._window.read()
            print(event)
            print(values)
            if event == "Close" or event == sg.WIN_CLOSED:
                break
            if event == self._submit_button:
                if self._verify_path(values):
                    break  # TODO: start the actual work!
                else:
                    sg.Popup(self._invalid_input, title="Error")
        self._window.close()

    def _verify_path(self, value):
        curr_dir = value[DIR_KEY]
        if not os.path.isdir(curr_dir):
            # not really necessary since simple gui handles this for us, but just in case I guess
            return False
        if not os.listdir(curr_dir):
            return False
        return True


if __name__ == "__main__":
    window = MainWindow(title="TEST")
    window.start()
