import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Progress

DEFAULT_TITLE = "Progress"

# is there an interface future? probably not worth it rn


class ProgressWindow:
    def __init__(self, max_value, title=DEFAULT_TITLE):
        self._progress_bar = None
        self._title = title
        self._max_value = max_value
        self._curr_progress = 0

    def start(self):
        layout = [[sg.Text(self._title)],
                  [sg.ProgressBar(max_value=self._max_value, orientation='h', size=(20, 20), key='progress')]]

        window = sg.Window(self._title, layout, finalize=True)

        self._progress_bar = window["progress"]

    def add_progress(self):
        self._curr_progress += 1
        self._progress_bar.update_bar(self._curr_progress)

    # def _run_loop(self):
    #     while True:
    #         event, values = self._window.read()
    #         print(event)
    #         print(values)
    #         if event == "Close" or event == sg.WIN_CLOSED:
    #             break
    #         if event == self._submit_button:
    #             if self._verify_path(values):
    #                 break  # TODO: start the actual work!
    #             else:
    #                 sg.Popup(self._invalid_input, title="Error")
    #     self._window.close()


if __name__ == "__main__":
    from time import sleep
    window = ProgressWindow(10)
    window.start()
    for i in range(0, 10):
        window.add_progress()
        sleep(1)