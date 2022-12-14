# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'username_taken.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class FilterByRow:
    def setupUi(self, df_operations_rows_window):
        df_operations_rows_window.setObjectName("df_operations_window")
        df_operations_rows_window.resize(421, 293)
        self.label = QtWidgets.QLabel(df_operations_rows_window)
        self.label.setGeometry(QtCore.QRect(120, 30, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # User input column name
        self.ui_column_name = QtWidgets.QLineEdit(df_operations_rows_window)
        self.ui_column_name.setGeometry(QtCore.QRect(160, 70, 113, 22))
        self.ui_column_name.setObjectName("ui_column_name")
        self.row_results_btn = QtWidgets.QPushButton(df_operations_rows_window)
        self.row_results_btn.setGeometry(QtCore.QRect(160, 210, 111, 28))

        # Show search results button
        self.row_results_btn.setObjectName("show_results_btn")
        self.label_2 = QtWidgets.QLabel(df_operations_rows_window)
        self.label_2.setGeometry(QtCore.QRect(120, 120, 321, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # User input row name
        self.ui_row_name = QtWidgets.QLineEdit(df_operations_rows_window)
        self.ui_row_name.setGeometry(QtCore.QRect(160, 160, 113, 22))
        self.ui_row_name.setObjectName("ui_column_name_2")

        self.retranslateUi(df_operations_rows_window)
        QtCore.QMetaObject.connectSlotsByName(df_operations_rows_window)

    def retranslateUi(self, df_operations_row_window):
        _translate = QtCore.QCoreApplication.translate
        df_operations_row_window.setWindowTitle(_translate("df_operations_window", "Show row data"))
        self.label.setText(_translate("df_operations_window", "Enter the column name"))
        self.row_results_btn.setText(_translate("df_operations_window", "Show results"))
        self.label_2.setText(_translate("df_operations_window", "What are you looking for?"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    filter_row = QtWidgets.QDialog()
    ui_filter_row = FilterByRow()
    ui_filter_row.setupUi(filter_row)
    filter_row.show()
    sys.exit(app.exec_())
