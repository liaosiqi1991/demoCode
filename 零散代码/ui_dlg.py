# -*- coding:utf8 -*-


# 弹出窗体

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

#键盘事件
#新增控件并且触发事件



#控件接受到消息，并且处理消息后作用到界面控件上（例如改变空间名称或者窗体背景颜色）
#1 输入消息  2 颜色对话框  3 文件选择框
class LsqW(QMainWindow):

    def __init__(self, parent=None):
        super(LsqW, self).__init__(parent)
        
        self.setWindowTitle("测试窗口")
        self.resize(400, 400)

        self.redb = QPushButton('测试按钮',self)
        self.redb.setCheckable(True)
        self.redb.move(10, 10)
        self.redb.clicked.connect(self.test3)

        self.txt=  QTextEdit(self)
        self.txt.move(10, 80)

    def test1(self):
        reply = QMessageBox.information(self,           
                                    "标题",
                                    "消息",
                                    QMessageBox.Yes | QMessageBox.No)
        if reply==QMessageBox.Yes:
            self.txt.setPlainText('YES')
        else:
            self.txt.setPlainText('No')
            
    #输入框 QInputDialog
    def test2(self):
        name,ok = QInputDialog.getText(self,"项目名称","输入项目名称:",
                                       QLineEdit.Normal,"默认")
        if ok and (len(name)!=0):
            self.txt.setText(name)
    #颜色
    def test3(self):
        color = QColorDialog.getColor(Qt.blue, self, "Select Color")


        


app = QApplication(sys.argv)
ui_demo = LsqW()
ui_demo.show()
sys.exit(app.exec_())


#下面是控件简单接受到消息
"""
class LsqW(QMainWindow):

    def __init__(self, parent=None):
        super(LsqW, self).__init__(parent)
        
        self.setWindowTitle("测试窗口")
        self.resize(400, 400)

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked.connect(self.test1)
        

    def test1(self):
        reply = QMessageBox.information(self,           
                                    "标题",
                                    "消息",
                                    QMessageBox.Yes | QMessageBox.No)
        print(reply)   
  
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui_demo = LsqW()
    ui_demo.show()
    sys.exit(app.exec_())
"""


