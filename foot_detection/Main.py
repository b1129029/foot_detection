import os
from LoginPage import LoginPage
from SearchPage import SearchPage
from DetailPage import DetailPage
from SQL import view_edema_info
from PyQt5.QtWidgets import  QApplication, QMainWindow, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.patient_id = None
        self.setWindowTitle("腳部水腫觀測系統")
        self.resize(1600, 900)

        # 創建堆疊佈局
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # 初始化不同頁面
        self.login_page = LoginPage(self)
        self.search_page = SearchPage(self)
        self.detail_page = DetailPage(self)

        # 添加頁面到堆疊佈局
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.search_page)
        self.stacked_widget.addWidget(self.detail_page)

        # 設置初始頁面為登錄頁面
        self.stacked_widget.setCurrentWidget(self.login_page)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
 