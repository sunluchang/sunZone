# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""


from PyQt4 import QtGui, QtCore, Qt
import time, alterInfo, newS, friends, sqlopt, stateW
        
class runWindow(QtGui.QMainWindow):
    def __init__(self, username, ID, parent = None):
        super(runWindow, self).__init__(parent)
        self.setWindowTitle(username + u"-SLcZone")
        self.setFixedSize(400, 720)
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        font = QtGui.QFont(u"微软雅黑", 12)
        
        self.id = ID
        self.name = username
        
        self.head = QtGui.QPushButton(self)
        self.head.setGeometry(10, 10, 80, 80)
        self.head.setEnabled(False)
        
        self.username = QtGui.QLabel(self)
        self.username.setGeometry(120, 10, 300, 25)
        self.username.setFont(font)
        self.setHello(username)
        
        self.newState = QtGui.QPushButton(u"发表新状态", self)
        self.newState.setGeometry(120, 50, 80, 40)
        
        self.friend = QtGui.QPushButton(u"我的好友", self)
        self.friend.setGeometry(210, 50, 80, 40)
        
        self.config = QtGui.QPushButton(u"修改资料", self)
        self.config.setGeometry(300, 50, 80, 40)
                
        self.button = QtGui.QPushButton(u"获取最新的动态", self)
        self.button.setGeometry(-1, 99, 402, 30)
        
        self.setDate()
        self.fresh()
        
        self.config.connect(self.config, QtCore.SIGNAL('clicked()'), self.setInfo)
        self.newState.connect(self.newState, QtCore.SIGNAL('clicked()'), self.sendNew)
        self.friend.connect(self.friend, QtCore.SIGNAL('clicked()'), self.showFriends)
        self.button.connect(self.button, QtCore.SIGNAL('clicked()'), self.fresh)
     
    def fresh(self):
        self.scrollAreaWidgetContents = QtGui.QWidget(self)
        self.scrollAreaWidgetContents.setMinimumSize(360, 590)
        self.scrollAreaWidgetContents.setGeometry(10, 130, 390, 560)
        #最大宽度 270
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(10, 130, 390, 560))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameStyle(0)
        self.scrollArea.setStyleSheet("width:3")
        
        self.scrollArea.show()
        self.scrollAreaWidgetContents.show()
        
        length = 10
        res = sqlopt.getNewStateFor(self.id)
        if (len(res) == 0):
            w = QtGui.QLabel(u"无动态", self.scrollAreaWidgetContents)
            w.setGeometry(100, 250, 190, 60)
            w.setFont(QtGui.QFont(u"微软雅黑", 30))
            w.setAlignment(Qt.Qt.AlignCenter)
            w.show()
        else:
            self.b = []
            for i in range(len(res)):
                #state.userid, stid, username, things, stdate
                #hostID, USERID, STID, x, y, name, date, things, mom
                self.b.append(stateW.stateWin(self.id, str(res[i][0]), str(res[i][1]), 0, length, str(res[i][2]), str(res[i][4]), str(res[i][3]), self.scrollAreaWidgetContents, self.name, 1))
                self.b[i].dis()            
                length += self.b[i].length
            
            self.scrollAreaWidgetContents.setMinimumSize(360, length)

    def showFriends(self):
        self.f = friends.friendWindow(self.name, self.id)
        self.f.load()
        self.f.show()
        
    def sendNew(self):
        self.new = newS.newState(self.name, self.id)
        self.new.show()
    
    def setInfo(self):
        self.infoWin = alterInfo.alterInfo(self.id, self.setNewName)
        self.infoWin.show()
        
    def setDate(self):
        self.today = QtGui.QLabel(self)
        self.today.setGeometry(300, 695, 95, 20)
        self.today.setText(u"今天 " + time.strftime('%Y-%m-%d', time.localtime(time.time())))
        self.today.setFont(QtGui.QFont(u"微软雅黑 Light", 9))
    
    def setHello(self, usrname):
        self.hour = int(time.strftime('%H',time.localtime(time.time())))
        self.date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.hello = ''
        
        if self.hour >=6 and self.hour <8:
            self.hello = u'， 早上好 ！  '
        elif self.hour>=8 and self.hour <12:
            self.hello = u'， 上午好 ！  '
        elif self.hour >=12 and self.hour <19:
            self.hello = u'， 下午好 ！  '
        else:
            self.hello = u'， 晚上好 ！  '
        self.username.setText(usrname + self.hello)
        
    def setNewName(self, name):
        self.name = name
        self.setWindowTitle(name + u"-SLcZone")
        self.setHello(name)
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = runWindow("sunluchang", 1)
    frm.show()
    sys.exit(app.exec_())