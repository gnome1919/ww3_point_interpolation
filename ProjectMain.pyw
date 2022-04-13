#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ProjectMain.py(w)
#  
#  Copyright 2017 Farrokh A. Ghavanini <ghavanini@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.

#  
#  

from PyQt5 import QtGui, QtCore, QtWidgets
import datetime as dt
from scipy import interpolate
import numpy as np
from ProjectGui import Ui_MainWindow
from AboutDialog import Ui_Dialog
from WW3TabFunctions import *
import os
from math import ceil, floor

# For better understanding Python classes:              https://www.w3schools.com/python/python_classes.asp
# For better understanding Python class inheritance:    https://www.w3schools.com/python/python_inheritance.asp
# For better understanding super() with __init__():     https://www.i2tutorials.com/python-super-with-__init__-methods/
# How to create apps with PyQt:                         https://www.pythonguis.com/tutorials/creating-your-first-pyqt-window/

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # super().__init__()                # Python3
        super(MainWindow, self).__init__()  # Python2
        # object created in ProjectGui.py:
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.filename = ""
        self.full_path = ""
        self.folder = ""
        self.params_split = []
        self.params_list = []
        self.params_names = []
        self.params_units = []
        self.timestep = ""
        self.index = None
        self.selected_param = None
        self.selected_method = None
        self.output_file = None
        self.lon = None
        self.lat = None
        self.start_date = None
        self.start_time = None

        # Number input validator        
        float_validator = QtGui.QRegExpValidator(QtCore.QRegExp('[-+]?([0-9]*\.[0-9]+|[0-9]+)'), self)
        # intValidator = QtGui.QRegExpValidator(QtCore.QRegExp('([1-9][0-9])'), self)
        # Longitude input field validator  
        self.ui.lon_le.setValidator(float_validator)
        # Latitude input field validator
        self.ui.lat_le.setValidator(float_validator)
        # Timestep input field validator  
        # self.ui.folder_le_4.setValidator(intValidator)

        # Select folder button
        self.ui.folder_btn.clicked.connect(self.selectFolder)
        # Select sample file button
        self.ui.sample_btn.clicked.connect(self.selectSample)        
        # OK button on date selecting section
        self.ui.date_btn.clicked.connect(self.setTimeRange)       
        # OK button on location input section
        self.ui.location_btn.clicked.connect(self.lockLocation)
        # OK button on timestep input section
        # self.ui.date_btn.clicked.connect(self.selectParameter)
        # OK button on select parameter section
        self.ui.param_btn.clicked.connect(self.extractValues)
        # OK button on interpolation method select section
        self.ui.interp_btn.clicked.connect(self.setMethod)
        # Select Output File button
        self.ui.output_btn.clicked.connect(self.setOutput)
        # Go! button select
        self.ui.go_btn.clicked.connect(self.startProcess)
        # New action menu item
        self.ui.action_new.triggered.connect(self.newSession)
        # About action menu item
        self.ui.action_about.triggered.connect(self.aboutDialog)

    def selectFolder(self):
        self.ui.folder_le.setText(QtWidgets.QFileDialog.getExistingDirectory())
        if self.ui.folder_le.text() == "":
            self.ui.folder_le.setText("Root folder is the one which contains folders of each date")
            return
        self.folder = self.ui.folder_le.text()  # root folder path
        self.ui.folder_btn.setEnabled(False)
        self.ui.sample_btn.setEnabled(True)
                    
    def selectSample(self):
        self.ui.sample_le.setText(QtWidgets.QFileDialog.getOpenFileName()[0])
        if self.ui.sample_le.text() == "":
            self.ui.sample_le.setText("Select a sample tab file (should be of the same name and type in all date folders)")
            return
        self.sample_file = os.path.basename((self.ui.sample_le.text())) # filename
        self.full_path = self.ui.sample_le.text() # full path to filename
        try:
            self.file_check = extractLine(self.full_path, 1)
            self.file_line_split = self.file_check.split()
            if self.file_line_split[0] != "Time":
                self.newSession
                self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red}")
                self.ui.statusbar.showMessage('The selected file is invalid! Please select another one (refer to "Help" from "Menu" for more information)', msecs = 5000)
            else:
                self.ui.date1_de.setEnabled(True)
                self.ui.date2_de.setEnabled(True)
                self.ui.date_btn.setEnabled(True)
                self.ui.sample_btn.setEnabled(False)         
                self.setTimeRange
        except UnicodeDecodeError:
            self.newSession
            self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red}")
            self.ui.statusbar.showMessage('The selected file is invalid! Please select another one (refer to "Help" from "Menu" for more information)', msecs = 5000)            
            pass            

    def setTimeRange(self):
        self.start_folder = self.ui.date1_de.date().toPyDate()
        self.end_folder = self.ui.date2_de.date().toPyDate()
        if self.start_folder > self.end_folder:
            self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red}")
            self.ui.statusbar.showMessage("End date should be greater than start date!", msecs = 4000)
            return
        self.ui.date1_de.setEnabled(False)
        self.ui.date2_de.setEnabled(False)
        self.ui.date_btn.setEnabled(False)
        self.ui.lon_le.setEnabled(True)
        self.ui.lat_le.setEnabled(True)
        self.ui.location_btn.setEnabled(True)
        
    def lockLocation(self):
        self.ui.lon_le.setEnabled(False)
        self.ui.lat_le.setEnabled(False)
        self.ui.location_btn.setEnabled(False)
        if self.ui.lon_le.text() == "":
            self.ui.lon_le.setText("0.00")
        if self.ui.lat_le.text() == "":
            self.ui.lat_le.setText("0.00")
        self.lon = float(self.ui.lon_le.text())  # longitude (lon)
        self.lat = float(self.ui.lat_le.text())  # latitude  (lat)
        self.getParameters()
        
    def getParameters(self):
        self.params_header = extractLine(self.full_path, 3)
        self.params_split = self.params_header.split()
        self.selectParameter()        

    def selectParameter(self):
        self.ui.hs_cx.setEnabled(True)
        self.ui.l_cx.setEnabled(True)
        self.ui.tr_cx.setEnabled(True)
        self.ui.dir_cx.setEnabled(True)
        self.ui.spr_cx.setEnabled(True)
        self.ui.fp_cx.setEnabled(True)
        self.ui.pdir_cx.setEnabled(True)        
        self.ui.pspr_cx.setEnabled(True)
        self.ui.param_btn.setEnabled(True)
        
    def extractValues(self):
        if self.ui.hs_cx.isChecked():
            self.params_list.append(2)
            self.params_names.append(' Hs')
            self.params_units.append(' (m)')
        if self.ui.l_cx.isChecked():
            self.params_list.append(3)
            self.params_names.append(' L')
            self.params_units.append(' (m)')            
        if self.ui.tr_cx.isChecked():
            self.params_list.append(4)
            self.params_names.append(' Tr')
            self.params_units.append(' (s)')            
        if self.ui.dir_cx.isChecked():
            self.params_list.append(5)
            self.params_names.append(' Dir.')
            self.params_units.append(' (d.N)')            
        if self.ui.spr_cx.isChecked():
            self.params_list.append(6)
            self.params_names.append(' Spr.')
            self.params_units.append(' (deg)')
        if self.ui.fp_cx.isChecked():
            self.params_list.append(7)
            self.params_names.append(' fp')
            self.params_units.append(' (Hz)')           
        if self.ui.pdir_cx.isChecked():
            self.params_list.append(8)
            self.params_names.append(' pdir.')
            self.params_units.append(' (d.N)')                                
        if self.ui.pspr_cx.isChecked():
            self.params_list.append(9)
            self.params_names.append(' pspr.')
            self.params_units.append(' (deg)')
        self.ui.hs_cx.setEnabled(False)
        self.ui.l_cx.setEnabled(False)
        self.ui.tr_cx.setEnabled(False)
        self.ui.dir_cx.setEnabled(False)
        self.ui.spr_cx.setEnabled(False)
        self.ui.fp_cx.setEnabled(False)
        self.ui.pdir_cx.setEnabled(False)        
        self.ui.pspr_cx.setEnabled(False)            
        self.ui.param_btn.setEnabled(False)
        self.ui.interp_cb.setEnabled(True)
        self.ui.interp_btn.setEnabled(True)
        self.interpMethodSelect()

    def interpMethodSelect(self):
        self.interp_methods = ['cubic', 'linear', 'nearest']
        self.ui.interp_cb.addItems(self.interp_methods)

    def setMethod(self):
        self.selected_method = self.ui.interp_cb.currentText()
        self.ui.interp_cb.setEnabled(False)
        self.ui.interp_btn.setEnabled(False)
        self.ui.output_btn.setEnabled(True)

    def setOutput(self):
        self.ui.output_le.setText(QtWidgets.QFileDialog.getSaveFileName()[0])
        if self.ui.output_le.text() == "":
            self.ui.output_le.setText("Path to output file")
            return
        elif self.ui.output_le.text() == self.full_path:
            self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:red}")
            self.ui.statusbar.showMessage("Output and input files can't be the same! Please select a proper one", msecs = 4000)            
            return
        self.output_file = self.ui.output_le.text()
        try:
            os.remove(self.output_file)
        except FileNotFoundError:
            pass
        self.ui.output_btn.setEnabled(False)
        self.ui.output_le.setEnabled(False)
        self.ui.go_btn.setEnabled(True)

    def startProcess(self):
        self.error_count = 0
        with open("report.log", "w+") as report_file:
            report_file.write(str("--> Process started at %s <--" % dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
            self.ui.go_btn.setEnabled(False)
            self.days_dt = self.end_folder - self.start_folder + dt.timedelta(days=1)
            self.days = self.days_dt.days
            self.passed_days = 1
            self.current_date = self.start_folder
            #self.timesteps = timestepCounter(self.full_path)
            self.timesteps = 24
            with open(self.output_file, "a") as self.out_file:
                self.out_file.write("Long.: " + str("%2.3f" % self.lon) + "\tLat.: " + str("%2.3f" % self.lat) + "\n\n\t" + "       Time" + "\t\t" + "\t\t".join(self.params_names[0:]) + "\n")
                self.out_file.write("\t\t\t\t" + "\t\t".join(self.params_units[0:]) + "\n\n")                
                #self.out_file.write("--------------------------------------------------------------------------------------------------------------------------------------------------------\n\n")
                while self.current_date <= self.end_folder:
                    self.date_dir = self.current_date.strftime("%Y%m%d")
                    self.filename = os.path.join(self.folder, self.date_dir, self.sample_file)
                    self.first_line, self.last_line = blockIdentifier(self.filename)
                    if self.first_line == 0:
                        self.error_count += 1
                        report_file.write("\n\n--> " + str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +
                                         "\n    **ERROR** @ {date_dir} : folder or included file is missing!".format(date_dir = self.date_dir))
                        self.current_date = self.current_date + dt.timedelta(days=1)
                        self.passed_days += 1
                        continue
                    elif self.first_line == 1:
                        self.error_count += 1
                        report_file.write("\n\n--> " + str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +
                                          "\n    **ERROR** @ {date_dir} : contents of included file is invalid!".format(date_dir = self.date_dir))
                        self.current_date = self.current_date + dt.timedelta(days=1)
                        self.passed_days += 1
                        continue                        
                    self.blockSize = self.last_line - self.first_line + 8
                    self.time_header = extractLine(self.filename, 1)
                    self.header_split = self.time_header.split()
                    self.time_header_2 = extractLine(self.filename, self.last_line + 3)
                    self.header_split_2 = self.time_header_2.split()
                    self.start_date = dt.datetime.strptime(self.header_split[2], "%Y/%m/%d")
                    self.start_time = dt.datetime.strptime(self.header_split[3], "%H:%M:%S")
                    self.start_time_2 = dt.datetime.strptime(self.header_split_2[3], "%H:%M:%S")
                    self.timestep = self.start_time_2 - self.start_time                
                    for i in range(0, self.timesteps):
                        self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;font:italic}")
                        self.ui.statusbar.showMessage("Processing folder {date_dir} timestep {timestep} ...".format(date_dir = self.date_dir, timestep = i))
                        if i != 0:
                            self.first_line = self.first_line + self.blockSize
                            self.last_line = self.last_line + self.blockSize
                        self.lon_container = extractParam(self.filename, self.first_line, self.last_line, 0)
                        self.lat_container = extractParam(self.filename, self.first_line, self.last_line, 1)
                        self.lon_array = listToArray(self.lon_container)
                        self.lat_array = listToArray(self.lat_container)
                        self.out_file.write("\t" + str(self.start_date) + "\t")
                        self.output_list = []
                        
                        for j in self.params_list:
                            self.param_container = extractParam(self.filename, self.first_line, self.last_line, int(j))
                            self.param_array = listToArray(self.param_container)
                            self.points = np.column_stack((self.lon_array, self.lat_array))
                            self.ndlon = np.array(self.lon)
                            self.ndlat = np.array(self.lat)
                            try:
                                self.param_interpolated = interpolate.griddata(self.points, self.param_array, (self.ndlon, self.ndlat), method=self.selected_method)
                                self.second_loop_status = 0
                            except ValueError:
                                report_file.write("\n\n--> " + str(dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")) +
                                                  "\n    **ERROR** @ {date_dir} : contents of included file is invalid!".format(date_dir = self.date_dir))
                                self.second_loop_status = 1
                                break
                            QtWidgets.QApplication.processEvents()
                            self.output_list.append(str("%0.3f" % self.param_interpolated))
                        if self.second_loop_status == 1:
                            break                             
                        self.out_file.write('\t\t'.join(self.output_list[0:]) + '\n')
                        self.completed = int(floor((i + 1) / self.timesteps * 100))                                       
                        #wait = input("PRESS ENTER TO CONTINUE.")            ####                    
                        self.ui.partial_pb.setValue(self.completed)                   
                        self.start_date = self.start_date + self.timestep
                    self.ui.overall_pb.setValue(int(floor(self.passed_days / self.days * 100)))                    
                    self.passed_days += 1
                    self.current_date = self.current_date + dt.timedelta(days=1)
                self.ui.partial_pb.setTextVisible(True)
                self.ui.overall_pb.setTextVisible(True)
                self.ui.partial_pb.setProperty("value", 100)
                self.ui.partial_pb.setFormat("Done!")
                self.ui.overall_pb.setProperty("value", 100)
                self.ui.overall_pb.setFormat("Done!")                
                if self.error_count == 0:
                    self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:green}")
                    self.ui.statusbar.showMessage('The requested job completed successfuly! You can start a new job by choosing "New" from "Menu"')
                elif self.error_count > 0:
                    self.ui.statusbar.setStyleSheet("QStatusBar{padding-left:8px;color:blue}")                   
                    self.ui.statusbar.showMessage('The requested job completed successfuly with {errors} error(s)! Please check "report.log" for more info'.format(errors = self.error_count))
                report_file.write(str("\n\n--> Process finished at %s <--" % dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                report_file.write('\n\n    Total error(s): {errors}'.format(errors = self.error_count))
                    
    def newSession(self):
        self.filename = ""
        self.full_path = ""        
        self.params_split = []
        self.params_list = []
        self.params_names = []
        self.params_units = []    
        self.timestep = None
        self.index = None
        self.selected_param = None
        self.selected_method = None
        self.output_file = None
        self.lon = None
        self.lat = None
        self.start_date = None
        self.start_time = None
        self.ui.folder_btn.setEnabled(True)
        self.ui.folder_le.setEnabled(False)
        self.ui.folder_le.setText("Root folder is the one which contains folders of each date")
        self.ui.sample_le.setText("Select a sample tab file (should be of the same name and type in all date folders)")        
        self.ui.lon_le.setEnabled(False)
        self.ui.lon_le.setText(None)
        self.ui.lat_le.setEnabled(False)
        self.ui.lat_le.setText(None)
        self.ui.location_btn.setEnabled(False)
        self.ui.hs_cx.setEnabled(False)
        self.ui.l_cx.setEnabled(False)
        self.ui.tr_cx.setEnabled(False)
        self.ui.dir_cx.setEnabled(False)
        self.ui.spr_cx.setEnabled(False)
        self.ui.fp_cx.setEnabled(False)
        self.ui.pdir_cx.setEnabled(False)        
        self.ui.pspr_cx.setEnabled(False)            
        self.ui.param_btn.setEnabled(False)
        self.ui.interp_cb.setEnabled(False)
        self.ui.interp_cb.clear()
        self.ui.interp_btn.setEnabled(False)
        self.ui.output_btn.setEnabled(False)
        self.ui.output_le.setEnabled(False)
        self.ui.output_le.setText("Path to output file")
        self.ui.go_btn.setEnabled(False)
        self.ui.overall_pb.setFormat("%p%")
        self.ui.overall_pb.setProperty("value", 0)
        self.ui.partial_pb.setFormat("%p%")
        self.ui.partial_pb.setProperty("value", 0)   

    def aboutDialog(self):
        self.dlg = Ui_Dialog()
        self.dlg.show()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.setFixedSize(756, 450)
    window.show()
    sys.exit(app.exec_())