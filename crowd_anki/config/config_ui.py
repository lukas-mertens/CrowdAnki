# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/config.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(825, 726)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.group_snapshot = QtWidgets.QGroupBox(Dialog)
        self.group_snapshot.setObjectName("group_snapshot")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_snapshot)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lbl_snapshot_path = QtWidgets.QLabel(self.group_snapshot)
        self.lbl_snapshot_path.setObjectName("lbl_snapshot_path")
        self.horizontalLayout_2.addWidget(self.lbl_snapshot_path)
        self.textedit_snapshot_path = QtWidgets.QLineEdit(self.group_snapshot)
        self.textedit_snapshot_path.setObjectName("textedit_snapshot_path")
        self.horizontalLayout_2.addWidget(self.textedit_snapshot_path)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.cb_automated_snapshot = QtWidgets.QCheckBox(self.group_snapshot)
        self.cb_automated_snapshot.setObjectName("cb_automated_snapshot")
        self.verticalLayout_3.addWidget(self.cb_automated_snapshot)
        self.lbl_snapshot = QtWidgets.QLabel(self.group_snapshot)
        self.lbl_snapshot.setObjectName("lbl_snapshot")
        self.verticalLayout_3.addWidget(self.lbl_snapshot)
        self.textedit_snapshot_root_decks = QtWidgets.QPlainTextEdit(self.group_snapshot)
        self.textedit_snapshot_root_decks.setObjectName("textedit_snapshot_root_decks")
        self.verticalLayout_3.addWidget(self.textedit_snapshot_root_decks)
        self.verticalLayout_2.addWidget(self.group_snapshot)
        self.group_deck_import = QtWidgets.QGroupBox(Dialog)
        self.group_deck_import.setObjectName("group_deck_import")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.group_deck_import)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.cb_ignore_move_cards = QtWidgets.QCheckBox(self.group_deck_import)
        self.cb_ignore_move_cards.setObjectName("cb_ignore_move_cards")
        self.verticalLayout_5.addWidget(self.cb_ignore_move_cards)
        self.verticalLayout_2.addWidget(self.group_deck_import)
        self.group_deck_export = QtWidgets.QGroupBox(Dialog)
        self.group_deck_export.setObjectName("group_deck_export")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.group_deck_export)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lbl_deck_sort = QtWidgets.QLabel(self.group_deck_export)
        self.lbl_deck_sort.setObjectName("lbl_deck_sort")
        self.verticalLayout_4.addWidget(self.lbl_deck_sort)
        self.textedit_deck_sort_methods = QtWidgets.QPlainTextEdit(self.group_deck_export)
        self.textedit_deck_sort_methods.setObjectName("textedit_deck_sort_methods")
        self.verticalLayout_4.addWidget(self.textedit_deck_sort_methods)
        self.cb_reverse_sort = QtWidgets.QCheckBox(self.group_deck_export)
        self.cb_reverse_sort.setObjectName("cb_reverse_sort")
        self.verticalLayout_4.addWidget(self.cb_reverse_sort)
        self.verticalLayout_2.addWidget(self.group_deck_export)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.tb_instructions = QtWidgets.QTextBrowser(Dialog)
        self.tb_instructions.setLineWidth(1)
        self.tb_instructions.setObjectName("tb_instructions")
        self.horizontalLayout.addWidget(self.tb_instructions)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CrowdAnki Configuration"))
        self.group_snapshot.setTitle(_translate("Dialog", "Snapshot"))
        self.lbl_snapshot_path.setText(_translate("Dialog", "Snapshot Path:"))
        self.cb_automated_snapshot.setText(_translate("Dialog", "Automated Snapshot"))
        self.lbl_snapshot.setText(_translate("Dialog", "Snapshot Root Decks (separated by comma)"))
        self.group_deck_import.setTitle(_translate("Dialog", "Import"))
        self.cb_ignore_move_cards.setText(_translate("Dialog", "Do Not Move Existing Cards"))
        self.group_deck_export.setTitle(_translate("Dialog", "Export"))
        self.lbl_deck_sort.setText(_translate("Dialog", "Deck Sort Method(s) (separated by comma)"))
        self.cb_reverse_sort.setText(_translate("Dialog", "Reverse Sort Order"))
        self.tb_instructions.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Snapshot</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Snapshot Path</span>: The path for base directory where the CrowdAnki snapshot would be written to.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Default</span>: `user_files` subdirectory of the extension directory.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Automated Snapshot</span>: Whether to perform the snapshot automatically on opening/closing the application and on switching the profile.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Default</span>: `false` - this is an experimental feature and it\'s disabled by default.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Snapshot Root Decks</span>: A list of names of the decks that should be considered `root`. When CrowdAnki creates a snapshot it\'ll create a separate git repository for each `root` deck.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Default</span>: Each deck with no children is considered `root`.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Example</span>: Let\'s assume that you have the following decks in your collection: `a` (with sub-decks `b` and `c`), and  `d`. By default CrowdAnki is going to create 3 separate repositories - `a::b`, `a::c` and `d`. If you are to add `a` to `snapshot_root_decks` then CrowdAnki would create 2 repositories instead -  `a` and `d`. The information for sub-decks `b` and `c` would be stored within repository `a` in this case.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Import</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Do Not Move Existing Cards</span>: By default on import of a CrowdAnki deck file, when a note already exists in Anki itself, all notes will be updated and placed in the deck set in the deck file. Tick this box if you wish only to have the notes updated, but left in their current deck. See <a href=\"https://github.com/Stvad/CrowdAnki/issues/23\"><span style=\" text-decoration: underline; color:#2980b9;\">this Issue</span></a> on the CrowdAnki Github Repo for more info.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt;\">Export</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Deck Sort Methods</span>: Methods with which the deck will be sorted. If multiple sorting methods are provided then each sorting method will be applied in order.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" text-decoration: underline;\">Options</span>: <span style=\" font-style:italic;\">none, guid, flag, tag, note_model_name, note_model_id, field1, </span>and<span style=\" font-style:italic;\"> field2.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Reverse Sort Order</span>: Swap the order of the notes, after all sorting.</p></body></html>"))
