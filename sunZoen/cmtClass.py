# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui
        
class stateWin():
    def __init__(self, name, date, thing, px, py, dad):
        self.name = name
        self.date = date
        self.thing = thing
        
        num = str(thing).count("\n")
        ht = max(num * 15 + 35, 15 * (len(thing)/40) + 35)
        
        self.labelN = QtGui.QLabel(self.name, dad)
        self.labelT = QtGui.QLabel(self.date, dad)
        self.labelC = QtGui.QTextEdit(dad)
        
        self.labelC.setText(self.thing)
        self.labelC.setDisabled(True)
        self.labelC.setStyleSheet("color : green; width : 0")
        
        self.labelC.setGeometry(px, py + 20, 370, ht)
        self.labelN.setGeometry(px + 3, py, 240, 20)
        self.labelT.setGeometry(px + 265, py, 190, 20)
        
        self.labelN.setFont(QtGui.QFont(u"Adobe Gothic Std B", 9))
        self.labelC.setFont(QtGui.QFont(u"微软雅黑", 10))
        self.labelT.setFont(QtGui.QFont(u"Adobe Gothic Std B", 8))
        
        self.height = ht + 30
  
    def dis(self):
        self.labelC.show()
        self.labelN.show()
        self.labelT.show()