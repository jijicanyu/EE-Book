# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Frank/PycharmProjects/EE-Book/src/gui/dialogs/download.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(945, 593)
        self.recipes = QtGui.QTreeView(Dialog)
        self.recipes.setGeometry(QtCore.QRect(10, 20, 301, 441))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recipes.sizePolicy().hasHeightForWidth())
        self.recipes.setSizePolicy(sizePolicy)
        self.recipes.setProperty("showDropIndicator", False)
        self.recipes.setIconSize(QtCore.QSize(16, 16))
        self.recipes.setAnimated(True)
        self.recipes.setHeaderHidden(True)
        self.recipes.setObjectName(_fromUtf8("recipes"))
        self.detail_box = QtGui.QTabWidget(Dialog)
        self.detail_box.setGeometry(QtCore.QRect(331, 10, 581, 577))
        self.detail_box.setObjectName(_fromUtf8("detail_box"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.blurb = QtGui.QLabel(self.tab)
        self.blurb.setText(_fromUtf8(""))
        self.blurb.setWordWrap(True)
        self.blurb.setOpenExternalLinks(True)
        self.blurb.setObjectName(_fromUtf8("blurb"))
        self.verticalLayout.addWidget(self.blurb)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        spacerItem1 = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem2 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.account = QtGui.QGroupBox(self.tab)
        self.account.setObjectName(_fromUtf8("account"))
        self.gridLayout = QtGui.QGridLayout(self.account)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(self.account)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(86, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 2)
        self.username = QtGui.QLineEdit(self.account)
        self.username.setObjectName(_fromUtf8("username"))
        self.gridLayout.addWidget(self.username, 0, 3, 1, 3)
        spacerItem4 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 0, 6, 1, 1)
        self.label_3 = QtGui.QLabel(self.account)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(86, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 2)
        self.password = QtGui.QLineEdit(self.account)
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.gridLayout.addWidget(self.password, 1, 3, 1, 3)
        spacerItem6 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 6, 1, 1)
        self.label_10 = QtGui.QLabel(self.account)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(135, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 2, 1, 1, 3)
        self.captcha = QtGui.QLineEdit(self.account)
        self.captcha.setEchoMode(QtGui.QLineEdit.Normal)
        self.captcha.setObjectName(_fromUtf8("captcha"))
        self.gridLayout.addWidget(self.captcha, 2, 4, 1, 2)
        spacerItem8 = QtGui.QSpacerItem(34, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 2, 6, 1, 1)
        self.show_password = QtGui.QCheckBox(self.account)
        self.show_password.setObjectName(_fromUtf8("show_password"))
        self.gridLayout.addWidget(self.show_password, 3, 0, 1, 2)
        spacerItem9 = QtGui.QSpacerItem(111, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 3, 2, 1, 3)
        self.login_button = QtGui.QPushButton(self.account)
        self.login_button.setObjectName(_fromUtf8("login_button"))
        self.gridLayout.addWidget(self.login_button, 3, 5, 1, 1)
        self.horizontalLayout_3.addWidget(self.account)
        spacerItem10 = QtGui.QSpacerItem(38, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem11 = QtGui.QSpacerItem(388, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem11)
        self.download_button = QtGui.QPushButton(self.tab)
        self.download_button.setObjectName(_fromUtf8("download_button"))
        self.horizontalLayout.addWidget(self.download_button)
        spacerItem12 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.detail_box.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem13, 3, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.custom_tags = QtGui.QLineEdit(self.tab_2)
        self.custom_tags.setObjectName(_fromUtf8("custom_tags"))
        self.gridLayout_3.addWidget(self.custom_tags, 1, 2, 1, 1)
        self.add_title_tag = QtGui.QCheckBox(self.tab_2)
        self.add_title_tag.setObjectName(_fromUtf8("add_title_tag"))
        self.gridLayout_3.addWidget(self.add_title_tag, 0, 0, 1, 1)
        self.detail_box.addTab(self.tab_2, _fromUtf8(""))
        self.count_label = QtGui.QLabel(Dialog)
        self.count_label.setGeometry(QtCore.QRect(20, 490, 256, 16))
        self.count_label.setAlignment(QtCore.Qt.AlignCenter)
        self.count_label.setObjectName(_fromUtf8("count_label"))
        self.label_2.setBuddy(self.username)
        self.label_3.setBuddy(self.password)
        self.label_10.setBuddy(self.password)
        self.label_5.setBuddy(self.custom_tags)

        self.retranslateUi(Dialog)
        self.detail_box.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.account.setTitle(_translate("Dialog", "&Account", None))
        self.label_2.setText(_translate("Dialog", "&username:", None))
        self.label_3.setText(_translate("Dialog", "&password:", None))
        self.label_10.setText(_translate("Dialog", "&captcha:", None))
        self.show_password.setText(_translate("Dialog", "&Show password", None))
        self.login_button.setText(_translate("Dialog", "login", None))
        self.download_button.setText(_translate("Dialog", "download", None))
        self.detail_box.setTabText(self.detail_box.indexOf(self.tab), _translate("Dialog", "&Schedule", None))
        self.label_5.setText(_translate("Dialog", "&Extra  tags:", None))
        self.add_title_tag.setText(_translate("Dialog", "Add &title as tag", None))
        self.detail_box.setTabText(self.detail_box.indexOf(self.tab_2), _translate("Dialog", "&Advanced", None))
        self.count_label.setText(_translate("Dialog", "dd", None))

