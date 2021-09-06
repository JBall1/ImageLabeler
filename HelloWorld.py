import os
import tkinter as tk
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

class NewprojectApp:
    def __init__(self, master=None):
        # build ui
        self.main_window = ttk.Frame(master)
        self.fm_main = ttk.Frame(self.main_window)
        self.fm_main.configure(height='400', relief='groove', width='800')
        self.fm_main.pack(side='top')
        self.main_window.configure(height='400', width='800')
        self.main_window.pack(side='top')

        # Main widget
        self.mainwindow = self.main_window
    

    def run(self):
        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    app = NewprojectApp(root)
    app.run()
