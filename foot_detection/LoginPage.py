import os
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox , QSpacerItem, QSizePolicy, QApplication, QHBoxLayout, QMainWindow, QWidget, QStackedWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFrame

class LoginPage(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setup_ui()
        
    def setup_ui(self):
        # 設定背景圖片
        base_dir = os.path.dirname(os.path.abspath(__file__))
        img_dir = os.path.join(base_dir, 'source', 'img')
        background_image = os.path.join(img_dir, 'background.gif')

        # 背景圖片顯示
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 1600, 900)  # 設置為全窗口尺寸
        self.movie = QtGui.QMovie(background_image)
        self.background_label.setMovie(self.movie)
        self.background_label.setScaledContents(True)
        self.movie.start()

        # 創建主佈局
        main_layout = QVBoxLayout()

        # 設置灰色背景框
        self.gray_background = QFrame(self)
        self.gray_background.setStyleSheet("background-color: white; border-radius: 10px;")
        self.gray_background.setFixedSize(390, 260)  # 設置固定大小

        # 創建灰色背景框內部佈局
        gray_layout = QVBoxLayout()
        gray_layout.setContentsMargins(20, 20, 20, 20)  # 設置邊距
        gray_layout.addWidget(self.gray_background)
        gray_layout.setAlignment(QtCore.Qt.AlignCenter)  # 垂直方向居中

        # 創建灰色框架內部佈局
        form_layout = QVBoxLayout()
        form_layout.setContentsMargins(10, 10, 10, 10)  # 設置邊距

        self.username_label = QLabel("用戶名:")
        self.username_label.setStyleSheet("font-size: 20px;")
        self.username_input = QLineEdit(self)
        self.username_input.setStyleSheet("""
            QLineEdit {
                border: 3px solid gray;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        form_layout.addWidget(self.username_label)
        form_layout.addWidget(self.username_input)

        self.password_label = QLabel("密碼:")
        self.password_label.setStyleSheet("font-size: 20px;")
        self.password_input = QLineEdit(self)
        self.password_input.setStyleSheet("""
            QLineEdit {
                border: 3px solid gray;
                border-radius: 10px;
                padding: 5px;
            }
        """)
        form_layout.addWidget(self.password_label)
        form_layout.addWidget(self.password_input)

        form_layout.addSpacing(30)

        button_layout = QVBoxLayout()
        button_layout.setContentsMargins(130, 0, 130, 0)
        # 創建登入按鈕
        login_button = QPushButton("登入", self)
        login_button.setStyleSheet("""
            QPushButton {
                background-color: gray;
                border: none;
                border-radius: 10px;
                color: white;
                padding: 8px;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: darkgray;
            }
        """)
        login_button.clicked.connect(self.handle_login)
        button_layout.addWidget(login_button)

        # 將按鈕添加到表單佈局中
        form_layout.addLayout(button_layout)

        # 將表單佈局添加到灰色背景框
        self.gray_background.setLayout(form_layout)

        # 將灰色背景框佈局添加到主佈局
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))  # 添加上部間隔
        main_layout.addLayout(gray_layout)  # 添加灰色背景框佈局
        main_layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))  # 添加下部間隔

        # 設置主佈局
        self.setLayout(main_layout)

    def handle_login(self):
        # 簡單模擬登錄驗證
        if self.username_input.text() == "123" and self.password_input.text() == "123":
            self.parent.stacked_widget.setCurrentWidget(self.parent.search_page)
        else:
            # 帳密錯誤彈出提示框
            msg_box = QMessageBox(self)
            msg_box.setWindowTitle("帳號或密碼錯誤")
            msg_box.setIcon(QMessageBox.Warning)  # 使用警告圖標
            msg_box.setText("帳號或密碼錯誤，請重新輸入。")
            msg_box.setStandardButtons(QMessageBox.Ok)
            msg_box.button(QMessageBox.Ok).setText("確定")
            msg_box.exec_()