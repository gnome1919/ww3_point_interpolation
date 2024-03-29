# -*- coding: utf-8 -*-

#
#

from PyQt5 import QtCore, QtGui, QtWidgets

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


# About the "object" term in class decleration refer to https://stackoverflow.com/questions/4015417/why-do-python-classes-inherit-object

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(756, 498)
        MainWindow.setWindowIcon(QtGui.QIcon('./Logo_Black.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 728, 411))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        # Folder selection
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.folder_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.folder_btn.setObjectName(_fromUtf8("folder_btn"))
        self.horizontalLayout.addWidget(self.folder_btn)
        self.folder_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.folder_le.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_le.sizePolicy().hasHeightForWidth())
        self.folder_le.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.folder_le.setFont(font)
        self.folder_le.setObjectName(_fromUtf8("folder_le"))
        self.horizontalLayout.addWidget(self.folder_le)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        # Sample file selection
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.sample_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.sample_btn.setObjectName(_fromUtf8("sample_btn"))
        self.horizontalLayout_2.addWidget(self.sample_btn)
        self.sample_btn.setEnabled(False)
        self.sample_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.sample_le.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_le.sizePolicy().hasHeightForWidth())
        self.sample_le.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.sample_le.setFont(font)
        self.sample_le.setObjectName(_fromUtf8("sample_le"))
        self.horizontalLayout_2.addWidget(self.sample_le)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        # Date selection
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.date1_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.date1_lbl.setObjectName(_fromUtf8("date1_lbl"))
        self.horizontalLayout_3.addWidget(self.date1_lbl)
        self.date1_de = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date1_de.setObjectName(_fromUtf8("date1_de"))
        self.date1_de.setDisplayFormat('yyyy MM dd')
        self.initDate = QtCore.QDate(2015,1,1)
        self.date1_de.setDate(self.initDate)     
        self.date1_de.setEnabled(False)
        self.date1_de.setCalendarPopup(True)
        self.horizontalLayout_3.addWidget(self.date1_de)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.date2_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.date2_lbl.setObjectName(_fromUtf8("date2_lbl"))
        self.horizontalLayout_3.addWidget(self.date2_lbl)
        self.date2_de = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.date2_de.setEnabled(False)
        self.date2_de.setCalendarPopup(True)
        self.date2_de.setObjectName(_fromUtf8("date2_de"))
        self.date2_de.setDisplayFormat('yyyy MM dd')
        self.date2_de.setDate(self.initDate)         
        self.horizontalLayout_3.addWidget(self.date2_de)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.date_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.date_btn.setObjectName(_fromUtf8("date_btn"))
        self.date_btn.setEnabled(False)
        self.horizontalLayout_3.addWidget(self.date_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        # Location selection        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.lon_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lon_lbl.setObjectName(_fromUtf8("lon_lbl"))
        self.horizontalLayout_4.addWidget(self.lon_lbl)
        self.lon_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lon_le.setEnabled(False)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lon_le.setFont(font)
        self.lon_le.setObjectName(_fromUtf8("lon_le"))
        self.horizontalLayout_4.addWidget(self.lon_le)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.lat_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lat_lbl.setObjectName(_fromUtf8("lat_lbl"))
        self.horizontalLayout_4.addWidget(self.lat_lbl)
        self.lat_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lat_le.setEnabled(False)
        font = QtGui.QFont()
        font.setItalic(True)
        self.lat_le.setFont(font)
        self.lat_le.setObjectName(_fromUtf8("lat_le"))
        self.horizontalLayout_4.addWidget(self.lat_le)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.location_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.location_btn.setObjectName(_fromUtf8("location_btn"))
        self.location_btn.setEnabled(False)
        self.horizontalLayout_4.addWidget(self.location_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_4)             
       
        # Parameter selection        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.param_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.param_lbl.setObjectName(_fromUtf8("param_lbl"))
        self.horizontalLayout_5.addWidget(self.param_lbl)
        
        self.hs_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.hs_lbl.setObjectName(_fromUtf8("hs_lbl"))
        self.horizontalLayout_5.addWidget(self.hs_lbl)        
        self.hs_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.hs_cx.setObjectName(_fromUtf8("hs_cx"))
        self.hs_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.hs_cx)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem8)
        
        self.l_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.l_lbl.setObjectName(_fromUtf8("l_lbl"))
        self.horizontalLayout_5.addWidget(self.l_lbl)        
        self.l_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.l_cx.setObjectName(_fromUtf8("l_cx"))
        self.l_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.l_cx)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)

        self.tr_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.tr_lbl.setObjectName(_fromUtf8("tr_lbl"))
        self.horizontalLayout_5.addWidget(self.tr_lbl)        
        self.tr_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.tr_cx.setObjectName(_fromUtf8("tr_cx"))
        self.tr_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.tr_cx)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        
        self.dir_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dir_lbl.setObjectName(_fromUtf8("dir_lbl"))
        self.horizontalLayout_5.addWidget(self.dir_lbl)        
        self.dir_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.dir_cx.setObjectName(_fromUtf8("dir_cx"))
        self.dir_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.dir_cx)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        
        self.spr_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.spr_lbl.setObjectName(_fromUtf8("spr_lbl"))
        self.horizontalLayout_5.addWidget(self.spr_lbl)        
        self.spr_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.spr_cx.setObjectName(_fromUtf8("spr_cx"))
        self.spr_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.spr_cx)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        
        self.fp_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.fp_lbl.setObjectName(_fromUtf8("fp_lbl"))
        self.horizontalLayout_5.addWidget(self.fp_lbl)
        self.fp_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.fp_cx.setObjectName(_fromUtf8("fp_cx"))
        self.fp_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.fp_cx)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        
        self.pdir_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pdir_lbl.setObjectName(_fromUtf8("pdir_lbl"))
        self.horizontalLayout_5.addWidget(self.pdir_lbl)        
        self.pdir_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.pdir_cx.setObjectName(_fromUtf8("pdir_cx"))
        self.pdir_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.pdir_cx)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        
        self.pspr_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pspr_lbl.setObjectName(_fromUtf8("pspr_lbl"))
        self.horizontalLayout_5.addWidget(self.pspr_lbl)
        self.pspr_cx = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.pspr_cx.setObjectName(_fromUtf8("pspr_cx"))
        self.pspr_cx.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.pspr_cx)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        
        self.param_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.param_btn.setObjectName(_fromUtf8("param_btn"))
        self.param_btn.setEnabled(False)
        self.horizontalLayout_5.addWidget(self.param_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        
        # Interpolation method selection
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.interp_lbl = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.interp_lbl.setObjectName(_fromUtf8("interp_lbl"))
        self.horizontalLayout_6.addWidget(self.interp_lbl)
        self.interp_cb = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.interp_cb.setObjectName(_fromUtf8("interp_cb"))
        self.interp_cb.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.interp_cb)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.interp_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.interp_btn.setObjectName(_fromUtf8("param_btn"))
        self.interp_btn.setEnabled(False)
        self.horizontalLayout_6.addWidget(self.interp_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        
        # Output file selection
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.output_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.output_btn.setObjectName(_fromUtf8("output_btn"))
        self.output_btn.setEnabled(False)
        self.horizontalLayout_10.addWidget(self.output_btn)
        self.output_le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setItalic(True)
        self.output_le.setFont(font)
        self.output_le.setObjectName(_fromUtf8("output_le"))
        self.output_le.setEnabled(False)
        self.horizontalLayout_10.addWidget(self.output_le)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        
        # Go button
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.go_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.go_btn.setObjectName(_fromUtf8("go_btn"))
        self.go_btn.setEnabled(False)
        self.horizontalLayout_8.addWidget(self.go_btn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        
        # Partial progress bar 
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.partial_pb = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.partial_pb.setProperty("value", 0)
        self.partial_pb.setObjectName(_fromUtf8("partial_pb"))
        self.horizontalLayout_9.addWidget(self.partial_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        
        # Overall progress bar       
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.overall_pb = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.overall_pb.setProperty("value", 0)
        self.overall_pb.setObjectName(_fromUtf8("overall_pb"))
        self.horizontalLayout_10.addWidget(self.overall_pb)
        self.verticalLayout.addLayout(self.horizontalLayout_10)        
        
        # Menu, actions and status bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 756, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_Menu = QtWidgets.QMenu(self.menubar)
        self.menu_Menu.setObjectName(_fromUtf8("menu_Menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_new = QtWidgets.QAction(MainWindow)
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.menu_Menu.addAction(self.action_new)
        self.menu_Menu.addAction(self.action_about)
        self.menubar.addAction(self.menu_Menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Display MainWindow at the center of the screen
        self.frame_geometry = MainWindow.frameGeometry()
        self.center_position = QtWidgets.QDesktopWidget().availableGeometry().center()
        self.frame_geometry.moveCenter(self.center_position)
        MainWindow.move(self.frame_geometry.topLeft())

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "WAVEWATCH III® Arbitrary Point Interpolation", None))
        self.folder_btn.setText(_translate("MainWindow", "Select root folder", None))
        self.folder_le.setText(_translate("MainWindow", "Root folder is the one which contains folders of each date", None))
        self.sample_btn.setText(_translate("MainWindow", "Select sample file", None))
        self.sample_le.setText(_translate("MainWindow", "Select a sample tab file (should be of the same name and type in all date folders)", None))        
        self.lon_lbl.setText(_translate("MainWindow", "Longitude", None))
        self.lat_lbl.setText(_translate("MainWindow", "Latitude", None))
        self.location_btn.setText(_translate("MainWindow", "OK", None))
        self.date1_lbl.setText(_translate("MainWindow", "Start date:", None))
        self.date2_lbl.setText(_translate("MainWindow", "End date:", None))
        self.date_btn.setText(_translate("MainWindow", "OK", None))
        self.param_btn.setText(_translate("MainWindow", "OK", None))
        self.interp_btn.setText(_translate("MainWindow", "OK", None))
        self.param_lbl.setText(_translate("MainWindow", "Select parameter(s):  ", None))       
        self.hs_lbl.setText(_translate("MainWindow", "Hs", None))
        self.l_lbl.setText(_translate("MainWindow", "L", None))
        self.tr_lbl.setText(_translate("MainWindow", "Tr", None))
        self.dir_lbl.setText(_translate("MainWindow", "Dir", None))
        self.spr_lbl.setText(_translate("MainWindow", "Spr", None))
        self.fp_lbl.setText(_translate("MainWindow", "fp", None))
        self.pdir_lbl.setText(_translate("MainWindow", "p_dir", None))        
        self.pspr_lbl.setText(_translate("MainWindow", "p_spr", None))                
        self.interp_lbl.setText(_translate("MainWindow", "Select interpolation method", None))
        self.output_btn.setText(_translate("MainWindow", "Select output file", None))
        self.output_le.setText(_translate("MainWindow", "Path to output file", None))
        self.go_btn.setText(_translate("MainWindow", "Go!", None))
        self.menu_Menu.setTitle(_translate("MainWindow", "Menu", None))
        self.action_new.setText(_translate("MainWindow", "New", None))
        self.action_about.setText(_translate("MainWindow", "About", None))
