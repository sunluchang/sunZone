# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore, Qt
import sqlopt

class signIN(QtGui.QMainWindow):
    def __init__(self, setInfo, parent = None):
        super(signIN, self).__init__(parent)
        self.setWindowTitle(u"注册-SLcZone")
        self.setFixedSize(300, 300)
        self.setStyleSheet("background-color : white")
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        
        
        self.logo = QtGui.QLabel(self)
        self.logo.setPixmap(QtGui.QPixmap('pics/logo.png'))
        self.logo.setGeometry(25, -10, 250, 124)
        
        font = QtGui.QFont(u"微软雅黑", 10)
        self.setInfoForLog = setInfo
        
        self.name = QtGui.QLineEdit(self)
        self.psd = QtGui.QLineEdit(self)
        self.psd2 = QtGui.QLineEdit(self)
        self.name.setFont(font)
        self.psd.setFont(font)
        self.psd2.setFont(font)
        self.psd.setEchoMode(QtGui.QLineEdit.Password)
        self.psd2.setEchoMode(QtGui.QLineEdit.Password)
        self.name.setMaxLength(20)
        self.psd.setMaxLength(20)
        self.psd2.setMaxLength(20)
        
        self.name.setGeometry(10, 100, 280, 40)
        self.psd.setGeometry(10, 150, 280, 40)
        self.psd2.setGeometry(10, 200, 280, 40)
        
        self.name.setPlaceholderText(u"用户名 最多20位")
        self.psd.setPlaceholderText(u"密码 至少8位")
        self.psd2.setPlaceholderText(u"再次输入密码")
        self.name.setAlignment(Qt.Qt.AlignCenter)
        self.psd.setAlignment(Qt.Qt.AlignCenter)
        self.psd2.setAlignment(Qt.Qt.AlignCenter)
        
        self.ok = QtGui.QPushButton(u"注册", self)
        self.ok.setGeometry(10, 250, 135, 40)
        self.ok.setFlat(True)
        self.ok.setFont(font)
        
        self.cancel = QtGui.QPushButton(u"取消", self)
        self.cancel.setGeometry(155, 250, 135, 40)
        self.cancel.setFont(font)
        self.cancel.setFlat(True)
        self.cancel.setFocus()
        
        self.ok.connect(self.ok, QtCore.SIGNAL('clicked()'), self.save)
        self.cancel.connect(self.cancel, QtCore.SIGNAL('clicked()'), self.Quit)
        
    def save(self):
        name = self.name.text()
        psd = self.psd.text()
        psd2 = self.psd.text()
        if name == '' or psd != psd2:
            reply = QtGui.QMessageBox.question(self, u'提示', u"按要求输入正确的信息", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
            	return
             
        if(sqlopt.checkInfo(name) == False):
            reply = QtGui.QMessageBox.question(self, u"提示", u"已经存在此用户", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
            	return
        else:
            sqlopt.signinNew(name, psd) 
            
        self.close()
        self.setInfoForLog(name, psd)
    
    def Quit(self):
        self.close()
