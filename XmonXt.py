# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os
import subprocess

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow

from Ui_Xmon import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super().__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_btnGo_clicked(self):
        """
        Slot documentation goes here.
        """
       
        command = 'collectl'
        paramCount = int(self.txtRows.text())
        appParams = "-c" + str(paramCount)
        cliParams = self.txtCmd.text()
#        shellProcess = subprocess.Popen( ["ls","-lisa"], stdout = subprocess.PIPE )
        shellProcess = subprocess.Popen( [command, appParams,  cliParams], stdout = subprocess.PIPE )
        shellQ = shellProcess.stdout.readlines()
        print(type(shellQ[2]))
        shellText = shellQ[2].decode('utf-8')
#        shellText = str(shellQ[2]) + "\n"
        for shellRow in shellQ[3:len(shellQ)]:
#            Row = shellRow.splitlines()
#            Row = str(shellRow)
            print(shellRow.decode('utf-8'))
            self.listOutput.addItem(shellRow.decode('utf-8').strip())
            shellText += shellRow.decode('utf-8')
                    
        self.textOutput.setText(shellText)
      


