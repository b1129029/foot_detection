from PyQt5 import QtCore, QtGui, QtWidgets
import os

class page3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 450)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # 左邊佈局開始
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # 工具按鈕佈局
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)  # 將上邊距設為0，將按鈕上移
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton = QtWidgets.QToolButton(Form)
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
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""\
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
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")

        # 加載圖片
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'source', 'img')
        image = os.path.join(img_dir, 'result.jpg')
        pixmap = QtGui.QPixmap(image)
        if pixmap.isNull():
            print("圖片加載失敗，請檢查路徑是否正確")
        
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
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("""\
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
        self.line = QtWidgets.QFrame(Form)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_3.addWidget(self.line)

        # 右側佈局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(Form)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        # 初始化 QStandardItemModel
        self.model = QtGui.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["等級", "病患_ID", "名字", "性別", "身高", "病患_LineID"])  # 設置表頭
        
        # 設置模型到 tableView
        self.tableView.setModel(self.model)
        

        # 設置只能選擇整行
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        # 添加測試數據
        self.add_table_data()
        

        # 添加右侧水平布局
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")

        # label_2
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.label_2.setFixedSize(150, 50)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)  # 置中對齊
        self.horizontalLayout_6.addWidget(self.label_2)

        # 测量按钮
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("""\
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_table_data(self):
        # 新增資料到表格
        data = [
            ["A", "001", " 高翊恩", "男", "172", "n112233"],
            ["B", "002", "李子捷", "男", "168", "j112233"],
            ["C", "003", "朱少謙", "男", "150", "c112233"]
        ]
        
        for row in data:
            items = []
            for item in row:
                table_item = QtGui.QStandardItem(item)
                table_item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)  # 設置為不可編輯
                items.append(table_item)
            self.model.appendRow(items)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.toolButton.setText(_translate("Form", ""))
        self.pushButton_2.setText(_translate("Form", "◀"))
        self.label.setText(_translate("Form", ""))
        self.pushButton_3.setText(_translate("Form", "▶"))
        self.pushButton_4.setText(_translate("Form", "測量"))
        doctor_name = ("扶老二")
        self.label_2.setText(_translate("Form", "主治醫師: " + doctor_name))
