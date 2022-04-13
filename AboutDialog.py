#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
# from PyQt4 import QtGui, QtCore
from PyQt5 import QtCore, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):

    def __init__(self):
        # super().__init__()                # Python3
        super(Ui_Dialog, self).__init__()  # Python2
        self.setupUi()

    def setupUi(self):

        self.setFixedSize(622, 269)
        self.setWindowTitle("About")

        self.textEdit = QtWidgets.QTextBrowser(self)
        self.textEdit.setOpenExternalLinks(True)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 601, 191))

        self.pushButton = QtWidgets.QPushButton('Close', self)
        self.pushButton.setGeometry(QtCore.QRect(270, 220, 92, 27))
        self.pushButton.clicked.connect(self.close)

        self.textEdit.setHtml("<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software is designed to generate data for non-grid (arbitrary) points of a WAVEWATCH III<span style=\" vertical-align:super;\">®</span> output file. The output should be in format of ITYPE(2)-OTYPE(2) and ASCII encoding. Note that new task can be initialised at any point by choosing &quot;New&quot; from &quot;Menu&quot;.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This software has been created for research purposes at <a href=\"http://www.inio.ac.ir/incoh\"><span style=\" text-decoration: underline; color:#0000ff;\">Iranian National Center for Ocean Hazards (INCOH)</span></a> and provided with no warranty. Any commercial utilization of this software is ristrictly prohibited.</p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Author: Farrokh A. Ghavanini</p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Email: <a href=\"mailto:ghavanini@gmail.com\"><span style=\" text-decoration: underline; color:#0000ff;\">ghavanini@gmail.com</span></a></p></body></html>")
        #
        # # Display Widget at the center of the screen
        # self.frameGeometry = self.frameGeometry()
        # self.frameGeometry.moveCenter(self.centerPosition)
        # self.move(self.frameGeometry.topLeft())
        frameGm = self.frameGeometry()
        screen = QtWidgets.QApplication.desktop().screenNumber(QtWidgets.QApplication.desktop().cursor().pos())
        centerPoint = QtWidgets.QApplication.desktop().screenGeometry(screen).center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

        self.show()
