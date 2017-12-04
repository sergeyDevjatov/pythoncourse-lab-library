# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_book_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddBookDialog(object):
    def setupUi(self, AddBookDialog):
        AddBookDialog.setObjectName("AddBookDialog")
        AddBookDialog.resize(290, 170)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddBookDialog.sizePolicy().hasHeightForWidth())
        AddBookDialog.setSizePolicy(sizePolicy)
        AddBookDialog.setMinimumSize(QtCore.QSize(290, 170))
        AddBookDialog.setMaximumSize(QtCore.QSize(290, 170))
        AddBookDialog.setSizeGripEnabled(False)
        AddBookDialog.setModal(True)
        self.pushButton = QtWidgets.QPushButton(AddBookDialog)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 140, 271, 23))
        self.pushButton.setObjectName("pushButton")
        self.widget = QtWidgets.QWidget(AddBookDialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 271, 126))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.author = QtWidgets.QComboBox(self.widget)
        self.author.setCurrentText("")
        self.author.setObjectName("author")
        self.gridLayout.addWidget(self.author, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.title = QtWidgets.QLineEdit(self.widget)
        self.title.setObjectName("title")
        self.gridLayout.addWidget(self.title, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.pages_count = QtWidgets.QSpinBox(self.widget)
        self.pages_count.setMinimum(-10000)
        self.pages_count.setMaximum(10000)
        self.pages_count.setProperty("value", 300)
        self.pages_count.setObjectName("pages_count")
        self.gridLayout.addWidget(self.pages_count, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.publisher = QtWidgets.QLineEdit(self.widget)
        self.publisher.setObjectName("publisher")
        self.gridLayout.addWidget(self.publisher, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.publishing_year = QtWidgets.QSpinBox(self.widget)
        self.publishing_year.setMinimum(-10000)
        self.publishing_year.setMaximum(10000)
        self.publishing_year.setProperty("value", 1900)
        self.publishing_year.setDisplayIntegerBase(10)
        self.publishing_year.setObjectName("publishing_year")
        self.gridLayout.addWidget(self.publishing_year, 4, 1, 1, 1)

        self.retranslateUi(AddBookDialog)
        self.pushButton.clicked.connect(AddBookDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(AddBookDialog)

    def retranslateUi(self, AddBookDialog):
        _translate = QtCore.QCoreApplication.translate
        AddBookDialog.setWindowTitle(_translate("AddBookDialog", "Добавить книгу"))
        self.pushButton.setText(_translate("AddBookDialog", "OK"))
        self.label_5.setText(_translate("AddBookDialog", "Автор"))
        self.label_6.setText(_translate("AddBookDialog", "Название"))
        self.label_3.setText(_translate("AddBookDialog", "Количество страниц"))
        self.label_2.setText(_translate("AddBookDialog", "Издательство"))
        self.label_4.setText(_translate("AddBookDialog", "Год издания"))

