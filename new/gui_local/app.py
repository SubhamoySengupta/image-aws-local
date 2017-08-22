# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app.ui'
#
# Created by: PyQt5 UI code generator 5.4.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# custom
import app_mod


class Ui_MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		self.setupUi(self)

	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setMinimumSize(QtCore.QSize(800, 600))
		MainWindow.setMaximumSize(QtCore.QSize(800, 600))
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.console_pipe = QtWidgets.QTextBrowser(self.centralwidget)
		self.console_pipe.setGeometry(QtCore.QRect(10, 100, 781, 421))
		font = QtGui.QFont()
		font.setPointSize(10)
		self.console_pipe.setFont(font)
		self.console_pipe.setStyleSheet("background-color: rgb(48, 48, 48);\n""color: rgb(62, 255, 41);\n""")
		self.console_pipe.setObjectName("console_pipe")
		self.progress_pipe = QtWidgets.QProgressBar(self.centralwidget)
		self.progress_pipe.setGeometry(QtCore.QRect(10, 530, 780, 23))
		self.progress_pipe.setStyleSheet("")
		self.progress_pipe.setProperty("value", 0)
		self.progress_pipe.setObjectName("progress_pipe")
		self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
		self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 781, 81))
		self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
		self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
		self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
		self.horizontalLayout_3.setObjectName("horizontalLayout_3")
		self.verticalLayout_2 = QtWidgets.QVBoxLayout()
		self.verticalLayout_2.setObjectName("verticalLayout_2")
		self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label.setFont(font)
		self.label.setObjectName("label")
		self.verticalLayout_2.addWidget(self.label)
		self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_2.setObjectName("horizontalLayout_2")
		self.run_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.run_btn.setFont(font)
		self.run_btn.setObjectName("run_btn")
		self.horizontalLayout_2.addWidget(self.run_btn)
		self.check_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.check_btn.setFont(font)
		self.check_btn.setObjectName("check_btn")
		self.horizontalLayout_2.addWidget(self.check_btn)
		self.verticalLayout_2.addLayout(self.horizontalLayout_2)
		self.horizontalLayout_3.addLayout(self.verticalLayout_2)
		self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
		self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
		self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line_2.setObjectName("line_2")
		self.horizontalLayout_3.addWidget(self.line_2)
		self.verticalLayout_3 = QtWidgets.QVBoxLayout()
		self.verticalLayout_3.setObjectName("verticalLayout_3")
		self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.label_2.setFont(font)
		self.label_2.setObjectName("label_2")
		self.verticalLayout_3.addWidget(self.label_2)
		self.horizontalLayout = QtWidgets.QHBoxLayout()
		self.horizontalLayout.setObjectName("horizontalLayout")
		self.dryrun_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.dryrun_btn.setFont(font)
		self.dryrun_btn.setObjectName("dryrun_btn")
		self.horizontalLayout.addWidget(self.dryrun_btn)
		self.sync_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.sync_btn.setFont(font)
		self.sync_btn.setObjectName("sync_btn")
		self.horizontalLayout.addWidget(self.sync_btn)
		self.verticalLayout_3.addLayout(self.horizontalLayout)
		self.horizontalLayout_3.addLayout(self.verticalLayout_3)
		self.line = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
		self.line.setFrameShape(QtWidgets.QFrame.VLine)
		self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
		self.line.setObjectName("line")
		self.horizontalLayout_3.addWidget(self.line)
		self.auto_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.auto_btn.setFont(font)
		self.auto_btn.setObjectName("auto_btn")
		self.horizontalLayout_3.addWidget(self.auto_btn)
		self.configure_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.configure_btn.setFont(font)
		self.configure_btn.setObjectName("configure_btn")
		self.horizontalLayout_3.addWidget(self.configure_btn)
		self.help_btn = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
		font = QtGui.QFont()
		font.setPointSize(14)
		self.help_btn.setFont(font)
		self.help_btn.setObjectName("help_btn")
		self.horizontalLayout_3.addWidget(self.help_btn)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

		# custom
		self.check_btn.clicked.connect(self.resize_check)
		self.run_btn.clicked.connect(self.resize_run)
		self.dryrun_btn.clicked.connect(self.sync_dryrun)
		self.sync_btn.clicked.connect(self.sync_sync)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Resize"))
		self.run_btn.setText(_translate("MainWindow", "Run"))
		self.check_btn.setText(_translate("MainWindow", "Check"))
		self.label_2.setText(_translate("MainWindow", "Upload"))
		self.dryrun_btn.setText(_translate("MainWindow", "Dryrun"))
		self.sync_btn.setText(_translate("MainWindow", "Sync"))
		self.auto_btn.setText(_translate("MainWindow", "Auto"))
		self.configure_btn.setText(_translate("MainWindow", "Configure"))
		self.help_btn.setText(_translate("MainWindow", "Help"))

	def update_console_pipe(self, code, msg):
		if code == 1:
			self.console_pipe.append(msg)
		elif code == 2:
			self.console_pipe.setText(msg)

	def resize_check(self):
		self.th = resize_check_class()
		self.th.progress.connect(self.progress_pipe.setValue)
		self.th.message.connect(self.update_console_pipe)
		self.th.finished.connect(self.progress_pipe.setValue)
		self.th.start()

	def resize_run(self):
		self.th = resize_run_class()
		self.th.progress.connect(self.progress_pipe.setValue)
		self.th.message.connect(self.update_console_pipe)
		self.th.finished.connect(self.progress_pipe.setValue)
		self.th.start()

	def sync_dryrun(self):
		self.th = sync_dryrun_class()
		self.th.progress.connect(self.progress_pipe.setValue)
		self.th.message.connect(self.update_console_pipe)
		self.th.finished.connect(self.progress_pipe.setValue)
		self.th.start()

	def sync_sync(self):
		self.th = sync_sync_class()
		self.th.progress.connect(self.progress_pipe.setValue)
		self.th.message.connect(self.update_console_pipe)
		self.th.finished.connect(self.progress_pipe.setValue)
		self.th.start()


class sync_sync_class(QtCore.QThread):
	progress = QtCore.pyqtSignal([int])
	message = QtCore.pyqtSignal(int, str)
	finished = QtCore.pyqtSignal(int)

	def run(self):
		self.progress.emit(0)
		app_mod.hyve_sync.sync(self.message, self.progress)
		self.finished.emit(100)


class sync_dryrun_class(QtCore.QThread):
	progress = QtCore.pyqtSignal([int])
	message = QtCore.pyqtSignal(int, str)
	finished = QtCore.pyqtSignal(int)

	def run(self):
		self.progress.emit(0)
		app_mod.hyve_sync.dryrun(self.message, self.progress)
		self.finished.emit(100)


class resize_run_class(QtCore.QThread):
	progress = QtCore.pyqtSignal([int])
	message = QtCore.pyqtSignal(int, str)
	finished = QtCore.pyqtSignal(int)

	def run(self):
		self.progress.emit(0)
		app_mod.resizer.run_8(self.message, self.progress)
		self.finished.emit(100)


class resize_check_class(QtCore.QThread):
	progress = QtCore.pyqtSignal([int])
	message = QtCore.pyqtSignal(int, str)
	finished = QtCore.pyqtSignal(int)

	def run(self):
		self.progress.emit(0)
		app_mod.resizer.check(self.message, self.progress)
		self.finished.emit(100)
