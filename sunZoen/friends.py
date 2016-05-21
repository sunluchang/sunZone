# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""


from PyQt4 import QtGui, QtCore, Qt
import sqlopt, srcWindow, friendDetail

class friend():
    def __init__(self, ID, name, x, y, mom, hostid):
        self.ID = ID
        self.name = name
        self.hostid = hostid
        self.button = QtGui.QPushButton(mom)
        self.button.setText(self.name)
        self.button.setFont(QtGui.QFont(u"微软雅黑", 13))
        self.button.setGeometry(x, y, 345, 30)
        
        self.button.connect(self.button, QtCore.SIGNAL('clicked()'), self.showThat)
        
    def showThat(self):
        self.detail = friendDetail.friendDetail(self.ID, self.name, self.hostid)
        self.detail.show()
        
    def dis(self):
        self.button.show()
        
    
class friendWindow(QtGui.QMainWindow):
    def __init__(self, name, id, parent=None):
        super(friendWindow, self).__init__(parent)
        self.setWindowTitle(u"好友")
        self.setFixedSize(400, 600)
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        self.id = id
        self.name = name
        self.setFocus()
        self.numLabel = QtGui.QLabel(self)
        
        self.head = QtGui.QPushButton(self)
        self.head.setGeometry(10, 10, 85, 85)
        self.head.setEnabled(False)
        
        self.username = QtGui.QLabel(self)
        self.username.setGeometry(110, 10, 180, 25)
        
        self.search = QtGui.QLineEdit(self)
        self.search.setPlaceholderText("Search by Name")
        self.search.setGeometry(110, 70, 280, 24)
        self.search.setFont(QtGui.QFont(u"微软雅黑 Light", 9))
        self.search.setAlignment(Qt.Qt.AlignCenter)
        self.search.setMaxLength(20)
        
        self.add = QtGui.QPushButton(u"添加好友", self)
        self.cancel = QtGui.QPushButton(u"刷新", self)
        self.add.setGeometry(300, 10, 90, 25)
        self.cancel.setGeometry(300, 40, 90, 25)
        
        self.add.connect(self.add, QtCore.SIGNAL('clicked()'), self.addF)
        self.cancel.connect(self.cancel, QtCore.SIGNAL('clicked()'), self.shut)
        
    def addF(self):
        self.a = srcWindow.searchWindow(self.id)
        self.a.show()
    
    def shut(self):
        self.load()
        
    def load(self):
        self.scrollAreaWidgetContents = QtGui.QWidget(self)
        self.scrollAreaWidgetContents.setMinimumSize(360, 590)
        self.scrollAreaWidgetContents.setGeometry(10, 100, 390, 590)
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(10, 100, 390, 590))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameStyle(0)
        self.scrollArea.setStyleSheet("width:3")
        self.scrollArea.show()
        self.scrollAreaWidgetContents.show()
        
        self.username.setText(str(self.name).upper() + u" 的好友")
        self.username.setFont(QtGui.QFont(u"微软雅黑", 18))        
        length = 0
        enumLength = 39
        self.res = sqlopt.queryFriendsOf(self.id)
        
        self.numLabel.clear()
        self.numLabel = QtGui.QLabel(str(len(self.res)) + u"位", self)
        self.numLabel.setGeometry(110, 38, 100, 25)
        self.numLabel.setFont(QtGui.QFont(u"微软雅黑 Light", 15))
        self.numLabel.show()
        
        self.b = []
        for i in range(len(self.res)):
            self.b.append(friend(self.res[i][0], self.res[i][1], 35, i * 33 + 10, self.scrollAreaWidgetContents, self.id))
            self.b[i].dis()
            num = QtGui.QPushButton(str(i+1), self.scrollAreaWidgetContents)
            num.setGeometry(0, 10 + i * 33, 30, 30)
            num.show()
            num.setFont(QtGui.QFont(u"微软雅黑", 15))
            num.setFlat(True)
            num.setEnabled(False)
            length += enumLength
        self.scrollAreaWidgetContents.setMinimumSize(360, length)
    
    def keyPressEvent(self, event):
        if QtGui.QKeyEvent(event).key() == 16777220:
            name = self.search.text()
            if name:
                pass
            else:
                pass
                        
    