import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QPushButton,
    QVBoxLayout, QWidget, QLabel, QListWidget
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QGuiApplication
from cyrtranslit import to_latin, to_cyrillic


class CirLatConverter(QMainWindow):

    def __init__(self):
        super().__init__()
        self.history = []
        self.initUI()

    # UI

    def initUI(self):
        self.setWindowTitle("CirLat konverter version 2.0")
        self.setGeometry(300, 300, 900, 700)

        if os.path.exists("ico.ico"):
            self.setWindowIcon(QIcon("ico.ico"))

        self.center()
        self.setMinimumSize(500, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # TITL
        title = QLabel("CirLat konverter")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 26px; font-weight: bold;")
        main_layout.addWidget(title)

        # POLJE ZA TEKST
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Unesite tekst ovde...")
        self.text_input.setMinimumHeight(200)
        self.text_input.setStyleSheet("""
            QTextEdit {
                font-size: 15px;
                border: 2px solid #3498db;
                border-radius: 6px;
                padding: 8px;
            }
        """)
        main_layout.addWidget(self.text_input, 4)

        # DUGMAD ZA APP
        self.cir_to_lat_btn = QPushButton("Cir → Lat")
        self.cir_to_lat_btn.clicked.connect(self.cir_to_lat)

        self.lat_to_cir_btn = QPushButton("Lat → Cir")
        self.lat_to_cir_btn.clicked.connect(self.lat_to_cir)

        self.copy_btn = QPushButton("Kopiraj")
        self.copy_btn.clicked.connect(self.copy_text)

        self.clear_btn = QPushButton("Obriši tekst")
        self.clear_btn.clicked.connect(self.clear_text)

        self.clear_history_btn = QPushButton("Obriši istoriju")
        self.clear_history_btn.clicked.connect(self.clear_history)

        self.exit_btn = QPushButton("Izlaz")
        self.exit_btn.clicked.connect(self.close)

        buttons = [
            self.cir_to_lat_btn,
            self.lat_to_cir_btn,
            self.copy_btn,
            self.clear_btn,
            self.clear_history_btn,
            self.exit_btn
        ]

        for btn in buttons:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #3498db;
                    color: white;
                    border: none;
                    padding: 10px;
                    font-weight: bold;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #2980b9;
                }
                QPushButton:pressed {
                    background-color: #1f6391;
                }
            """)
            main_layout.addWidget(btn)

        # ISTORIJA
        history_label = QLabel("Istorija konverzija:")
        history_label.setAlignment(Qt.AlignLeft)
        main_layout.addWidget(history_label)

        self.history_list = QListWidget()
        self.history_list.itemClicked.connect(self.load_from_history)
        main_layout.addWidget(self.history_list, 1)

        # FOOTER
        footer = QLabel("Software created by Šamec Uglješa © 2026")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("font-size: 11px; color: gray; margin-top: 10px;")
        main_layout.addWidget(footer)

        central_widget.setLayout(main_layout)

    # PREBACIVANJE TEKSTA

    def cir_to_lat(self):
        text = self.text_input.toPlainText()
        if text.strip():
            converted = to_latin(text, "sr")
            self.add_to_history("Cir → Lat", text, converted)
            self.text_input.setPlainText(converted)
            self.statusBar().showMessage("Konverzija završena", 2000)

    def lat_to_cir(self):
        text = self.text_input.toPlainText()
        if text.strip():
            converted = to_cyrillic(text, "sr")
            self.add_to_history("Lat → Cir", text, converted)
            self.text_input.setPlainText(converted)
            self.statusBar().showMessage("Konverzija završena", 2000)

    # ISTORIJA

    def add_to_history(self, direction, original, converted):
        self.history.append((direction, original, converted))
        preview = original[:30].replace("\n", " ")
        self.history_list.addItem(f"{len(self.history)}. {direction} | {preview}...")

    def load_from_history(self, item):
        index = self.history_list.row(item)
        direction, original, converted = self.history[index]
        self.text_input.setPlainText(converted)
        self.statusBar().showMessage("Učitano iz istorije", 2000)

    def clear_history(self):
        self.history.clear()
        self.history_list.clear()
        self.statusBar().showMessage("Istorija obrisana", 2000)

    # DODATNA FUNKCIONALNOST

    def copy_text(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.text_input.toPlainText())
        self.statusBar().showMessage("Tekst kopiran u clipboard", 2000)

    def clear_text(self):
        self.text_input.clear()
        self.statusBar().showMessage("Tekst obrisan", 2000)

    def center(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        center_point = screen_geometry.center()
        frame_geometry = self.frameGeometry()
        frame_geometry.moveCenter(center_point)
        self.move(frame_geometry.topLeft())


# MAIN

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    window = CirLatConverter()
    window.show()


    sys.exit(app.exec_())
