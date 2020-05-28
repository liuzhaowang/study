# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'woniuci.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
from configparser import ConfigParser

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(807, 603)
        font = QtGui.QFont()
        font.setPointSize(11)
        Form.setFont(font)
        self.button_start = QtWidgets.QPushButton(Form)
        self.button_start.setGeometry(QtCore.QRect(160, 480, 131, 31))
        self.button_start.setObjectName("button_start")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.text_tomcat = QtWidgets.QTextEdit(Form)
        self.text_tomcat.setGeometry(QtCore.QRect(200, 150, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.text_tomcat.setFont(font)
        self.text_tomcat.setObjectName("text_tomcat")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(80, 210, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setObjectName("label_2")
        self.text_svn = QtWidgets.QTextEdit(Form)
        self.text_svn.setGeometry(QtCore.QRect(200, 210, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.text_svn.setFont(font)
        self.text_svn.setObjectName("text_svn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(True)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.text_svnurl = QtWidgets.QTextEdit(Form)
        self.text_svnurl.setGeometry(QtCore.QRect(200, 270, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.text_svnurl.setFont(font)
        self.text_svnurl.setObjectName("text_svnurl")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(80, 330, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.text_version = QtWidgets.QTextEdit(Form)
        self.text_version.setGeometry(QtCore.QRect(200, 320, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.text_version.setFont(font)
        self.text_version.setObjectName("text_version")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(80, 390, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Andalus")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setText("winRAR路径:")
        self.label_5.setTextFormat(QtCore.Qt.RichText)
        self.label_5.setObjectName("label_5")
        self.text_rar = QtWidgets.QTextEdit(Form)
        self.text_rar.setGeometry(QtCore.QRect(200, 390, 391, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.text_rar.setFont(font)
        self.text_rar.setObjectName("text_rar")
        self.check_source = QtWidgets.QCheckBox(Form)
        self.check_source.setGeometry(QtCore.QRect(70, 440, 121, 31))
        self.check_source.setObjectName("check_source")
        self.check_build = QtWidgets.QCheckBox(Form)
        self.check_build.setGeometry(QtCore.QRect(200, 440, 121, 31))
        self.check_build.setObjectName("check_build")
        self.check_deploy = QtWidgets.QCheckBox(Form)
        self.check_deploy.setGeometry(QtCore.QRect(330, 440, 121, 31))
        self.check_deploy.setObjectName("check_deploy")
        self.check_test = QtWidgets.QCheckBox(Form)
        self.check_test.setGeometry(QtCore.QRect(440, 440, 121, 31))
        self.check_test.setObjectName("check_test")
        self.check_report = QtWidgets.QCheckBox(Form)
        self.check_report.setGeometry(QtCore.QRect(560, 440, 121, 31))
        self.check_report.setObjectName("check_report")
        self.button_save = QtWidgets.QPushButton(Form)
        self.button_save.setGeometry(QtCore.QRect(330, 480, 131, 31))
        self.button_save.setObjectName("button_save")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(280, 50, 271, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "WoniuCBT CI System"))
        self.button_start.setText(_translate("Form", "开始测试"))
        self.label.setText(_translate("Form", "Tomcat目录:"))
        self.label_2.setText(_translate("Form", "SVN源码目录:"))
        self.label_3.setText(_translate("Form", "SVN服务器:"))
        self.label_4.setText(_translate("Form", "系统version:"))
        self.check_source.setText(_translate("Form", "是否下载源码"))
        self.check_build.setText(_translate("Form", "是否构建版本"))
        self.check_deploy.setText(_translate("Form", "是否部署"))
        self.check_test.setText(_translate("Form", "是否执行测试"))
        self.check_report.setText(_translate("Form", "是否发送报告"))
        self.button_save.setText(_translate("Form", "保存配置"))
        self.label_6.setText(_translate("Form", "欢迎使用蜗牛CBT持续集成工具"))
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys
from woniucbt.ci.woniusales import WoniuSaleCI
class WoniuCI(QWidget,Ui_Form):
    def __init__(self):
        super(WoniuCI,self).__init__()
        self.setupUi(self)

    def get_config_value(cls,section,key):
        conf = ConfigParser()
        conf.read('../data/woniusales.conf') #读取当前目录下的配置文件
        return  conf.get(section,key)

    def start_test(self):
        wc =  WoniuSaleCI()
        if self.check_source.isChecked():
            wc.svn()

        if self.check_build.isChecked():
            wc.ant()

        if self.check_deploy.isChecked():
            wc.deploy()

        if self.check_test.isChecked():
            wc.test()

        if self.check_report.isChecked():
            wc.report()

    def save_config(self):
        tomcat = self.text_tomcat.toPlainText()
        svn = self.text_svn.toPlainText()
        rar = self.text_rar.toPlainText()
        svn_url = self.text_svnurl.toPlainText()
        version = self.text_version.toPlainText()

        config = ConfigParser()
        config.read('../data/woniusales.conf')
        config.set('ci','tomcat',tomcat)
        config.set('ci', 'svn', svn)
        config.set('ci', 'svn_url', svn_url)
        config.set('ci', 'rar', rar)
        config.set('ci', 'version', version)

        with open('../data/woniusales.conf','w+',encoding='utf8') as file:
            config.write(file)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WoniuCI()
    w.show()
    w.text_tomcat.setText(w.get_config_value('ci', 'tomcat'))
    w.text_svn.setText(w.get_config_value('ci', 'svn'))
    w.text_svnurl.setText(w.get_config_value('ci', 'svn_url'))
    w.text_version.setText(w.get_config_value('ci', 'version'))
    w.text_rar.setText(w.get_config_value('ci', 'rar'))
    w.check_deploy.setChecked(True)
    w.check_test.setChecked(True)
    w.button_start.clicked.connect(w.start_test)
    w.button_save.clicked.connect(w.save_config)
    sys.exit(app.exec_())



