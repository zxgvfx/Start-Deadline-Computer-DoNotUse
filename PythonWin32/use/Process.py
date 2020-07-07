import psutil
import win32api
import os,sys
import time

import tkinter as tk
from tkinter import filedialog
import pyautogui as pag


class Process:
    def __init__(self):
        self.allProcess = psutil.process_iter()
        self.procNameLiset = [i.name() for i in self.allProcess]

    #---------------deadline--------------------
    def isDeadlineslaveRun(self):
        return 'deadlineslave.exe' in self.procNameLiset

    #---------------houdini---------------------
    def __isMantraRun(self):
        return 'matra.exe' in self.procNameLiset
    def __isHythonRun(self):
        return 'hython.exe' in self.procNameLiset
    def __isIdialogRun(self):
        return 'idialog.exe' in self.procNameLiset

    def isHouUsed(self):
        return self.__isMantraRun() or self.__isHythonRun() or self.__isIdialogRun()

class Computer:

    def getCPUse(self):
        return psutil.cpu_percent(interval=1)
    def getMousePos(self):
        return pag.position()
    def getMemoryUse(self):
        return round(psutil.virtual_memory().used/1024/1024/1024,2)

class Deadline:
    def __init__(self,deadlinePath = 'C:/Program Files/Thinkbox/Deadline7/bin/deadlineslave.exe'):
        self.path = deadlinePath
        if not os.path.isfile(self.path):
            print('没有找到Deadline Slave')
            self.__open()
    def __open(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename()
        self.path = file_path
        
    def openSlave(self):
       win32api.ShellExecute(0, 'open', self.path, '', '', 1)



