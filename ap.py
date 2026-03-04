import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QPushButton, 
                             QVBoxLayout, QHBoxLayout, QWidget, QDesktopWidget, 
                             QSpacerItem, QSizePolicy, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from cyrtranslit import to_latin, to_cyrillic

class CirLatConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Podešavanja prozora
        self.setWindowTitle("CirLat konverter")
        self.setGeometry(300, 300, 800, 600)
        
        # POSTAVI IKONU - ico.ico iz istog direktorijuma
        self.setWindowIcon(QIcon("ico.ico"))
        
        self.center()
        
        # Centralni vidžet
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # IZGLED
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # NASLOV
        title = QLabel("CirLat konverter")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 28px; font-weight: bold; color: #2c3e50; margin: 10px;")
        main_layout.addWidget(title)
        
        # POLJE ZA UBACIVANJE TEKSTA
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Unesite tekst ovde...")
        self.text_input.setMinimumHeight(200)
        self.text_input.setStyleSheet("""
            QTextEdit {
                font-size: 16px;
                border: 2px solid #3498db;
                border-radius: 8px;
                padding: 10px;
            }
            QTextEdit:focus {
                border-color: #2980b9;
            }
        """)
        main_layout.addWidget(self.text_input)
        
        # DUGMAD ZA APLIKACIJU
        self.cir_to_lat_btn = QPushButton("Cir → Lat")
        self.cir_to_lat_btn.clicked.connect(self.cir_to_lat)
        self.style_button(self.cir_to_lat_btn, "#27ae60")
        main_layout.addWidget(self.cir_to_lat_btn)
        
        self.lat_to_cir_btn = QPushButton("Lat → Cir")
        self.lat_to_cir_btn.clicked.connect(self.lat_to_cir)
        self.style_button(self.lat_to_cir_btn, "#e74c3c")
        main_layout.addWidget(self.lat_to_cir_btn)
        
        self.clear_btn = QPushButton("Obriši polje")
        self.clear_btn.clicked.connect(self.clear_text)
        self.style_button(self.clear_btn, "#f39c12")
        main_layout.addWidget(self.clear_btn)
        
        self.exit_btn = QPushButton("Izlaz")
        self.exit_btn.clicked.connect(self.close)
        self.style_button(self.exit_btn, "#95a5a6")
        main_layout.addWidget(self.exit_btn)
        
        # FOOTER
        footer = QLabel("Software created by Šamec Uglješa © 2025")
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("font-size: 12px; color: #7f8c8d; margin-top: 20px;")
        main_layout.addWidget(footer)
        
        # Dodato rastezanje da bi se pomerilo podnožje na dno
        main_layout.addStretch()
        
        central_widget.setLayout(main_layout)
        
        # ZA RESPONZIVNOST
        self.setMinimumSize(400, 500)
    
    def style_button(self, button, color):
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                padding: 12px 24px;
                font-size: 14px;
                font-weight: bold;
                border-radius: 6px;
                min-width: 120px;
            }}
            QPushButton:hover {{
                background-color: {self.darken_color(color)};
            }}
            QPushButton:pressed {{
                background-color: {self.lighten_color(color)};
            }}
        """)
    
    def darken_color(self, color):
        hex_color = color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        darkened = tuple(max(0, c - 30) for c in rgb)
        return f"#{darkened[0]:02x}{darkened[1]:02x}{darkened[2]:02x}"
    
    def lighten_color(self, color):
        hex_color = color.lstrip('#')
        rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
        lightened = tuple(min(255, c + 20) for c in rgb)
        return f"#{lightened[0]:02x}{lightened[1]:02x}{lightened[2]:02x}"
    
    def cir_to_lat(self):
        text = self.text_input.toPlainText()
        if text.strip():
            converted = to_latin(text, "sr")
            self.text_input.setPlainText(converted)
    
    def lat_to_cir(self):
        text = self.text_input.toPlainText()
        if text.strip():
            converted = to_cyrillic(text, "sr")
            self.text_input.setPlainText(converted)
    
    def clear_text(self):
        self.text_input.clear()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def resizeEvent(self, event):
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Modern look
    
    window = CirLatConverter()
    window.show()
    
    sys.exit(app.exec_())

