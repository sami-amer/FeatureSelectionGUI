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
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(786, 632)
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
        
        self.featureFile_lineedit = QtWidgets.QLineEdit(self.dataFrame)
        self.featureFile_lineedit.setGeometry(QtCore.QRect(110, 20, 113, 20))
        self.featureFile_lineedit.setObjectName("featureFile_lineedit")
        
        self.labelFile_lineedit = QtWidgets.QLineEdit(self.dataFrame)
        self.labelFile_lineedit.setGeometry(QtCore.QRect(460, 20, 113, 20))
        self.labelFile_lineedit.setObjectName("labelFile_lineedit")
        
        self.FeatureSelection = QtWidgets.QWidget(self.centralwidget)
        self.FeatureSelection.setGeometry(QtCore.QRect(30, 90, 741, 306))
        self.FeatureSelection.setObjectName("FeatureSelection")
        
        self.FSFrame = QtWidgets.QFrame(self.FeatureSelection)
        self.FSFrame.setGeometry(QtCore.QRect(0, 0, 741, 306))
        self.FSFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.FSFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.FSFrame.setObjectName("FSFrame")
        
        self.featureSelection_label = QtWidgets.QLabel(self.FSFrame)
        self.featureSelection_label.setGeometry(QtCore.QRect(20, 0, 91, 16))
        self.featureSelection_label.setObjectName("featureSelection_label")
        
        self.groupSAOLA_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.groupSAOLA_checkbox.setGeometry(QtCore.QRect(20, 30, 91, 17))
        self.groupSAOLA_checkbox.setObjectName("groupSAOLA_checkbox")
        
        self.sparseGroupLASSO_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.sparseGroupLASSO_checkbox.setGeometry(QtCore.QRect(20, 60, 131, 17))
        self.sparseGroupLASSO_checkbox.setObjectName("sparseGroupLASSO_checkbox")
        
        self.groupLASSO_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.groupLASSO_checkbox.setGeometry(QtCore.QRect(20, 90, 91, 17))
        self.groupLASSO_checkbox.setObjectName("groupLASSO_checkbox")
        
        self.fastOSFS_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.fastOSFS_checkbox.setGeometry(QtCore.QRect(20, 120, 70, 17))
        self.fastOSFS_checkbox.setObjectName("fastOSFS_checkbox")
        
        self.OSFS_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.OSFS_checkbox.setGeometry(QtCore.QRect(20, 150, 70, 17))
        self.OSFS_checkbox.setObjectName("OSFS_checkbox")
        
        self.SAOLA_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SAOLA_checkbox.setGeometry(QtCore.QRect(20, 180, 70, 17))
        self.SAOLA_checkbox.setObjectName("SAOLA_checkbox")
        
        self.alphaInvesting_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.alphaInvesting_checkbox.setGeometry(QtCore.QRect(20, 210, 101, 17))
        self.alphaInvesting_checkbox.setObjectName("alphaInvesting_checkbox")
        
        self.minMaxMarkovBlanket_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.minMaxMarkovBlanket_checkbox.setGeometry(QtCore.QRect(20, 240, 141, 17))
        self.minMaxMarkovBlanket_checkbox.setObjectName("minMaxMarkovBlanket_checkbox")
        
        self.checkBox_9 = QtWidgets.QCheckBox(self.FSFrame)
        self.checkBox_9.setGeometry(QtCore.QRect(20, 270, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        
        self.HITON_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.HITON_checkbox.setGeometry(QtCore.QRect(605, 210, 70, 17))
        self.HITON_checkbox.setObjectName("HITON_checkbox")
        
        self.SES_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SES_checkbox.setGeometry(QtCore.QRect(605, 90, 70, 17))
        self.SES_checkbox.setObjectName("SES_checkbox")
        
        self.randomForest_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.randomForest_checkbox.setGeometry(QtCore.QRect(605, 30, 101, 17))
        self.randomForest_checkbox.setObjectName("randomForest_checkbox")
        
        self.gradientBoosting_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.gradientBoosting_checkbox.setGeometry(QtCore.QRect(605, 120, 111, 17))
        self.gradientBoosting_checkbox.setObjectName("gradientBoosting_checkbox")
        
        self.regularizedRandomForest_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.regularizedRandomForest_checkbox.setGeometry(QtCore.QRect(190, 30, 156, 17))
        self.regularizedRandomForest_checkbox.setObjectName("regularizedRandomForest_checkbox")
        
        self.guidedRegularizedRandomForest_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.guidedRegularizedRandomForest_checkbox.setGeometry(QtCore.QRect(190, 60, 211, 17))
        self.guidedRegularizedRandomForest_checkbox.setObjectName("guidedRegularizedRandomForest_checkbox")
        
        self.RFgroove_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.RFgroove_checkbox.setGeometry(QtCore.QRect(190, 90, 70, 17))
        self.RFgroove_checkbox.setObjectName("RFgroove_checkbox")
        
        self.infFS_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.infFS_checkbox.setGeometry(QtCore.QRect(190, 120, 70, 17))
        self.infFS_checkbox.setObjectName("infFS_checkbox")
        
        self.infiniteLatenFeatureSelection_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.infiniteLatenFeatureSelection_checkbox.setGeometry(QtCore.QRect(190, 150, 181, 17))
        self.infiniteLatenFeatureSelection_checkbox.setObjectName("infiniteLatenFeatureSelection_checkbox")
        
        self.eigenvectorCentrality_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.eigenvectorCentrality_checkbox.setGeometry(QtCore.QRect(190, 180, 131, 17))
        self.eigenvectorCentrality_checkbox.setObjectName("eigenvectorCentrality_checkbox")
        
        self.quickReduct_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.quickReduct_checkbox.setGeometry(QtCore.QRect(190, 210, 91, 17))
        self.quickReduct_checkbox.setObjectName("quickReduct_checkbox")
        
        self.FSDAARHueristicRST_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.FSDAARHueristicRST_checkbox.setGeometry(QtCore.QRect(190, 240, 136, 17))
        self.FSDAARHueristicRST_checkbox.setObjectName("FSDAARHueristicRST_checkbox")
        
        self.FSnearOptfvprsFRST_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.FSnearOptfvprsFRST_checkbox.setGeometry(QtCore.QRect(190, 270, 136, 17))
        self.FSnearOptfvprsFRST_checkbox.setObjectName("FSnearOptfvprsFRST_checkbox")
        
        self.tTest_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.tTest_checkbox.setGeometry(QtCore.QRect(605, 175, 70, 17))
        self.tTest_checkbox.setObjectName("tTest_checkbox")
        
        self.chiSquare_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.chiSquare_checkbox.setGeometry(QtCore.QRect(605, 60, 70, 17))
        self.chiSquare_checkbox.setObjectName("chiSquare_checkbox")
        
        self.CFS_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.CFS_checkbox.setGeometry(QtCore.QRect(605, 145, 70, 17))
        self.CFS_checkbox.setObjectName("CFS_checkbox")
        
        self.fisherScore_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.fisherScore_checkbox.setGeometry(QtCore.QRect(495, 270, 91, 17))
        self.fisherScore_checkbox.setObjectName("fisherScore_checkbox")
        
        self.HSICLasso_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.HSICLasso_checkbox.setGeometry(QtCore.QRect(495, 240, 70, 17))
        self.HSICLasso_checkbox.setObjectName("HSICLasso_checkbox")
        
        self.LASSO_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.LASSO_checkbox.setGeometry(QtCore.QRect(390, 210, 66, 17))
        self.LASSO_checkbox.setObjectName("LASSO_checkbox")
        
        self.L1SVM_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.L1SVM_checkbox.setGeometry(QtCore.QRect(390, 240, 56, 17))
        self.L1SVM_checkbox.setObjectName("L1SVM_checkbox")
        
        self.MRMR_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.MRMR_checkbox.setGeometry(QtCore.QRect(390, 90, 56, 17))
        self.MRMR_checkbox.setObjectName("MRMR_checkbox")
        
        self.boruta_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.boruta_checkbox.setGeometry(QtCore.QRect(495, 145, 56, 17))
        self.boruta_checkbox.setObjectName("boruta_checkbox")
        
        self.CMIM_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.CMIM_checkbox.setGeometry(QtCore.QRect(390, 150, 56, 17))
        self.CMIM_checkbox.setObjectName("CMIM_checkbox")
        
        self.elasticNets_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.elasticNets_checkbox.setGeometry(QtCore.QRect(390, 270, 86, 17))
        self.elasticNets_checkbox.setObjectName("elasticNets_checkbox")
        
        self.JM_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.JM_checkbox.setGeometry(QtCore.QRect(390, 120, 46, 17))
        self.JM_checkbox.setObjectName("JM_checkbox")
        
        self.GA_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.GA_checkbox.setGeometry(QtCore.QRect(495, 175, 36, 17))
        self.GA_checkbox.setObjectName("GA_checkbox")
        
        self.SPEC_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SPEC_checkbox.setGeometry(QtCore.QRect(390, 60, 46, 17))
        self.SPEC_checkbox.setObjectName("SPEC_checkbox")
        
        self.relief_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.relief_checkbox.setGeometry(QtCore.QRect(390, 30, 46, 17))
        self.relief_checkbox.setObjectName("relief_checkbox")
        
        self.ridge_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.ridge_checkbox.setGeometry(QtCore.QRect(495, 210, 56, 17))
        self.ridge_checkbox.setObjectName("ridge_checkbox")
        
        self.DISR_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.DISR_checkbox.setGeometry(QtCore.QRect(390, 180, 51, 17))
        self.DISR_checkbox.setObjectName("DISR_checkbox")
        
        self.CCM_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.CCM_checkbox.setGeometry(QtCore.QRect(495, 30, 46, 17))
        self.CCM_checkbox.setCheckable(True)
        self.CCM_checkbox.setChecked(False)
        self.CCM_checkbox.setTristate(False)
        self.CCM_checkbox.setObjectName("CCM_checkbox")
        
        self.SVMBackward_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SVMBackward_checkbox.setGeometry(QtCore.QRect(495, 90, 96, 17))
        self.SVMBackward_checkbox.setObjectName("SVMBackward_checkbox")
        
        self.SVMRFE_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SVMRFE_checkbox.setGeometry(QtCore.QRect(495, 60, 76, 17))
        self.SVMRFE_checkbox.setObjectName("SVMRFE_checkbox")
        
        self.SVMForward_checkbox = QtWidgets.QCheckBox(self.FSFrame)
        self.SVMForward_checkbox.setGeometry(QtCore.QRect(495, 120, 86, 17))
        self.SVMForward_checkbox.setObjectName("SVMForward_checkbox")
        
        self.Analysis = QtWidgets.QWidget(self.centralwidget)
        self.Analysis.setGeometry(QtCore.QRect(30, 405, 741, 106))
        self.Analysis.setObjectName("Analysis")
        
        self.frame = QtWidgets.QFrame(self.Analysis)
        self.frame.setGeometry(QtCore.QRect(0, 0, 741, 106))
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
        self.trainingTestingSplit_lineedit.setObjectName("trainingTestingSplit_lineedit")
        
        self.Output = QtWidgets.QWidget(self.centralwidget)
        self.Output.setGeometry(QtCore.QRect(30, 520, 741, 81))
        self.Output.setObjectName("Output")
        
        self.frame_2 = QtWidgets.QFrame(self.Output)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 741, 81))
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
        self.run_button.setGeometry(QtCore.QRect(580, 10, 75, 23))
        self.run_button.setObjectName("run_button")
        
        self.runAndSave_button = QtWidgets.QPushButton(self.frame_2)
        self.runAndSave_button.setGeometry(QtCore.QRect(580, 50, 81, 23))
        self.runAndSave_button.setObjectName("runAndSave_button")
        
        self.outputBrowse_button = QtWidgets.QPushButton(self.frame_2)
        self.outputBrowse_button.setGeometry(QtCore.QRect(60, 10, 75, 23))
        self.outputBrowse_button.setObjectName("outputBrowse_button")
        self.outputBrowse_button.setToolTip("Choose Output")
        self.outputBrowse_button.clicked.connect(self.on_click_save_output)
        
        self.browseOutput_lineedit = QtWidgets.QLineEdit(self.frame_2)
        self.browseOutput_lineedit.setGeometry(QtCore.QRect(25, 40, 113, 20))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browseFeature_button.setText(_translate("MainWindow", "Browse"))
        self.browseLabel_button.setText(_translate("MainWindow", "Browse"))
        self.featureFile_label.setText(_translate("MainWindow", "Feature File"))
        self.labelFile_label.setText(_translate("MainWindow", "Label File"))
        self.data_label.setText(_translate("MainWindow", "Data"))
        self.featureSelection_label.setText(_translate("MainWindow", " Feature Selection"))
        self.groupSAOLA_checkbox.setText(_translate("MainWindow", "Group-SAOLA"))
        self.sparseGroupLASSO_checkbox.setText(_translate("MainWindow", "Sparse Group LASSO"))
        self.groupLASSO_checkbox.setText(_translate("MainWindow", "Group LASSO"))
        self.fastOSFS_checkbox.setText(_translate("MainWindow", "Fast OSFS"))
        self.OSFS_checkbox.setText(_translate("MainWindow", "OSFS"))
        self.SAOLA_checkbox.setText(_translate("MainWindow", "SAOLA"))
        self.alphaInvesting_checkbox.setText(_translate("MainWindow", "alpha-investing"))
        self.minMaxMarkovBlanket_checkbox.setText(_translate("MainWindow", "Min-Max Markov Blanket"))
        self.checkBox_9.setText(_translate("MainWindow", "mmpc"))
        self.HITON_checkbox.setText(_translate("MainWindow", "HITON"))
        self.SES_checkbox.setText(_translate("MainWindow", "SES"))
        self.randomForest_checkbox.setText(_translate("MainWindow", "Random Forest"))
        self.gradientBoosting_checkbox.setText(_translate("MainWindow", "Gradient Boosting"))
        self.regularizedRandomForest_checkbox.setText(_translate("MainWindow", "Regularized Random Forest"))
        self.guidedRegularizedRandomForest_checkbox.setText(_translate("MainWindow", "Guided Regularized Random Forest"))
        self.RFgroove_checkbox.setText(_translate("MainWindow", "RFgroove"))
        self.infFS_checkbox.setText(_translate("MainWindow", "Inf-FS"))
        self.infiniteLatenFeatureSelection_checkbox.setText(_translate("MainWindow", "Infinite Latent Feature Selection"))
        self.eigenvectorCentrality_checkbox.setText(_translate("MainWindow", "Eigenvector Centrality"))
        self.quickReduct_checkbox.setText(_translate("MainWindow", "Quick Reduct"))
        self.FSDAARHueristicRST_checkbox.setText(_translate("MainWindow", "FS.DAAR.hueristic.RST"))
        self.FSnearOptfvprsFRST_checkbox.setText(_translate("MainWindow", "FS.nearOpt.fvprs.FRST"))
        self.tTest_checkbox.setText(_translate("MainWindow", "t-test"))
        self.chiSquare_checkbox.setText(_translate("MainWindow", "Chi square"))
        self.CFS_checkbox.setText(_translate("MainWindow", "CFS"))
        self.fisherScore_checkbox.setText(_translate("MainWindow", "Fisher Score"))
        self.HSICLasso_checkbox.setText(_translate("MainWindow", "HSICLasso"))
        self.LASSO_checkbox.setText(_translate("MainWindow", "LASSO"))
        self.L1SVM_checkbox.setText(_translate("MainWindow", "L1-SVM"))
        self.MRMR_checkbox.setText(_translate("MainWindow", "MRMR"))
        self.boruta_checkbox.setText(_translate("MainWindow", "Boruta"))
        self.CMIM_checkbox.setText(_translate("MainWindow", "CMIM"))
        self.elasticNets_checkbox.setText(_translate("MainWindow", "elastic nets"))
        self.JM_checkbox.setText(_translate("MainWindow", "JMI"))
        self.GA_checkbox.setText(_translate("MainWindow", "GA"))
        self.SPEC_checkbox.setText(_translate("MainWindow", "SPEC"))
        self.relief_checkbox.setText(_translate("MainWindow", "relief"))
        self.ridge_checkbox.setText(_translate("MainWindow", "Ridge"))
        self.DISR_checkbox.setText(_translate("MainWindow", "DISR"))
        self.CCM_checkbox.setText(_translate("MainWindow", "CCM"))
        self.SVMBackward_checkbox.setText(_translate("MainWindow", "SVM-Backward"))
        self.SVMRFE_checkbox.setText(_translate("MainWindow", "SVM-RFE"))
        self.SVMForward_checkbox.setText(_translate("MainWindow", "SVM-Forward"))
        self.analysis_label.setText(_translate("MainWindow", "Analysis"))
        self.crossvalidation_checkbox.setText(_translate("MainWindow", "Cross Validation"))
        self.folds_label.setText(_translate("MainWindow", "folds"))
        self.stratified_checkbox.setText(_translate("MainWindow", "Stratified"))
        self.numOfSelectFunc_label.setText(_translate("MainWindow", "# of select functions"))
        self.precent_radiobutton.setText(_translate("MainWindow", "%"))
        self.top_radiobutton.setText(_translate("MainWindow", "Top"))
        self.log_radiobutton.setText(_translate("MainWindow", "Log"))
        self.trainingTestingSplit_label.setText(_translate("MainWindow", "(Training/Testing) Split"))
        self.output_label.setText(_translate("MainWindow", "Output"))
        self.run_button.setText(_translate("MainWindow", "Run"))
        self.runAndSave_button.setText(_translate("MainWindow", "Run And Save"))
        self.outputBrowse_button.setText(_translate("MainWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

