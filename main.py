import sys, os
from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWebEngineWidgets import QWebEngineView


def res(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)


class Win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("السبّاح الماهر 🏊")
        self.resize(520, 800)
        self.view = QWebEngineView()
        self.setCentralWidget(self.view)
        self.view.load(QUrl.fromLocalFile(res("swim-game.html")))

    def keyPressEvent(self, e):
        # F11 = ملء الشاشة، Esc = خروج من ملء الشاشة
        if e.key() == Qt.Key.Key_F11:
            self.showNormal() if self.isFullScreen() else self.showFullScreen()
        elif e.key() == Qt.Key.Key_Escape and self.isFullScreen():
            self.showNormal()
        else:
            super().keyPressEvent(e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setOrganizationName("NOAI")
    app.setApplicationName("SwimGame")  # يحفظ أفضل نتيجة بين مرات التشغيل
    w = Win()
    w.show()
    sys.exit(app.exec())
