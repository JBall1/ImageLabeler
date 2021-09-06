import os
import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import pygubu

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_UI = os.path.join(PROJECT_PATH, "newproject")

folder_selected = None

class ImageLabeler:
    def __init__(self, master=None):
        # build ui
        self.main_window = ttk.Frame(master)
        self.fm_main = ttk.Frame(self.main_window)
        self.fm_main.configure(height='400', width='800')
        self.fm_main.pack(side='right')
        self.selectDir = ttk.Button(self.main_window, command= lambda: self.getDir())
        self.selectedDir = tk.StringVar(value='Select Directory')
        self.selectDir.configure(text='Select Directory', textvariable=self.selectedDir)
        self.selectDir.pack(padx='5', pady='5', side='left')
        self.separator44 = ttk.Separator(self.main_window)
        self.separator44.configure(orient='horizontal')
        self.separator44.pack(fill='y', side='top')
        self.main_window.configure(height='400', width='800')
        self.main_window.pack(side='top')
        self.main_window
        # Main widget
        self.mainwindow = self.main_window
    
    def getDir(self):
        """
        Prompts the user with a new window to select a directory(folder)
        returns the String of the directory selected
        """
        self.folder_selected = filedialog.askdirectory()
        return self.folder_selected

    def run(self):
        self.mainwindow.mainloop()




if __name__ == '__main__':
    root = tk.Tk()
    app = ImageLabeler(root)
    app.run()
    
