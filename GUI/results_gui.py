# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'results_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class ResultsGui:
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1097, 759)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(50, 90, 1011, 511))
        self.tableView.setObjectName("tableView")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(360, 30, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.filter_btn = QtWidgets.QPushButton(Dialog)
        self.filter_btn.setGeometry(QtCore.QRect(210, 640, 93, 28))
        self.filter_btn.setObjectName("filter_btn")
        self.filter_col_btn = QtWidgets.QRadioButton(Dialog)
        self.filter_col_btn.setGeometry(QtCore.QRect(330, 640, 95, 21))
        self.filter_col_btn.setObjectName("filter_col_btn")
        self.filter_row_btn = QtWidgets.QRadioButton(Dialog)
        self.filter_row_btn.setGeometry(QtCore.QRect(440, 640, 95, 20))
        self.filter_row_btn.setObjectName("filter_row_btn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Your search results "))
        self.filter_btn.setText(_translate("Dialog", "Filter"))
        self.filter_col_btn.setText(_translate("Dialog", "By column"))
        self.filter_row_btn.setText(_translate("Dialog", "By row"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = ResultsGui()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
