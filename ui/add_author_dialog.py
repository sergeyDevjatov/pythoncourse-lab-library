# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_author_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddAuthorDialog(object):
    def setupUi(self, AddAuthorDialog):
        AddAuthorDialog.setObjectName("AddAuthorDialog")
        AddAuthorDialog.resize(260, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddAuthorDialog.sizePolicy().hasHeightForWidth())
        AddAuthorDialog.setSizePolicy(sizePolicy)
        AddAuthorDialog.setMinimumSize(QtCore.QSize(260, 170))
        AddAuthorDialog.setMaximumSize(QtCore.QSize(260, 170))
        AddAuthorDialog.setSizeGripEnabled(False)
        AddAuthorDialog.setModal(True)
        self.pushButton = QtWidgets.QPushButton(AddAuthorDialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 140, 211, 23))
        self.pushButton.setObjectName("pushButton")
        self.splitter = QtWidgets.QSplitter(AddAuthorDialog)
        self.splitter.setGeometry(QtCore.QRect(110, 10, 133, 121))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setHandleWidth(13)
        self.splitter.setOpaqueResize(False)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setObjectName("splitter")
        self.name = QtWidgets.QLineEdit(self.splitter)
        self.name.setObjectName("name")
        self.country = QtWidgets.QLineEdit(self.splitter)
        self.country.setObjectName("country")
        self.birth_year = QtWidgets.QLineEdit(self.splitter)
        self.birth_year.setObjectName("birth_year")
        self.death_year = QtWidgets.QLineEdit(self.splitter)
        self.death_year.setObjectName("death_year")
        self.splitter_2 = QtWidgets.QSplitter(AddAuthorDialog)
        self.splitter_2.setGeometry(QtCore.QRect(30, 10, 81, 121))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setOpaqueResize(False)
        self.splitter_2.setChildrenCollapsible(False)
        self.splitter_2.setObjectName("splitter_2")
        self.label = QtWidgets.QLabel(self.splitter_2)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter_2)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AddAuthorDialog)
        self.pushButton.clicked.connect(AddAuthorDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AddAuthorDialog)

    def retranslateUi(self, AddAuthorDialog):
        _translate = QtCore.QCoreApplication.translate
        AddAuthorDialog.setWindowTitle(_translate("AddAuthorDialog", "Добавить автора"))
        self.pushButton.setText(_translate("AddAuthorDialog", "OK"))
        self.label.setText(_translate("AddAuthorDialog", "Имя"))
        self.label_2.setText(_translate("AddAuthorDialog", "Страна"))
        self.label_3.setText(_translate("AddAuthorDialog", "Год рождения"))
        self.label_4.setText(_translate("AddAuthorDialog", "Год смерти"))

