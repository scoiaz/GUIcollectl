# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

import os
import subprocess

import pyqtgraph as pg
from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QMainWindow,  QGraphicsScene

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
            
            scene = QGraphicsScene()
            self.graphicsView.setScene(scene)
            self.plot_graph = pg.PlotWidget()
#            self.setCentralWidget(self.plot_graph)
            minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 30]
            plot_item = self.plot_graph.plot(minutes, temperature)
            proxy_widget = scene.addWidget(self.plot_graph)

      


