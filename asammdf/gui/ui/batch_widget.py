# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'batch_widget.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_batch_widget(object):
    def setupUi(self, batch_widget):
        batch_widget.setObjectName("batch_widget")
        batch_widget.resize(707, 779)
        self.gridLayout_9 = QtWidgets.QGridLayout(batch_widget)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.splitter = QtWidgets.QSplitter(batch_widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.aspects = QtWidgets.QTabWidget(self.splitter)
        self.aspects.setTabPosition(QtWidgets.QTabWidget.West)
        self.aspects.setDocumentMode(False)
        self.aspects.setObjectName("aspects")
        self.concatenate_tab = QtWidgets.QWidget()
        self.concatenate_tab.setObjectName("concatenate_tab")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.concatenate_tab)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.concatenate_sync = QtWidgets.QCheckBox(self.concatenate_tab)
        self.concatenate_sync.setChecked(True)
        self.concatenate_sync.setObjectName("concatenate_sync")
        self.gridLayout_7.addWidget(self.concatenate_sync, 0, 0, 1, 2)
        self.concatenate_add_samples_origin = QtWidgets.QCheckBox(self.concatenate_tab)
        self.concatenate_add_samples_origin.setChecked(True)
        self.concatenate_add_samples_origin.setObjectName("concatenate_add_samples_origin")
        self.gridLayout_7.addWidget(self.concatenate_add_samples_origin, 1, 0, 1, 2)
        self.label_11 = QtWidgets.QLabel(self.concatenate_tab)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 2, 0, 1, 1)
        self.concatenate_format = QtWidgets.QComboBox(self.concatenate_tab)
        self.concatenate_format.setObjectName("concatenate_format")
        self.gridLayout_7.addWidget(self.concatenate_format, 2, 1, 1, 1)
        self.line_5 = QtWidgets.QFrame(self.concatenate_tab)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.gridLayout_7.addWidget(self.line_5, 3, 0, 1, 2)
        self.label_12 = QtWidgets.QLabel(self.concatenate_tab)
        self.label_12.setObjectName("label_12")
        self.gridLayout_7.addWidget(self.label_12, 4, 0, 1, 1)
        self.concatenate_compression = QtWidgets.QComboBox(self.concatenate_tab)
        self.concatenate_compression.setObjectName("concatenate_compression")
        self.gridLayout_7.addWidget(self.concatenate_compression, 4, 1, 1, 1)
        self.concatenate_split = QtWidgets.QCheckBox(self.concatenate_tab)
        self.concatenate_split.setChecked(True)
        self.concatenate_split.setObjectName("concatenate_split")
        self.gridLayout_7.addWidget(self.concatenate_split, 5, 0, 1, 1)
        self.line_6 = QtWidgets.QFrame(self.concatenate_tab)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.gridLayout_7.addWidget(self.line_6, 7, 0, 1, 2)
        self.concatenate_split_size = QtWidgets.QDoubleSpinBox(self.concatenate_tab)
        self.concatenate_split_size.setDecimals(3)
        self.concatenate_split_size.setMaximum(4.0)
        self.concatenate_split_size.setObjectName("concatenate_split_size")
        self.gridLayout_7.addWidget(self.concatenate_split_size, 6, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.concatenate_tab)
        self.label_10.setObjectName("label_10")
        self.gridLayout_7.addWidget(self.label_10, 6, 0, 1, 1)
        self.concatenate_btn = QtWidgets.QPushButton(self.concatenate_tab)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.concatenate_btn.setIcon(icon)
        self.concatenate_btn.setObjectName("concatenate_btn")
        self.gridLayout_7.addWidget(self.concatenate_btn, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 502, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem, 8, 1, 1, 1)
        self.aspects.addTab(self.concatenate_tab, icon, "")
        self.convert_tab = QtWidgets.QWidget()
        self.convert_tab.setObjectName("convert_tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.convert_tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtWidgets.QLabel(self.convert_tab)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.convert_format = QtWidgets.QComboBox(self.convert_tab)
        self.convert_format.setObjectName("convert_format")
        self.gridLayout_2.addWidget(self.convert_format, 0, 1, 1, 1)
        self.line = QtWidgets.QFrame(self.convert_tab)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 2)
        self.convert_compression = QtWidgets.QComboBox(self.convert_tab)
        self.convert_compression.setObjectName("convert_compression")
        self.gridLayout_2.addWidget(self.convert_compression, 2, 1, 1, 1)
        self.convert_split = QtWidgets.QCheckBox(self.convert_tab)
        self.convert_split.setChecked(True)
        self.convert_split.setObjectName("convert_split")
        self.gridLayout_2.addWidget(self.convert_split, 3, 0, 1, 1)
        self.convert_split_size = QtWidgets.QDoubleSpinBox(self.convert_tab)
        self.convert_split_size.setDecimals(3)
        self.convert_split_size.setMaximum(4.0)
        self.convert_split_size.setObjectName("convert_split_size")
        self.gridLayout_2.addWidget(self.convert_split_size, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.convert_tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.convert_tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.convert_tab)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 5, 0, 1, 2)
        self.convert_btn = QtWidgets.QPushButton(self.convert_tab)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/convert.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.convert_btn.setIcon(icon1)
        self.convert_btn.setObjectName("convert_btn")
        self.gridLayout_2.addWidget(self.convert_btn, 7, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 6, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout_2)
        self.aspects.addTab(self.convert_tab, icon1, "")
        self.cut_tab = QtWidgets.QWidget()
        self.cut_tab.setObjectName("cut_tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.cut_tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.cut_tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.cut_tab)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 0, 1, 1)
        self.cut_format = QtWidgets.QComboBox(self.cut_tab)
        self.cut_format.setObjectName("cut_format")
        self.gridLayout_3.addWidget(self.cut_format, 5, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.cut_tab)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 0, 0, 1, 1)
        self.cut_time_from_zero = QtWidgets.QCheckBox(self.cut_tab)
        self.cut_time_from_zero.setObjectName("cut_time_from_zero")
        self.gridLayout_3.addWidget(self.cut_time_from_zero, 2, 0, 1, 2)
        self.whence = QtWidgets.QCheckBox(self.cut_tab)
        self.whence.setObjectName("whence")
        self.gridLayout_3.addWidget(self.whence, 3, 0, 1, 2)
        self.cut_stop = QtWidgets.QDoubleSpinBox(self.cut_tab)
        self.cut_stop.setDecimals(6)
        self.cut_stop.setMinimum(-999999.0)
        self.cut_stop.setMaximum(999999.999999)
        self.cut_stop.setObjectName("cut_stop")
        self.gridLayout_3.addWidget(self.cut_stop, 1, 1, 1, 1)
        self.cut_split = QtWidgets.QCheckBox(self.cut_tab)
        self.cut_split.setChecked(True)
        self.cut_split.setObjectName("cut_split")
        self.gridLayout_3.addWidget(self.cut_split, 7, 0, 1, 1)
        self.cut_start = QtWidgets.QDoubleSpinBox(self.cut_tab)
        self.cut_start.setDecimals(6)
        self.cut_start.setMinimum(-999999.0)
        self.cut_start.setMaximum(999999.999999)
        self.cut_start.setObjectName("cut_start")
        self.gridLayout_3.addWidget(self.cut_start, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.cut_tab)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 1, 0, 1, 1)
        self.cut_split_size = QtWidgets.QDoubleSpinBox(self.cut_tab)
        self.cut_split_size.setMaximum(4.0)
        self.cut_split_size.setObjectName("cut_split_size")
        self.gridLayout_3.addWidget(self.cut_split_size, 8, 1, 1, 1)
        self.cut_compression = QtWidgets.QComboBox(self.cut_tab)
        self.cut_compression.setObjectName("cut_compression")
        self.gridLayout_3.addWidget(self.cut_compression, 6, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.cut_tab)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_3.addWidget(self.line_3, 4, 0, 1, 2)
        self.line_4 = QtWidgets.QFrame(self.cut_tab)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout_3.addWidget(self.line_4, 9, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.cut_tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 8, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 10, 1, 1, 1)
        self.cut_btn = QtWidgets.QPushButton(self.cut_tab)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/cut.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cut_btn.setIcon(icon2)
        self.cut_btn.setObjectName("cut_btn")
        self.gridLayout_3.addWidget(self.cut_btn, 11, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_3)
        self.aspects.addTab(self.cut_tab, icon2, "")
        self.export_tab = QtWidgets.QWidget()
        self.export_tab.setObjectName("export_tab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.export_tab)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.single_time_base = QtWidgets.QCheckBox(self.export_tab)
        self.single_time_base.setObjectName("single_time_base")
        self.gridLayout_6.addWidget(self.single_time_base, 2, 0, 1, 1)
        self.export_type = QtWidgets.QComboBox(self.export_tab)
        self.export_type.setObjectName("export_type")
        self.gridLayout_6.addWidget(self.export_type, 0, 1, 1, 1)
        self.use_display_names = QtWidgets.QCheckBox(self.export_tab)
        self.use_display_names.setObjectName("use_display_names")
        self.gridLayout_6.addWidget(self.use_display_names, 6, 0, 1, 1)
        self.mat_format = QtWidgets.QComboBox(self.export_tab)
        self.mat_format.setObjectName("mat_format")
        self.gridLayout_6.addWidget(self.mat_format, 11, 1, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.export_tab)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 11, 0, 1, 1)
        self.time_from_zero = QtWidgets.QCheckBox(self.export_tab)
        self.time_from_zero.setObjectName("time_from_zero")
        self.gridLayout_6.addWidget(self.time_from_zero, 3, 0, 1, 1)
        self.reduce_memory_usage = QtWidgets.QCheckBox(self.export_tab)
        self.reduce_memory_usage.setObjectName("reduce_memory_usage")
        self.gridLayout_6.addWidget(self.reduce_memory_usage, 7, 0, 1, 1)
        self.export_btn = QtWidgets.QPushButton(self.export_tab)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/export.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export_btn.setIcon(icon3)
        self.export_btn.setObjectName("export_btn")
        self.gridLayout_6.addWidget(self.export_btn, 15, 1, 1, 1)
        self.export_raster = QtWidgets.QDoubleSpinBox(self.export_tab)
        self.export_raster.setDecimals(6)
        self.export_raster.setObjectName("export_raster")
        self.gridLayout_6.addWidget(self.export_raster, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem3, 14, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.export_tab)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 9, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.export_tab)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 10, 0, 1, 1)
        self.export_compression = QtWidgets.QComboBox(self.export_tab)
        self.export_compression.setObjectName("export_compression")
        self.gridLayout_6.addWidget(self.export_compression, 9, 1, 1, 1)
        self.line_11 = QtWidgets.QFrame(self.export_tab)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.gridLayout_6.addWidget(self.line_11, 1, 0, 1, 2)
        self.oned_as = QtWidgets.QComboBox(self.export_tab)
        self.oned_as.setObjectName("oned_as")
        self.gridLayout_6.addWidget(self.oned_as, 12, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.export_tab)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 0, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.export_tab)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 4, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.export_tab)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_6.addWidget(self.line_9, 5, 0, 1, 2)
        self.line_10 = QtWidgets.QFrame(self.export_tab)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_6.addWidget(self.line_10, 13, 0, 1, 2)
        self.empty_channels = QtWidgets.QComboBox(self.export_tab)
        self.empty_channels.setObjectName("empty_channels")
        self.gridLayout_6.addWidget(self.empty_channels, 10, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.export_tab)
        self.label_16.setObjectName("label_16")
        self.gridLayout_6.addWidget(self.label_16, 12, 0, 1, 1)
        self.time_as_date = QtWidgets.QCheckBox(self.export_tab)
        self.time_as_date.setObjectName("time_as_date")
        self.gridLayout_6.addWidget(self.time_as_date, 8, 0, 1, 1)
        self.verticalLayout_7.addLayout(self.gridLayout_6)
        self.aspects.addTab(self.export_tab, icon3, "")
        self.resample_tab = QtWidgets.QWidget()
        self.resample_tab.setObjectName("resample_tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.resample_tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setContentsMargins(5, 5, 5, 5)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_8 = QtWidgets.QLabel(self.resample_tab)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 3, 0, 1, 1)
        self.resample_split_size = QtWidgets.QDoubleSpinBox(self.resample_tab)
        self.resample_split_size.setDecimals(3)
        self.resample_split_size.setMaximum(4.0)
        self.resample_split_size.setObjectName("resample_split_size")
        self.gridLayout_4.addWidget(self.resample_split_size, 5, 1, 1, 1)
        self.resample_split = QtWidgets.QCheckBox(self.resample_tab)
        self.resample_split.setChecked(True)
        self.resample_split.setObjectName("resample_split")
        self.gridLayout_4.addWidget(self.resample_split, 4, 0, 1, 1)
        self.resample_compression = QtWidgets.QComboBox(self.resample_tab)
        self.resample_compression.setObjectName("resample_compression")
        self.gridLayout_4.addWidget(self.resample_compression, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.resample_tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 1, 0, 1, 1)
        self.resample_format = QtWidgets.QComboBox(self.resample_tab)
        self.resample_format.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.resample_format.setObjectName("resample_format")
        self.gridLayout_4.addWidget(self.resample_format, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.resample_tab)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 5, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.resample_tab)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 1)
        self.resample_time_from_zero = QtWidgets.QCheckBox(self.resample_tab)
        self.resample_time_from_zero.setObjectName("resample_time_from_zero")
        self.gridLayout_4.addWidget(self.resample_time_from_zero, 2, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.resample_tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.raster_type_step = QtWidgets.QRadioButton(self.groupBox)
        self.raster_type_step.setChecked(True)
        self.raster_type_step.setObjectName("raster_type_step")
        self.verticalLayout_9.addWidget(self.raster_type_step)
        self.raster_type_channel = QtWidgets.QRadioButton(self.groupBox)
        self.raster_type_channel.setObjectName("raster_type_channel")
        self.verticalLayout_9.addWidget(self.raster_type_channel)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.raster = QtWidgets.QDoubleSpinBox(self.resample_tab)
        self.raster.setDecimals(6)
        self.raster.setObjectName("raster")
        self.verticalLayout_2.addWidget(self.raster)
        self.raster_channel = QtWidgets.QComboBox(self.resample_tab)
        self.raster_channel.setEnabled(False)
        self.raster_channel.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.raster_channel.setObjectName("raster_channel")
        self.verticalLayout_2.addWidget(self.raster_channel)
        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 1, 1, 1)
        self.resample_btn = QtWidgets.QPushButton(self.resample_tab)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resample.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.resample_btn.setIcon(icon4)
        self.resample_btn.setObjectName("resample_btn")
        self.gridLayout_4.addWidget(self.resample_btn, 7, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 6, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.aspects.addTab(self.resample_tab, icon4, "")
        self.scramble_tab = QtWidgets.QWidget()
        self.scramble_tab.setObjectName("scramble_tab")
        self.gridLayout = QtWidgets.QGridLayout(self.scramble_tab)
        self.gridLayout.setContentsMargins(25, 25, -1, -1)
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 572, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 1, 2, 1, 1)
        self.scramble_btn = QtWidgets.QPushButton(self.scramble_tab)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/scramble.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.scramble_btn.setIcon(icon5)
        self.scramble_btn.setObjectName("scramble_btn")
        self.gridLayout.addWidget(self.scramble_btn, 2, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.scramble_tab)
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 0, 1, 1, 2)
        self.aspects.addTab(self.scramble_tab, icon5, "")
        self.stack_tab = QtWidgets.QWidget()
        self.stack_tab.setObjectName("stack_tab")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.stack_tab)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stack_sync = QtWidgets.QCheckBox(self.stack_tab)
        self.stack_sync.setChecked(True)
        self.stack_sync.setObjectName("stack_sync")
        self.gridLayout_8.addWidget(self.stack_sync, 0, 0, 1, 2)
        self.stack_add_samples_origin = QtWidgets.QCheckBox(self.stack_tab)
        self.stack_add_samples_origin.setChecked(True)
        self.stack_add_samples_origin.setObjectName("stack_add_samples_origin")
        self.gridLayout_8.addWidget(self.stack_add_samples_origin, 1, 0, 1, 2)
        self.label_26 = QtWidgets.QLabel(self.stack_tab)
        self.label_26.setObjectName("label_26")
        self.gridLayout_8.addWidget(self.label_26, 2, 0, 1, 1)
        self.stack_format = QtWidgets.QComboBox(self.stack_tab)
        self.stack_format.setObjectName("stack_format")
        self.gridLayout_8.addWidget(self.stack_format, 2, 1, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.stack_tab)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_8.addWidget(self.line_8, 3, 0, 1, 2)
        self.label_25 = QtWidgets.QLabel(self.stack_tab)
        self.label_25.setObjectName("label_25")
        self.gridLayout_8.addWidget(self.label_25, 4, 0, 1, 1)
        self.stack_compression = QtWidgets.QComboBox(self.stack_tab)
        self.stack_compression.setObjectName("stack_compression")
        self.gridLayout_8.addWidget(self.stack_compression, 4, 1, 1, 1)
        self.stack_split = QtWidgets.QCheckBox(self.stack_tab)
        self.stack_split.setChecked(True)
        self.stack_split.setObjectName("stack_split")
        self.gridLayout_8.addWidget(self.stack_split, 5, 0, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.stack_tab)
        self.label_23.setObjectName("label_23")
        self.gridLayout_8.addWidget(self.label_23, 6, 0, 1, 1)
        self.stack_split_size = QtWidgets.QDoubleSpinBox(self.stack_tab)
        self.stack_split_size.setDecimals(3)
        self.stack_split_size.setMaximum(4.0)
        self.stack_split_size.setObjectName("stack_split_size")
        self.gridLayout_8.addWidget(self.stack_split_size, 6, 1, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.stack_tab)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_8.addWidget(self.line_7, 7, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 502, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem6, 8, 1, 1, 1)
        self.stack_btn = QtWidgets.QPushButton(self.stack_tab)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/stack.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stack_btn.setIcon(icon6)
        self.stack_btn.setObjectName("stack_btn")
        self.gridLayout_8.addWidget(self.stack_btn, 9, 1, 1, 1)
        self.aspects.addTab(self.stack_tab, icon6, "")
        self.extract_can_tab = QtWidgets.QWidget()
        self.extract_can_tab.setObjectName("extract_can_tab")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.extract_can_tab)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.load_can_database_btn = QtWidgets.QPushButton(self.extract_can_tab)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.load_can_database_btn.setIcon(icon7)
        self.load_can_database_btn.setObjectName("load_can_database_btn")
        self.gridLayout_11.addWidget(self.load_can_database_btn, 0, 0, 1, 1)
        self.can_database_list = MinimalListWidget(self.extract_can_tab)
        self.can_database_list.setObjectName("can_database_list")
        self.gridLayout_11.addWidget(self.can_database_list, 1, 0, 1, 3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.extract_can_tab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.extract_can_btn = QtWidgets.QPushButton(self.groupBox_2)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extract_can_btn.setIcon(icon8)
        self.extract_can_btn.setObjectName("extract_can_btn")
        self.gridLayout_5.addWidget(self.extract_can_btn, 5, 0, 1, 2)
        self.label__1 = QtWidgets.QLabel(self.groupBox_2)
        self.label__1.setObjectName("label__1")
        self.gridLayout_5.addWidget(self.label__1, 0, 0, 1, 1)
        self.extract_can_compression = QtWidgets.QComboBox(self.groupBox_2)
        self.extract_can_compression.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.extract_can_compression.setObjectName("extract_can_compression")
        self.gridLayout_5.addWidget(self.extract_can_compression, 0, 1, 1, 1)
        self.extract_can_format = QtWidgets.QComboBox(self.groupBox_2)
        self.extract_can_format.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.extract_can_format.setObjectName("extract_can_format")
        self.gridLayout_5.addWidget(self.extract_can_format, 1, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox_2)
        self.label_24.setObjectName("label_24")
        self.gridLayout_5.addWidget(self.label_24, 1, 0, 1, 1)
        self.ignore_invalid_signals_mdf = QtWidgets.QCheckBox(self.groupBox_2)
        self.ignore_invalid_signals_mdf.setObjectName("ignore_invalid_signals_mdf")
        self.gridLayout_5.addWidget(self.ignore_invalid_signals_mdf, 2, 0, 1, 2)
        self.label_27 = QtWidgets.QLabel(self.groupBox_2)
        self.label_27.setText("")
        self.label_27.setObjectName("label_27")
        self.gridLayout_5.addWidget(self.label_27, 3, 0, 1, 1)
        self.line_12 = QtWidgets.QFrame(self.groupBox_2)
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.gridLayout_5.addWidget(self.line_12, 4, 0, 1, 2)
        self.gridLayout_11.addWidget(self.groupBox_2, 2, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.extract_can_tab)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.time_from_zero_can = QtWidgets.QCheckBox(self.groupBox_3)
        self.time_from_zero_can.setObjectName("time_from_zero_can")
        self.gridLayout_10.addWidget(self.time_from_zero_can, 1, 1, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.groupBox_3)
        self.label_28.setObjectName("label_28")
        self.gridLayout_10.addWidget(self.label_28, 4, 1, 1, 1)
        self.line_13 = QtWidgets.QFrame(self.groupBox_3)
        self.line_13.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_13.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_13.setObjectName("line_13")
        self.gridLayout_10.addWidget(self.line_13, 7, 1, 1, 3)
        self.export_raster_can = QtWidgets.QDoubleSpinBox(self.groupBox_3)
        self.export_raster_can.setDecimals(6)
        self.export_raster_can.setObjectName("export_raster_can")
        self.gridLayout_10.addWidget(self.export_raster_can, 4, 2, 1, 2)
        self.extract_can_csv_btn = QtWidgets.QPushButton(self.groupBox_3)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/csv.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.extract_can_csv_btn.setIcon(icon9)
        self.extract_can_csv_btn.setObjectName("extract_can_csv_btn")
        self.gridLayout_10.addWidget(self.extract_can_csv_btn, 8, 1, 1, 3)
        self.single_time_base_can = QtWidgets.QCheckBox(self.groupBox_3)
        self.single_time_base_can.setObjectName("single_time_base_can")
        self.gridLayout_10.addWidget(self.single_time_base_can, 0, 1, 1, 1)
        self.ignore_invalid_signals_csv = QtWidgets.QCheckBox(self.groupBox_3)
        self.ignore_invalid_signals_csv.setObjectName("ignore_invalid_signals_csv")
        self.gridLayout_10.addWidget(self.ignore_invalid_signals_csv, 3, 1, 1, 1)
        self.empty_channels_can = QtWidgets.QComboBox(self.groupBox_3)
        self.empty_channels_can.setObjectName("empty_channels_can")
        self.gridLayout_10.addWidget(self.empty_channels_can, 5, 2, 1, 2)
        self.label_29 = QtWidgets.QLabel(self.groupBox_3)
        self.label_29.setObjectName("label_29")
        self.gridLayout_10.addWidget(self.label_29, 5, 1, 1, 1)
        self.can_time_as_date = QtWidgets.QCheckBox(self.groupBox_3)
        self.can_time_as_date.setObjectName("can_time_as_date")
        self.gridLayout_10.addWidget(self.can_time_as_date, 2, 1, 1, 1)
        self.gridLayout_11.addWidget(self.groupBox_3, 2, 1, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(240, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_11.addItem(spacerItem7, 2, 2, 1, 1)
        self.aspects.addTab(self.extract_can_tab, icon8, "")
        self.gridLayout_9.addWidget(self.splitter, 0, 0, 1, 1)

        self.retranslateUi(batch_widget)
        self.aspects.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(batch_widget)

    def retranslateUi(self, batch_widget):
        _translate = QtCore.QCoreApplication.translate
        batch_widget.setWindowTitle(_translate("batch_widget", "Form"))
        self.concatenate_sync.setText(_translate("batch_widget", "Sync using measurements timestamps"))
        self.concatenate_add_samples_origin.setText(_translate("batch_widget", "Add samples origin file"))
        self.label_11.setText(_translate("batch_widget", "Output format"))
        self.label_12.setText(_translate("batch_widget", "Compression"))
        self.concatenate_split.setText(_translate("batch_widget", "Split data blocks"))
        self.concatenate_split_size.setSuffix(_translate("batch_widget", "MB"))
        self.label_10.setText(_translate("batch_widget", "Split size "))
        self.concatenate_btn.setText(_translate("batch_widget", "Concatenate"))
        self.aspects.setTabText(self.aspects.indexOf(self.concatenate_tab), _translate("batch_widget", "Concatenate"))
        self.label_5.setText(_translate("batch_widget", "Split size "))
        self.convert_split.setText(_translate("batch_widget", "Split data blocks"))
        self.convert_split_size.setSuffix(_translate("batch_widget", "MB"))
        self.label_2.setText(_translate("batch_widget", "Output format"))
        self.label_3.setText(_translate("batch_widget", "Compression"))
        self.convert_btn.setText(_translate("batch_widget", "Convert"))
        self.aspects.setTabText(self.aspects.indexOf(self.convert_tab), _translate("batch_widget", "Convert"))
        self.aspects.setTabToolTip(self.aspects.indexOf(self.convert_tab), _translate("batch_widget", "conv"))
        self.label_6.setText(_translate("batch_widget", "Compression"))
        self.label_15.setText(_translate("batch_widget", "Output format"))
        self.label_13.setText(_translate("batch_widget", "Start"))
        self.cut_time_from_zero.setText(_translate("batch_widget", "Time from 0s"))
        self.whence.setText(_translate("batch_widget", "Start relative to first time stamp"))
        self.cut_stop.setSuffix(_translate("batch_widget", "s"))
        self.cut_split.setText(_translate("batch_widget", "Split data blocks"))
        self.cut_start.setSuffix(_translate("batch_widget", "s"))
        self.label_14.setText(_translate("batch_widget", "End"))
        self.label_7.setText(_translate("batch_widget", "Split size [MB]"))
        self.cut_btn.setText(_translate("batch_widget", "Cut"))
        self.aspects.setTabText(self.aspects.indexOf(self.cut_tab), _translate("batch_widget", "Cut"))
        self.single_time_base.setText(_translate("batch_widget", "Single time base"))
        self.use_display_names.setText(_translate("batch_widget", "Use display names"))
        self.label_18.setText(_translate("batch_widget", ".mat format"))
        self.time_from_zero.setText(_translate("batch_widget", "Time from 0s"))
        self.reduce_memory_usage.setText(_translate("batch_widget", "Reduce  memory usage"))
        self.export_btn.setText(_translate("batch_widget", "Export"))
        self.export_raster.setSuffix(_translate("batch_widget", "s"))
        self.label_20.setText(_translate("batch_widget", "Compression"))
        self.label_19.setText(_translate("batch_widget", "Empty channels"))
        self.label_21.setText(_translate("batch_widget", "Type"))
        self.label_22.setText(_translate("batch_widget", "Raster"))
        self.label_16.setText(_translate("batch_widget", ".mat oned_as"))
        self.time_as_date.setText(_translate("batch_widget", "Time as date"))
        self.aspects.setTabText(self.aspects.indexOf(self.export_tab), _translate("batch_widget", "Export"))
        self.label_8.setText(_translate("batch_widget", "Compression"))
        self.resample_split_size.setSuffix(_translate("batch_widget", "MB"))
        self.resample_split.setText(_translate("batch_widget", "Split data blocks"))
        self.label_4.setText(_translate("batch_widget", "Output format"))
        self.label_9.setText(_translate("batch_widget", "Split size"))
        self.label.setText(_translate("batch_widget", "Raster"))
        self.resample_time_from_zero.setText(_translate("batch_widget", "Time from 0s"))
        self.groupBox.setTitle(_translate("batch_widget", "Raster type"))
        self.raster_type_step.setText(_translate("batch_widget", "step"))
        self.raster_type_channel.setText(_translate("batch_widget", "channel"))
        self.raster.setSuffix(_translate("batch_widget", "s"))
        self.resample_btn.setText(_translate("batch_widget", "Resample"))
        self.aspects.setTabText(self.aspects.indexOf(self.resample_tab), _translate("batch_widget", "Resample"))
        self.scramble_btn.setText(_translate("batch_widget", "Scramble texts"))
        self.label_17.setText(_translate("batch_widget", "Anonymize the measurements: scramble all texts and replace them with random strings"))
        self.aspects.setTabText(self.aspects.indexOf(self.scramble_tab), _translate("batch_widget", "Scramble"))
        self.stack_sync.setText(_translate("batch_widget", "Sync using measurements timestamps"))
        self.stack_add_samples_origin.setText(_translate("batch_widget", "Add samples origin file"))
        self.label_26.setText(_translate("batch_widget", "Output format"))
        self.label_25.setText(_translate("batch_widget", "Compression"))
        self.stack_split.setText(_translate("batch_widget", "Split data blocks"))
        self.label_23.setText(_translate("batch_widget", "Split size "))
        self.stack_split_size.setSuffix(_translate("batch_widget", "MB"))
        self.stack_btn.setText(_translate("batch_widget", "Stack"))
        self.aspects.setTabText(self.aspects.indexOf(self.stack_tab), _translate("batch_widget", "Stack"))
        self.load_can_database_btn.setText(_translate("batch_widget", "Load CAN database"))
        self.groupBox_2.setTitle(_translate("batch_widget", "MDF"))
        self.extract_can_btn.setText(_translate("batch_widget", "Extract CAN signals"))
        self.label__1.setText(_translate("batch_widget", "Compression"))
        self.label_24.setText(_translate("batch_widget", "Version"))
        self.ignore_invalid_signals_mdf.setToolTip(_translate("batch_widget", "checks if all samples are eauql to the maximum teoretical signal value"))
        self.ignore_invalid_signals_mdf.setText(_translate("batch_widget", "Ignore invalid signals"))
        self.groupBox_3.setTitle(_translate("batch_widget", "CSV"))
        self.time_from_zero_can.setText(_translate("batch_widget", "Time from 0s"))
        self.label_28.setText(_translate("batch_widget", "Raster"))
        self.export_raster_can.setSuffix(_translate("batch_widget", "s"))
        self.extract_can_csv_btn.setText(_translate("batch_widget", "Export to CSV         "))
        self.single_time_base_can.setText(_translate("batch_widget", "Single time base"))
        self.ignore_invalid_signals_csv.setToolTip(_translate("batch_widget", "checks if all samples are eauql to the maximum teoretical signal value"))
        self.ignore_invalid_signals_csv.setText(_translate("batch_widget", "Ignore invalid signals"))
        self.label_29.setText(_translate("batch_widget", "Empty channels"))
        self.can_time_as_date.setText(_translate("batch_widget", "Time as date"))
        self.aspects.setTabText(self.aspects.indexOf(self.extract_can_tab), _translate("batch_widget", "CAN logging"))


from asammdf.gui.widgets.list import MinimalListWidget
from . import resource_rc
