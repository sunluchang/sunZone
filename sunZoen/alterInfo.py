# -*- coding: utf-8 -*-
"""
Created on Fri May 20 13:52:34 2016

@author: sunluchang
"""

from PyQt4 import QtGui, QtCore
import sqlopt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
        
class alterInfo(QtGui.QMainWindow):
    def __init__(self, usrID, setNewName, parent = None):
        super(alterInfo, self).__init__(parent)
        self.setWindowTitle(usrID + u"修改资料-SLcZone")
        self.setFixedSize(650, 180)
        desktop =QtGui.QApplication.desktop()
        width = desktop.width()
        height = desktop.height()
        self.move((width - self.width())/2, (height - self.height())/2)
        self.setMouseTracking(True)
        
        self.setNewName = setNewName
        font = QtGui.QFont(u"微软雅黑", 10)
        self.id = usrID
        
        self.head = QtGui.QPushButton(self)
        self.head.setGeometry(10, 10, 160, 160)
        self.head.setText(u"添加图像")
        self.head.setFont(font)
        
        self.n = QtGui.QLabel(u"昵称：", self)
        self.n.setGeometry(200, 10, 40, 30)
        self.n.setFont(font)
        self.name = QtGui.QLineEdit(self)
        self.name.setGeometry(250, 15, 160, 20)
        self.name.setMaxLength(20)
        self.name.setFont(font)
        
        self.s = QtGui.QLabel(u"性别：", self)
        self.s.setGeometry(200, 50, 40, 30)
        self.s.setFont(font)
        self.sex = QtGui.QComboBox(self)
        self.sex.addItem(_fromUtf8(""))
        self.sex.addItem(_fromUtf8("Male"))
        self.sex.addItem(_fromUtf8("Female"))
        self.sex.addItem(_fromUtf8(u"Others"))
        self.sex.setFont(font)
        self.sex.setGeometry(250, 55, 160, 20)
        
        self.dateL = QtGui.QLabel(u"生日：", self)
        self.dateL.setGeometry(200, 90, 40, 30)
        self.dateL.setFont(font)
        self.date = QtGui.QDateEdit(self)
        self.date.setGeometry(250, 95, 100, 20)
        self.date.setFont(font)
        
        self.b = QtGui.QLabel(u"血型：", self)
        self.b.setGeometry(200, 130, 40, 30)
        self.b.setFont(font)
        self.blood = QtGui.QComboBox(self)
        self.blood.addItem(_fromUtf8(""))
        self.blood.addItem(_fromUtf8("A+"))
        self.blood.addItem(_fromUtf8(u"B+"))
        self.blood.addItem(_fromUtf8("O"))
        self.blood.addItem(_fromUtf8("AB"))
        self.blood.addItem(_fromUtf8("Others"))
        self.blood.setFont(font)
        self.blood.setGeometry(250, 135, 160, 20)
        
        self.p = QtGui.QLabel(u"手机：", self)
        self.p.setGeometry(420, 10, 40, 30)
        self.p.setFont(font)
        self.phone = QtGui.QLineEdit(self)
        self.phone.setGeometry(470, 15, 160, 20)
        self.phone.setMaxLength(11)
        self.phone.setFont(font)
        
        self.a = QtGui.QLabel(u"地址：", self)
        self.a.setGeometry(420, 50, 40, 30)
        self.a.setFont(font)
        self.address = QtGui.QLineEdit(self)
        self.address.setGeometry(470, 55, 160, 20)
        self.address.setMaxLength(50)
        self.address.setFont(font)
        
        self.ok = QtGui.QPushButton(u"保存", self)
        self.ok.setGeometry(540, 135, 90, 20)
        
        self.cancel = QtGui.QPushButton(u"取消", self)
        self.cancel.setGeometry(430, 135, 90, 20)
        
        self.ok.connect(self.ok, QtCore.SIGNAL('clicked()'), self.save)
        self.cancel.connect(self.cancel, QtCore.SIGNAL('clicked()'), self.Quit)
        
        self.load()
        self.head.connect(self.head, QtCore.SIGNAL('clicked()'), self.setHeadPic)
        
    def setHeadPic(self):
        log = QtGui.QFileDialog()
        log.getOpenFileNameAndFilter(self, u"选择头像", "", "*.jpg")
        
    
    def load(self):
        res = sqlopt.queryInfoFor(self.id)
        if res[0][1]:
            self.name.setText(res[0][1])
        if res[0][2]:
            index = ['male', 'female', 'others'].index(str(_fromUtf8(res[0][2])).lower()) + 1
            self.sex.setCurrentIndex(index)
        if res[0][3]:
            self.date.setDate(res[0][3])
        if res[0][4]:
            index = ['a+', 'b+', 'o', 'ab', 'others'].index(str(_fromUtf8(res[0][4])).lower()) + 1
            self.blood.setCurrentIndex(index)
        if res[0][5]:
            pass
        if res[0][6]:
            self.address.setText(u"" + str(res[0][6]))
        if res[0][7]:
            self.phone.setText(_fromUtf8(res[0][7]))
            
        
    def save(self):
        date = str(self.date.date()).split("(")[1].split(")")[0].replace(", ", "-")
        flag = sqlopt.updateInfoFor(self.id, self.name.text(), self.sex.currentText(), date, self.blood.currentText(), self.address.text(), self.phone.text())
        if flag:
            reply = QtGui.QMessageBox.question(self, u'该用户名不可用', u"用户名已经存在，不可用！", QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
            	return
        self.close()
        self.setNewName(self.name.text())
    
    def Quit(self):
        self.close()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    frm = alterInfo("sunluchang", 1)
    frm.show()
    sys.exit(app.exec_())