from PyQt5.QtWidgets import QApplication
import sys
import app


if __name__ == '__main__':
	parent_app = QApplication(sys.argv)
	main_window = app.Ui_MainWindow()
	main_window.show()
	sys.exit(parent_app.exec_())
