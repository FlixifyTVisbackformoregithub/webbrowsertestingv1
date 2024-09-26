import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super(SimpleBrowser, self).__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl("http://www.google.com")

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)

        self.go_button = QPushButton('Go')
        self.go_button.clicked.connect(self.navigate_to_url)

        layout = QVBoxLayout()
        layout.addWidget(self.url_bar)
        layout.addWidget(self.go_button)
        layout.addWidget(self.browser)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
        self.setWindowTitle("Simple Web Browser")
        self.show()

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith('http'):
            url = 'http://' + url
        self.browser.setUrl(url)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SimpleBrowser()
    sys.exit(app.exec_())
