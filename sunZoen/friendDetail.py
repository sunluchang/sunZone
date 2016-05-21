# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore, Qt
import sqlopt, stateW

class friendDetail(QtGui.QMainWindow):
    def __init__(self, id, name, hostid, parent=None):
        super(friendDetail, self).__init__(parent)
        self.setWindowTitle(u"详细资料-SLcZone")
        self.setFixedSize(400, 720)
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        self.id = id
        self.name = name
        self.hostid = hostid
        
        self.head = QtGui.QPushButton(self)
        self.head.setGeometry(10, 10, 80, 80)
        self.head.setEnabled(False)
        
        self.label = QtGui.QLabel(name + u" 's 详细信息", self)
        self.label.setGeometry(100, 11, 400, 40)
        self.label.setFont(QtGui.QFont(u"微软雅黑", 18))
        
        self.delete = QtGui.QPushButton(u"删除", self)
        self.delete.setGeometry(330, 10, 60, 80)
        self.delete.setFont(QtGui.QFont(u"微软雅黑 Light", 16))
        self.delete.setFlat(True)
        
        self.howmany = QtGui.QLabel(self)
        self.howmany.setFont(QtGui.QFont(u"微软雅黑", 12))
        
        self.delete.connect(self.delete, QtCore.SIGNAL('clicked()'), self.deleteF)
        self.loadInfo()
        self.load()

    def deleteF(self):
        reply = QtGui.QMessageBox.question(self, u'确认', u"确认删除"+self.name + "?", QtGui.QMessageBox.Yes)
        if reply == QtGui.QMessageBox.Yes:
            sqlopt.deleteFriend(self.hostid, self.id)
            self.close()
        else:
            return
    
    def loadInfo(self):
        res = sqlopt.queryInfoFor(self.id)
        name = ''
        sex = ''
        blood = ''
        addr = ''
        phone = ''
        date = QtCore.QDate()
        if res[0][1]:
            name = res[0][1]
        if res[0][2]:
            sex = str(res[0][2])
        if res[0][3]:
            date = res[0][3]
        if res[0][4]:
            blood = str(res[0][4])
        if res[0][5]:
            pass
        if res[0][6]:
            addr = str(res[0][6])
        if res[0][7]:
            phone = res[0][7]
            
        self.n = QtGui.QLabel('Name:\t'+name, self)
        self.s = QtGui.QLabel('Sex:\t'+sex, self)
        self.b = QtGui.QLabel('Blood:\t'+blood, self)
        self.a = QtGui.QLabel('Addr:\t'+addr, self)
        self.p = QtGui.QLabel('Phone:\t'+phone, self)
        self.d = QtGui.QDateEdit(self)
        self.d.setDate(date)
        
        self.n.setGeometry(20, 130, 180, 30)
        self.s.setGeometry(20, 180, 180, 30)
        self.b.setGeometry(20, 230, 180, 30)
        self.a.setGeometry(210, 130, 180, 30)
        self.p.setGeometry(210, 180, 180, 30)
        self.d.setGeometry(210, 230, 180, 30)
        self.d.setEnabled(False)
        
        font = QtGui.QFont(u"微软雅黑", 14)
        self.n.setFont(font)
        self.s.setFont(font)
        self.b.setFont(font)
        self.a.setFont(font)
        self.p.setFont(font)
        self.d.setFont(font)
        
        
    def load(self):
        self.scrollAreaWidgetContents = QtGui.QWidget(self)
        self.scrollAreaWidgetContents.setMinimumSize(360, 360)
        self.scrollAreaWidgetContents.setGeometry(10, 330, 390, 360)
        #最大宽度 270
        self.scrollArea = QtGui.QScrollArea(self)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setGeometry(QtCore.QRect(10, 330, 390, 360))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFrameStyle(0)
        self.scrollArea.setStyleSheet("width:3")
        
        self.scrollArea.show()
        self.scrollAreaWidgetContents.show()
        
        length = 10
        res = sqlopt.getStateFor(self.id)
        self.howmany.setText(u'一共 ' + str(len(res)) + u'条动态')
        self.howmany.setGeometry(100, 50, 200, 40)
        if (len(res) == 0):
            w = QtGui.QLabel(u"无动态", self.scrollAreaWidgetContents)
            w.setGeometry(100, 200, 190, 60)
            w.setFont(QtGui.QFont(u"微软雅黑", 30))
            w.setAlignment(Qt.Qt.AlignCenter)
            w.show()
        else:
            self.b = []
            for i in range(len(res)):
                #stid, things, stdate
                #hostID, USERID, STID, x, y, name, date, things, mom
                self.b.append(stateW.stateWin(self.hostid, self.id, str(res[i][0]), 0, length, self.name, str(res[i][2]), str(res[i][1]), self.scrollAreaWidgetContents, self.name))
                self.b[i].dis()            
                length += self.b[i].length
            
            self.scrollAreaWidgetContents.setMinimumSize(360, length)
     
    
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = friendDetail(1, "slc", 2)
    frm.show()
    sys.exit(app.exec_())