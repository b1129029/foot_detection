import os
from SQL import view_edema_info
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

class DetailPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName("Form")
        self.resize(800, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 左邊佈局開始
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 工具按鈕佈局
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)  # 將上邊距設為0，將按鈕上移
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(self)
        self.toolButton.setObjectName("toolButton")
        back_pixmap  = QtGui.QPixmap("source/img/back.png")
        icon = QtGui.QIcon()
        icon.addPixmap(back_pixmap)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(40, 40))
        self.horizontalLayout_2.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        # 增加按鈕下方的空白區域
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        # 左邊下方的圖片和按鈕佈局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, 10)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # 左側按鈕
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border-radius: 5px;
                border: 2px solid darkgray;
                padding: 5px;
                min-width: 10px;
                min-height: 10px;
            }
            QPushButton:hover {
                background-color: gray;
            }
        """)
        self.verticalLayout_3.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        # 圖片標籤
        self.label = QtWidgets.QLabel(self)
        self.label.setObjectName("label")

        # 加載圖片
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'source', 'img')
        image = os.path.join(img_dir, 'result.jpg')
        pixmap = QtGui.QPixmap(image)
        
        # 調整 QLabel 的大小以適應圖片
        self.label.setPixmap(pixmap)
        self.label.resize(pixmap.size())

        # 設置 QLabel 的最大尺寸
        self.label.setMaximumSize(700, 700) 

        # 設置 QLabel 內容縮放以適應大小
        self.label.setScaledContents(True)
        
        # 添加到佈局中
        self.horizontalLayout.addWidget(self.label)

        # 右側按鈕佈局
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem4)
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border-radius: 5px;
                border: 2px solid darkgray;
                padding: 5px;
                min-width: 10px;
                min-height: 10px;
            }
            QPushButton:hover {
                background-color: gray;
            }
        """)
        self.verticalLayout_4.addWidget(self.pushButton_3)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem5)
        self.horizontalLayout.addLayout(self.verticalLayout_4)

        # 將圖片和按鈕佈局加入主佈局中
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)

        # 分隔線
        self.line = QtWidgets.QFrame(self)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)

        # 右側佈局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(self)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        # 初始化 QStandardItemModel
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["測量編號", "病患_ID", "測量時間", "腳圍"])  # 設置表頭
        
        # 設置模型到 tableView
        self.tableView.setModel(self.model)
        

        # 設置只能選擇整行
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # 添加右侧水平布局
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # label_2
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(150, 50)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 置中對齊
        self.horizontalLayout_6.addWidget(self.label_2)

        # 测量按钮
        self.pushButton_4 = QtWidgets.QPushButton(self)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""
            QPushButton {
                background-color: lightgray;
                border-radius: 5px;
                border: 2px solid darkgray;
                padding: 10px;
                min-width: 50px;
                min-height: 20px;
            }
            QPushButton:hover {
                background-color: gray;
            }
        """)
        self.horizontalLayout_6.addWidget(self.pushButton_4)

        # 将水平布局添加到右侧垂直布局中
        self.verticalLayout.addLayout(self.horizontalLayout_6)

        # 在左側的底部添加 spacerItem
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem6)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
        self.toolButton.clicked.connect(self.go_back)

    def go_back(self):
        # 切換到查詢頁面
        self.parent.stacked_widget.setCurrentWidget(self.parent.search_page)

    def add_table_data_2(self):
        print('add table')
        search_page = self.parent.search_page    
        patient_id = str(search_page.get_patient_id())
        print(patient_id)
        data = view_edema_info(patient_id)
        # 初始化 QStandardItemModel
        self.model.clear()
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["測量編號", "病患_ID", "測量時間", "腳圍"])  # 設置表頭
        
        # 設置模型到 tableView
        self.tableView.setModel(self.model)
        for row in data:
            items = []
            for item in row:
                table_item = QtGui.QStandardItem(str(item))
                table_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)  # 設置為不可編輯
                items.append(table_item)
            self.model.appendRow(items)
        self.model.layoutChanged.emit()
        
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "◀"))
        self.label.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", "▶"))
        self.pushButton_4.setText(_translate("Form", "測量"))
        doctor_name = ("扶老二")
        self.label_2.setText(_translate("Form", "主治醫師: " + doctor_name))
