# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore, Qt
import sqlopt, time, stateW, cmtClass

class cmtWindow(QtGui.QMainWindow):
    def __init__(self, hostid, stuserid, stid, things, date, name, hostname, parent = None):
        super(cmtWindow, self).__init__(parent)
        self.setWindowTitle(u"评论-SLcZone")
        self.setFixedSize(400, 600)
#        self.setStyleSheet("background-color : white")
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        
        self.hostid = hostid
        self.stuserid = stuserid
        self.stid = stid
        self.thingsForState = things
        self.dateForState = date
        self.nameForState = name
        self.hostname = hostname
        
        self.state = stateW.stateWin(self.hostid, self.stuserid, self.stid, 10, 10, self.nameForState, self.dateForState, self.thingsForState, self, self.hostname, 0)
        self.startHeight = self.state.length
        
        self.comment = QtGui.QTextEdit(self)
        self.comment.setGeometry(10, 550, 310, 40)
        self.comment.setFont(QtGui.QFont(u"微软雅黑 Light", 9))
        
        self.commit = QtGui.QPushButton(u'提交', self)
        self.commit.setGeometry(330, 550, 60, 40)
        self.commit.setFont(QtGui.QFont(u"微软雅黑 Light", 9))
        self.commit.setFlat(True)
        
        self.lineh = QtGui.QFrame(self)
        self.lineh.setGeometry(QtCore.QRect(-1, self.startHeight -25, 402, 2))
        self.lineh.setFrameShape(QtGui.QFrame.HLine)
        self.lineh.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(-1, 540, 402, 2))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        
        self.commit.connect(self.commit, QtCore.SIGNAL('clicked()'), self.addCMT)
        
        self.load()
        
    def load(self):
        self.scrollAreaWidgetContents = QtGui.QWidget(self)
        self.scrollAreaWidgetContents.setMinimumSize(360, 530 - self.startHeight)
        self.scrollAreaWidgetContents.setGeometry(10, self.startHeight, 390, 590 - self.startHeight)
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(10, self.startHeight, 390, 530 - self.startHeight))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameStyle(0)
        self.scrollArea.setStyleSheet("width:3")
        self.scrollArea.show()
        self.scrollAreaWidgetContents.show()
        
        cmt = []
        height  = 5
        #username, things, cmdate
        res = sqlopt.getCmtForState(self.stuserid, self.stid)
        for i in range(len(res)):
            cmt.append(cmtClass.stateWin(str(res[i][0]), str(res[i][2]), str(res[i][1]), 5, height, self.scrollAreaWidgetContents))
            cmt[i].dis()
            height += cmt[i].height
            
        self.scrollAreaWidgetContents.setMinimumSize(360, height + 5)
    
    def addCMT(self):
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        newC = self.comment.toPlainText()
        
        if newC == "" or newC == " ":
            reply = QtGui.QMessageBox.question(self, u'提示', u"内容不能为空", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                return
                
        sqlopt.addCommentFor(self.stuserid, self.stid, self.hostid, newC, str(date))

        self.comment.setText("")
        self.load()
    