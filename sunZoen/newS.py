# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore, Qt
import sqlopt, time

class newState(QtGui.QMainWindow):
    def __init__(self, name, id, parent = None):
        super(newState, self).__init__(parent)
        self.setWindowTitle(u"发表新状态-SLcZone")
        self.setFixedSize(300, 300)
        self.setStyleSheet("background-color : white")
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
            
        font = QtGui.QFont(u"微软雅黑", 10)  
        self.id = id
        self.name = name
        
        self.edit = QtGui.QTextEdit(self)
        self.edit.setGeometry(10, 10, 280, 230)
        self.edit.setFont(font)
        
        self.ok = QtGui.QPushButton(u"发布", self)
        self.ok.setGeometry(10, 250, 135, 40)
        self.ok.setFlat(True)
        self.ok.setFont(font)
        self.cancel = QtGui.QPushButton(u"关闭", self)
        self.cancel.setGeometry(155, 250, 135, 40)
        self.cancel.setFont(font)
        self.cancel.setFlat(True)
        self.cancel.setFocus()
        
        self.ok.connect(self.ok, QtCore.SIGNAL('clicked()'), self.send)
        self.cancel.connect(self.cancel, QtCore.SIGNAL('clicked()'), self.Quit)
        
    def send(self):
        self.things = self.edit.toPlainText()
        self.date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        
        if (len(self.things) == 0):
            self.things = self.name + " @ " + self.date
            
        sqlopt.sendANewState(self.id, self.things, self.date)
        self.close()

    def Quit(self):
        self.close()
        
