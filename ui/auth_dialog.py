# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'auth_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthDialog(object):
    def setupUi(self, AuthDialog):
        AuthDialog.setObjectName("AuthDialog")
        AuthDialog.resize(220, 95)
        AuthDialog.setMinimumSize(QtCore.QSize(220, 95))
        AuthDialog.setMaximumSize(QtCore.QSize(220, 95))
        AuthDialog.setModal(True)
        self.widget = QtWidgets.QWidget(AuthDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 201, 77))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.login = QtWidgets.QLineEdit(self.widget)
        self.login.setDragEnabled(True)
        self.login.setObjectName("login")
        self.gridLayout.addWidget(self.login, 0, 1, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setDragEnabled(True)
        self.password.setReadOnly(False)
        self.password.setPlaceholderText("")
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 1, 1, 2)
        self.okButton = QtWidgets.QPushButton(self.widget)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(self.widget)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 2, 2, 1, 1)
        self.gridLayout.addWidget(self.okButton, 2, 0, 1, 1)

        self.retranslateUi(AuthDialog)
        self.cancelButton.clicked.connect(AuthDialog.reject)
        self.okButton.clicked.connect(AuthDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AuthDialog)

    def retranslateUi(self, AuthDialog):
        _translate = QtCore.QCoreApplication.translate
        AuthDialog.setWindowTitle(_translate("AuthDialog", "Авторизация"))
        self.label.setText(_translate("AuthDialog", "Логин"))
        self.label_2.setText(_translate("AuthDialog", "Пароль"))
        self.cancelButton.setText(_translate("AuthDialog", "Отмена"))
        self.okButton.setText(_translate("AuthDialog", "ОК"))

