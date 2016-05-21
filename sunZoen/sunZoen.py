# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""


from PyQt4 import QtGui, QtCore, Qt
import signIn, sqlopt, run

class loginWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(loginWindow, self).__init__(parent)
        self.setWindowTitle(u"??¼-SLcZone")
        self.setFixedSize(300, 280)
        self.setStyleSheet("background-color : white")
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        
        font = QtGui.QFont(u"΢???ź? Light", 10)

        self.logo = QtGui.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap('pics/logo.png'))
        self.logo.setGeometry(25, 10, 250, 124)
        
        self.username = QtGui.QLineEdit(self)
        self.username.setMaxLength(20)
        self.username.setGeometry(15, 140, 270, 30)
        self.username.setPlaceholderText(u"?û???")
        self.username.setFont(font)
        self.username.setAlignment(Qt.Qt.AlignCenter)
        
        self.psd = QtGui.QLineEdit(self)
        self.psd.setMaxLength(24)
        self.psd.setGeometry(15, 195, 270, 30)
        self.psd.setEchoMode(QtGui.QLineEdit.Password)
        self.psd.setContextMenuPolicy(Qt.Qt.NoContextMenu)
        self.psd.setPlaceholderText(u"????")
        self.psd.setFont(font)
        self.psd.setAlignment(Qt.Qt.AlignCenter)
        
        self.signin = QtGui.QPushButton(u"ע??", self)
        self.signin.setGeometry(15, 235, 105, 40)
        self.signin.setFlat(True)
        
        self.login = QtGui.QPushButton(u"??¼", self)
        self.login.setGeometry(180, 235, 105, 40)
        self.login.setFlat(True)
        self.login.setFocus()
        
        self.login.connect(self.login, QtCore.SIGNAL('clicked()'), self.loginF)
        self.signin.connect(self.signin, QtCore.SIGNAL('clicked()'), self.signinF)
    
    def loginF(self):
        name = str(self.username.text())
        psd = str(self.psd.text())
        flag = sqlopt.login(name, psd)
        if (flag == False):
            reply = QtGui.QMessageBox.question(self, u'??ʾ', u"?û?????????????", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
            	return
        else:
            self.run = run.runWindow(name, flag)
            self.run.show()
            self.close()     
        
    def signinF(self):
        self.zhuce = signIn.signIN(self.setNamePsd)
        self.zhuce.show()
    
    def setNamePsd(self, name, psd):
        self.username.setText(name)
        self.psd.setText(psd)
    