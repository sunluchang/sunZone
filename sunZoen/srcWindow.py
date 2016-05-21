# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore, Qt
import sqlopt

class searchWindow(QtGui.QMainWindow):
    def __init__(self, hid, parent=None):
        super(searchWindow, self).__init__(parent)
        self.setWindowTitle(u"搜索-SLcZone")
        self.setFixedSize(300, 100)
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        
        font = QtGui.QFont(u"微软雅黑 Light", 12)
        self.hid = hid
        
        self.a = QtGui.QPushButton("+", self)
        self.a.setGeometry(215, 50, 75, 40)
        self.a.setEnabled(False)
        self.a.setFont(QtGui.QFont(u"微软雅黑 Light", 20))
        self.b = QtGui.QPushButton("SEARCH", self)
        self.b.setGeometry(9, 50, 202, 40)
        self.b.setFont(QtGui.QFont(u"微软雅黑 Light", 17))
        self.b.setEnabled(False)
                
        self.text = QtGui.QLineEdit(self)
        self.text.setPlaceholderText(' By Name')
        self.text.setGeometry(10, 10, 200, 30)
        self.text.setFont(font)
        self.text.setAlignment(Qt.Qt.AlignCenter)
        
        self.search = QtGui.QPushButton(u"搜索", self)
        self.search.setGeometry(215, 10, 75, 30)
        self.search.setFont(font)
        self.search.setFlat(True)
        self.search.setFocus()
        self.search.setDefault(True)
        
        self.search.connect(self.search, QtCore.SIGNAL('clicked()'), self.sF)
        self.a.connect(self.a, QtCore.SIGNAL('clicked()'), self.ok)
        
    def sF(self):
        self.name = ''
        self.id = 0
        name = str(self.text.text())
        res = sqlopt.searchName(name)
        if (res == False):
            reply = QtGui.QMessageBox.question(self, u'提示', u"没有此用户！", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.text.clear()
                self.a.setDisabled(True)
        else:
            self.text.clear()
            self.name = str(res[0][1])
            self.id = str(res[0][0])
            self.a.setEnabled(True)
            self.b.setText(str(res[0][1]))
            self.b.show()
            self.a.show()
        
        
    def ok(self):
        if int(self.hid) != int(self.id):
            if(sqlopt.addFriendFor(self.hid, self.id)):
                reply = QtGui.QMessageBox.question(self, u'提示', u"添加成功！", QtGui.QMessageBox.Yes)
                if reply == QtGui.QMessageBox.Yes:
                    self.a.setEnabled(False)
            else:
                reply = QtGui.QMessageBox.question(self, u'提示', u"您已经拥有该好友！", QtGui.QMessageBox.Yes)
                if reply == QtGui.QMessageBox.Yes:
                    self.a.setEnabled(False)
        else:
            reply = QtGui.QMessageBox.question(self, u'提示', u"您一直都是自己的好友", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.a.setEnabled(False)
        