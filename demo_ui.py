# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo_ui.ui'
#
# Created: Thu Sep  3 23:25:12 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(320, 240)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tab_demo = QtGui.QTabWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_demo.sizePolicy().hasHeightForWidth())
        self.tab_demo.setSizePolicy(sizePolicy)
        self.tab_demo.setObjectName(_fromUtf8("tab_demo"))
        self.tab_gpio = QtGui.QWidget()
        self.tab_gpio.setObjectName(_fromUtf8("tab_gpio"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab_gpio)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.gb_leds = QtGui.QGroupBox(self.tab_gpio)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_leds.sizePolicy().hasHeightForWidth())
        self.gb_leds.setSizePolicy(sizePolicy)
        self.gb_leds.setObjectName(_fromUtf8("gb_leds"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.gb_leds)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.rbox_1 = QtGui.QRadioButton(self.gb_leds)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbox_1.setFont(font)
        self.rbox_1.setChecked(True)
        self.rbox_1.setObjectName(_fromUtf8("rbox_1"))
        self.verticalLayout_6.addWidget(self.rbox_1)
        self.rbox_2 = QtGui.QRadioButton(self.gb_leds)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbox_2.setFont(font)
        self.rbox_2.setObjectName(_fromUtf8("rbox_2"))
        self.verticalLayout_6.addWidget(self.rbox_2)
        self.rbox_3 = QtGui.QRadioButton(self.gb_leds)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.rbox_3.setFont(font)
        self.rbox_3.setObjectName(_fromUtf8("rbox_3"))
        self.verticalLayout_6.addWidget(self.rbox_3)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.horizontalLayout_4.addWidget(self.gb_leds)
        self.gb_buttons = QtGui.QGroupBox(self.tab_gpio)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gb_buttons.sizePolicy().hasHeightForWidth())
        self.gb_buttons.setSizePolicy(sizePolicy)
        self.gb_buttons.setObjectName(_fromUtf8("gb_buttons"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.gb_buttons)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.verticalLayout_7 = QtGui.QVBoxLayout()
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.lbl_btn_b1 = QtGui.QLabel(self.gb_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_btn_b1.sizePolicy().hasHeightForWidth())
        self.lbl_btn_b1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_btn_b1.setFont(font)
        self.lbl_btn_b1.setObjectName(_fromUtf8("lbl_btn_b1"))
        self.horizontalLayout_2.addWidget(self.lbl_btn_b1)
        self.lbl_btn_1 = QtGui.QLabel(self.gb_buttons)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_btn_1.setFont(font)
        self.lbl_btn_1.setWordWrap(True)
        self.lbl_btn_1.setObjectName(_fromUtf8("lbl_btn_1"))
        self.horizontalLayout_2.addWidget(self.lbl_btn_1)
        self.verticalLayout_7.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lbl_btn_b2 = QtGui.QLabel(self.gb_buttons)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_btn_b2.sizePolicy().hasHeightForWidth())
        self.lbl_btn_b2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_btn_b2.setFont(font)
        self.lbl_btn_b2.setObjectName(_fromUtf8("lbl_btn_b2"))
        self.horizontalLayout_5.addWidget(self.lbl_btn_b2)
        self.lbl_btn_2 = QtGui.QLabel(self.gb_buttons)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_btn_2.setFont(font)
        self.lbl_btn_2.setWordWrap(True)
        self.lbl_btn_2.setObjectName(_fromUtf8("lbl_btn_2"))
        self.horizontalLayout_5.addWidget(self.lbl_btn_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_4.addWidget(self.gb_buttons)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.btn_exit = QtGui.QPushButton(self.tab_gpio)
        self.btn_exit.setObjectName(_fromUtf8("btn_exit"))
        self.verticalLayout_5.addWidget(self.btn_exit)
        self.tab_demo.addTab(self.tab_gpio, _fromUtf8(""))
        self.tab_dimmer = QtGui.QWidget()
        self.tab_dimmer.setObjectName(_fromUtf8("tab_dimmer"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.tab_dimmer)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.lbl_dimmer = QtGui.QLabel(self.tab_dimmer)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_dimmer.sizePolicy().hasHeightForWidth())
        self.lbl_dimmer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_dimmer.setFont(font)
        self.lbl_dimmer.setObjectName(_fromUtf8("lbl_dimmer"))
        self.verticalLayout_3.addWidget(self.lbl_dimmer)
        self.dial_dimmer = QtGui.QDial(self.tab_dimmer)
        self.dial_dimmer.setEnabled(False)
        self.dial_dimmer.setSliderPosition(50)
        self.dial_dimmer.setNotchesVisible(True)
        self.dial_dimmer.setObjectName(_fromUtf8("dial_dimmer"))
        self.verticalLayout_3.addWidget(self.dial_dimmer)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.tab_demo.addTab(self.tab_dimmer, _fromUtf8(""))
        self.tab_servo = QtGui.QWidget()
        self.tab_servo.setObjectName(_fromUtf8("tab_servo"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tab_servo)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.lbl_servo = QtGui.QLabel(self.tab_servo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_servo.sizePolicy().hasHeightForWidth())
        self.lbl_servo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_servo.setFont(font)
        self.lbl_servo.setObjectName(_fromUtf8("lbl_servo"))
        self.verticalLayout.addWidget(self.lbl_servo)
        self.dial_servo = QtGui.QDial(self.tab_servo)
        self.dial_servo.setEnabled(False)
        self.dial_servo.setSliderPosition(50)
        self.dial_servo.setNotchesVisible(True)
        self.dial_servo.setObjectName(_fromUtf8("dial_servo"))
        self.verticalLayout.addWidget(self.dial_servo)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tab_demo.addTab(self.tab_servo, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.tab_demo)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tab_demo.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.gb_leds.setTitle(_translate("MainWindow", "LEDs", None))
        self.rbox_1.setText(_translate("MainWindow", "LED 1", None))
        self.rbox_2.setText(_translate("MainWindow", "LED 2", None))
        self.rbox_3.setText(_translate("MainWindow", "Toggle", None))
        self.gb_buttons.setTitle(_translate("MainWindow", "Buttons", None))
        self.lbl_btn_b1.setText(_translate("MainWindow", "B1", None))
        self.lbl_btn_1.setText(_translate("MainWindow", "OFF", None))
        self.lbl_btn_b2.setText(_translate("MainWindow", "B2", None))
        self.lbl_btn_2.setText(_translate("MainWindow", "OFF", None))
        self.btn_exit.setText(_translate("MainWindow", "Exit", None))
        self.tab_demo.setTabText(self.tab_demo.indexOf(self.tab_gpio), _translate("MainWindow", "LEDs/Buttons", None))
        self.lbl_dimmer.setText(_translate("MainWindow", "LED Dimmer Pin 22", None))
        self.tab_demo.setTabText(self.tab_demo.indexOf(self.tab_dimmer), _translate("MainWindow", "LED Dimmer", None))
        self.lbl_servo.setText(_translate("MainWindow", "Servo Demo Pin 26", None))
        self.tab_demo.setTabText(self.tab_demo.indexOf(self.tab_servo), _translate("MainWindow", "Servo Demo", None))

