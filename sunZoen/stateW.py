# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore
import sqlopt, cmtWindow

class stateWin():
    def __init__(self, HOSTID, USERID, STID, x, y, name, date, things, mom, hostname, flag):
        self.hostid = HOSTID
        self.stuserid = USERID
        self.stid = STID
        self.labelN = QtGui.QLabel(name + ":", mom)
        self.labelD = QtGui.QLabel("@ " + date, mom)
        self.th = QtGui.QTextEdit(mom)  
        self.th.setEnabled(False)
        self.th.setStyleSheet("background-color:white")
        self.num = 0
        self.th.setText(things)
        self.flag = 0
        self.cORcs = flag
    
        num = str(things).count("\n")
        height = max(num * 25 + 35, 25 * (len(things)/40) + 35)
        self.name = hostname
        self.things = things
        self.date = date
        self.nameCMT = name
        
        self.labelN.setGeometry(x+5, y, 150, 23)
        self.labelD.setGeometry(x + 250, y, 150, 20)
        self.th.setGeometry(x, y + 25, 380, height)
        self.labelN.setFont(QtGui.QFont(u"Adobe Gothic Std B", 16))
        self.labelD.setFont(QtGui.QFont(u"微软雅黑 Light", 10))
        self.th.setFont(QtGui.QFont(u"微软雅黑", 14))
        self.length = height + 60
        
        if self.cORcs:
            self.comment = QtGui.QPushButton(mom)
            self.comment.setGeometry(x, y + height + 30, 200, 30)
            self.comment.setFont(QtGui.QFont(u"微软雅黑 Light", 10))
            self.comment.setText(u"评论")
        
        self.good = QtGui.QPushButton(mom)
        self.good.setGeometry(x + 330, y + height + 30, 30, 30)
        
        self.allName = ''
        res = sqlopt.howManyGoodOf(USERID, STID)
        for i in range(len(res)):
            self.allName = self.allName + str(res[i][1])+', '

        self.numofGood = QtGui.QLabel(mom)
        self.num = len(res)
        temp =  'x' + str(self.num)
        self.numofGood.setText(temp)
        self.numofGood.setGeometry(int(x + 360), int(y + height + 30), 30, 30)
        self.numofGood.setFont(QtGui.QFont(u"微软雅黑 Light", 10))
        self.numofGood.setToolTip(self.allName)
        
        if sqlopt.isGood(self.hostid, self.stuserid, self.stid):
            self.good.setIcon(QtGui.QIcon('pics/good.png'))
            self.flag = 1
        else:
            self.good.setIcon(QtGui.QIcon('pics/bad.png'))
            self.flag = 0
            
        self.good.setFlat(True)
        self.length += 33
        
        if self.cORcs:
            self.comment.connect(self.comment, QtCore.SIGNAL('clicked()'), self.setComment)
            
        self.good.connect(self.good, QtCore.SIGNAL('clicked()'), self.nextHow)
                
    def setComment(self):
        self.newCmt = cmtWindow.cmtWindow(self.hostid, self.stuserid, self.stid, self.things, self.date, self.nameCMT, self.name)
        self.newCmt.show()
        
    def nextHow(self):
        if self.flag == 1:
            self.good.setIcon(QtGui.QIcon('pics/bad.png'))
            self.good.show()
            self.num-=1
            temp =  'x' + str(self.num)
            self.numofGood.setText(temp)
            temp = self.name+', '
            self.allName = self.allName.replace(temp, '')
            self.numofGood.setToolTip(self.allName)
            self.numofGood.show()
            self.flag = 0
            sqlopt.cancelGood(self.hostid, self.stuserid, self.stid)
        elif self.flag == 0:
            self.good.setIcon(QtGui.QIcon('pics/good.png'))
            self.good.show()
            self.num+=1
            temp =  'x' + str(self.num)
            self.numofGood.setText(temp)
            self.allName = self.allName + self.name + ', '
            self.numofGood.setToolTip(self.allName)
            self.numofGood.show()
            self.flag = 1
            sqlopt.addGood(self.hostid, self.stuserid, self.stid)
        
        
    def dis(self):
        self.labelN.show()
        self.labelD.show()
        self.th.show()
        if self.cORcs:
            self.comment.show()
        self.good.show()
        self.numofGood.show()