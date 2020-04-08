# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'template.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import main
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from pathlib import Path


class Ui_MainWindow(QWidget):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Analyzer")
        MainWindow.resize(799, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Data = QtWidgets.QWidget(self.centralwidget)
        self.Data.setEnabled(True)
        self.Data.setGeometry(QtCore.QRect(0, 20, 791, 61))
        self.Data.setAutoFillBackground(False)
        self.Data.setObjectName("Data")
        self.dataFrame = QtWidgets.QFrame(self.Data)
        self.dataFrame.setGeometry(QtCore.QRect(30, 0, 741, 61))
        self.dataFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.dataFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.dataFrame.setObjectName("dataFrame")

        # browse for the feature file BUTTON
        self.browseFeature_button = QtWidgets.QPushButton(self.dataFrame)
        self.browseFeature_button.setGeometry(QtCore.QRect(290, 20, 75, 23))
        self.browseFeature_button.setObjectName("browseFeature_button")
        self.browseFeature_button.setToolTip("Choose Feature File")
        self.browseFeature_button.clicked.connect(self.on_click_browse_feature)
        # sets values for features and feature length so they can be checked before they are set
        self.featuresLength = ""
        self.features = []

        # browse for the label file BUTTON
        self.browseLabel_button = QtWidgets.QPushButton(self.dataFrame)
        self.browseLabel_button.setGeometry(QtCore.QRect(620, 20, 75, 23))
        self.browseLabel_button.setObjectName("browseLabel_button")
        self.browseLabel_button.setToolTip("Choose Label File")
        self.browseLabel_button.clicked.connect(self.on_click_browse_label)
        # sets values for labels and label leanght so they can be checked before they are set
        self.labelsLength = ""
        self.labels = []

        self.featureFile_label = QtWidgets.QLabel(self.dataFrame)
        self.featureFile_label.setGeometry(QtCore.QRect(40, 20, 61, 16))
        self.featureFile_label.setObjectName("featureFile_label")

        self.labelFile_label = QtWidgets.QLabel(self.dataFrame)
        self.labelFile_label.setGeometry(QtCore.QRect(400, 20, 61, 21))
        self.labelFile_label.setObjectName("labelFile_label")

        self.data_label = QtWidgets.QLabel(self.dataFrame)
        self.data_label.setGeometry(QtCore.QRect(20, 0, 47, 13))
        self.data_label.setObjectName("data_label")

        # output path of feature file input here LINE EDIT
        self.featureFile_lineedit = QtWidgets.QLineEdit(self.dataFrame)
        self.featureFile_lineedit.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.featureFile_lineedit.setObjectName("featureFile_lineedit")

        # output path of label file input here LINE EDIT
        self.labelFile_lineedit = QtWidgets.QLineEdit(self.dataFrame)
        self.labelFile_lineedit.setGeometry(QtCore.QRect(460, 20, 113, 20))
        self.labelFile_lineedit.setObjectName("labelFile_lineedit")

        self.FeatureSelection = QtWidgets.QWidget(self.centralwidget)
        self.FeatureSelection.setGeometry(QtCore.QRect(30, 110, 741, 421))
        self.FeatureSelection.setObjectName("FeatureSelection")

        self.FSFrame = QtWidgets.QFrame(self.FeatureSelection)
        self.FSFrame.setGeometry(QtCore.QRect(0, 0, 741, 421))
        self.FSFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.FSFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FSFrame.setObjectName("FSFrame")

        self.featureSelection_label = QtWidgets.QLabel(self.FSFrame)
        self.featureSelection_label.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.featureSelection_label.setObjectName("featureSelection_label")

        self.Analysis = QtWidgets.QWidget(self.centralwidget)
        self.Analysis.setGeometry(QtCore.QRect(30, 540, 741, 141))
        self.Analysis.setObjectName("Analysis")

        self.frame = QtWidgets.QFrame(self.Analysis)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.analysis_label = QtWidgets.QLabel(self.frame)
        self.analysis_label.setGeometry(QtCore.QRect(20, 0, 47, 13))
        self.analysis_label.setObjectName("analysis_label")

        self.crossvalidation_checkbox = QtWidgets.QCheckBox(self.frame)
        self.crossvalidation_checkbox.setGeometry(QtCore.QRect(40, 30, 101, 17))
        self.crossvalidation_checkbox.setObjectName("crossvalidation_checkbox")

        self.folds_spinbox = QtWidgets.QSpinBox(self.frame)
        self.folds_spinbox.setGeometry(QtCore.QRect(60, 50, 42, 22))
        self.folds_spinbox.setObjectName("folds_spinbox")

        self.folds_label = QtWidgets.QLabel(self.frame)
        self.folds_label.setGeometry(QtCore.QRect(110, 50, 61, 21))
        self.folds_label.setObjectName("folds_label")

        self.stratified_checkbox = QtWidgets.QCheckBox(self.frame)
        self.stratified_checkbox.setGeometry(QtCore.QRect(60, 80, 70, 17))
        self.stratified_checkbox.setObjectName("stratified_checkbox")

        self.numOfSelectFunc_label = QtWidgets.QLabel(self.frame)
        self.numOfSelectFunc_label.setGeometry(QtCore.QRect(490, 10, 141, 21))
        self.numOfSelectFunc_label.setObjectName("numOfSelectFunc_label")

        self.precent_radiobutton = QtWidgets.QRadioButton(self.frame)
        self.precent_radiobutton.setGeometry(QtCore.QRect(500, 30, 82, 17))
        self.precent_radiobutton.setObjectName("precent_radiobutton")

        self.top_radiobutton = QtWidgets.QRadioButton(self.frame)
        self.top_radiobutton.setGeometry(QtCore.QRect(500, 50, 82, 17))
        self.top_radiobutton.setObjectName("top_radiobutton")

        self.log_radiobutton = QtWidgets.QRadioButton(self.frame)
        self.log_radiobutton.setGeometry(QtCore.QRect(500, 70, 82, 17))
        self.log_radiobutton.setObjectName("log_radiobutton")

        self.percent_spinbox = QtWidgets.QSpinBox(self.frame)
        self.percent_spinbox.setGeometry(QtCore.QRect(540, 30, 41, 16))
        self.percent_spinbox.setObjectName("percent_spinbox")

        self.top_spinbox = QtWidgets.QSpinBox(self.frame)
        self.top_spinbox.setGeometry(QtCore.QRect(540, 50, 42, 22))
        self.top_spinbox.setObjectName("top_spinbox")

        self.trainingTestingSplit_label = QtWidgets.QLabel(self.frame)
        self.trainingTestingSplit_label.setGeometry(QtCore.QRect(250, 20, 111, 16))
        self.trainingTestingSplit_label.setObjectName("trainingTestingSplit_label")
        self.trainingTestingSplit_lineedit = QtWidgets.QLineEdit(self.frame)
        self.trainingTestingSplit_lineedit.setGeometry(QtCore.QRect(250, 50, 113, 20))
        self.trainingTestingSplit_lineedit.setText("")
        self.trainingTestingSplit_lineedit.setObjectName(
            "trainingTestingSplit_lineedit"
        )

        self.Output = QtWidgets.QWidget(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(30, 700, 741, 121))
        self.Output.setObjectName("Output")

        self.frame_2 = QtWidgets.QFrame(self.Output)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 121))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.output_label = QtWidgets.QLabel(self.frame_2)
        self.output_label.setGeometry(QtCore.QRect(20, 0, 61, 16))
        self.output_label.setObjectName("output_label")

        self.output_textbrowser = QtWidgets.QTextBrowser(self.frame_2)
        self.output_textbrowser.setGeometry(QtCore.QRect(140, 10, 421, 61))
        self.output_textbrowser.setObjectName("output_textbrowser")

        self.run_button = QtWidgets.QPushButton(self.frame_2)
        self.run_button.setGeometry(QtCore.QRect(510, 90, 75, 23))
        self.run_button.setObjectName("run_button")

        self.runAndSave_button = QtWidgets.QPushButton(self.frame_2)
        self.runAndSave_button.setGeometry(QtCore.QRect(610, 90, 81, 23))
        self.runAndSave_button.setObjectName("runAndSave_button")

        # Save output path BUTTON
        self.outputBrowse_button = QtWidgets.QPushButton(self.frame_2)
        self.outputBrowse_button.setGeometry(QtCore.QRect(50, 90, 75, 23))
        self.outputBrowse_button.setObjectName("outputBrowse_button")
        self.outputBrowse_button.setToolTip("Choose Output")
        self.outputBrowse_button.clicked.connect(self.on_click_save_output)

        # output path of save output here LINE EDIT
        self.browseOutput_lineedit = QtWidgets.QLineEdit(self.frame_2)
        self.browseOutput_lineedit.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.browseOutput_lineedit.setObjectName("browseOutput_lineedit")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click_browse_feature(self):  # feature file button click
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.featureFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Comma Seperated Values (*.csv)",
            options=options,
        )
        self.output_textbrowser.insertPlainText("Loading Features File...\n")
        if self.featureFilePath:
            self.featureFile_lineedit.insert(self.featureFilePath)
        self.features, self.featuresLength = main.load_features(self.featureFilePath)
        if self.labels:  # Checks to see if a label file has been selected yet
            if (
                self.labelsLength != self.featuresLength
            ):  # makes sure the lenghts of the file are equal
                self.output_textbrowser.insertPlainText(
                    "WARNING: Feature File and Label File lengths do not match\n"
                )
                self.output_textbrowser.insertPlainText(
                    str(self.featuresLength)
                    + " is not equal to "
                    + str(self.labelsLength)
                    + "\n"
                )

            else:
                self.output_textbrowser.insertPlainText("Loading Features Successful\n")
        else:
            self.output_textbrowser.insertPlainText("Loading Features Successful\n")

    def on_click_browse_label(self):  # label file button click
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.labelFilePath, _ = QFileDialog.getOpenFileName(
            self,
            "QFileDialog.getOpenFileName()",
            "",
            "Comma Seperated Values (*.csv)",
            options=options,
        )
        self.output_textbrowser.insertPlainText("Loading Label File...\n")
        if self.labelFilePath:
            self.labelFile_lineedit.insert(self.labelFilePath)
        self.labels, self.labelsLength = main.load_labels(self.labelFilePath)
        if self.features:
            if self.featuresLength != self.labelsLength:
                self.output_textbrowser.insertPlainText(
                    "WARNING: Labels and Feature File lengths do not match\n"
                )
                self.output_textbrowser.insertPlainText(
                    str(self.labelsLength)
                    + " is not equal to "
                    + str(self.featuresLength)
                    + "\n"
                )
            else:
                self.output_textbrowser.insertPlainText("Loading Labels Successful\n")
        else:
            self.output_textbrowser.insertPlainText("Loading Labels Successful\n")

    def on_click_save_output(self):  # output button click
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        outputPath, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getSaveFileName()",
            "",
            ";Text Files (*.txt)",
            options=options,
        )
        if outputPath:
            self.browseOutput_lineedit.insert(outputPath)
        # TODO insert saving of output file

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Feature Selection"))
        self.browseFeature_button.setText(_translate("MainWindow", "Browse"))
        self.browseLabel_button.setText(_translate("MainWindow", "Browse"))
        self.featureFile_label.setText(_translate("MainWindow", "Feature File"))
        self.labelFile_label.setText(_translate("MainWindow", "Label File"))
        self.data_label.setText(_translate("MainWindow", "Data"))
        self.featureSelection_label.setText(
            _translate("MainWindow", " Feature Selection")
        )
        self.analysis_label.setText(_translate("MainWindow", "Analysis"))
        self.crossvalidation_checkbox.setText(
            _translate("MainWindow", "Cross Validation")
        )
        self.folds_label.setText(_translate("MainWindow", "folds"))
        self.stratified_checkbox.setText(_translate("MainWindow", "Stratified"))
        self.numOfSelectFunc_label.setText(
            _translate("MainWindow", "# of select functions")
        )
        self.precent_radiobutton.setText(_translate("MainWindow", "%"))
        self.top_radiobutton.setText(_translate("MainWindow", "Top"))
        self.log_radiobutton.setText(_translate("MainWindow", "Log"))
        self.output_label.setText(_translate("MainWindow", "Output"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.runAndSave_button.setText(_translate("MainWindow", "Run And Save"))
        self.outputBrowse_button.setText(_translate("MainWindow", "Browse"))
        self.trainingTestingSplit_label.setText(
            _translate("MainWindow", "(Training/Testing) Split")
        )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
