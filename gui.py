import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                           QHBoxLayout, QPushButton, QLabel, QLineEdit, 
                           QComboBox, QTableWidget, QTableWidgetItem, QTabWidget)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont, QIcon
import pyqtgraph as pg
from datetime import datetime
from trader import CryptoTrader
from market_data import MarketData
from config import TRADING_SYMBOL

class CryptoTradingBotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("روبوت التداول الآلي للعملات المشفرة")
        self.setGeometry(100, 100, 1200, 800)
        
        # تهيئة المكونات
        self.market_data = MarketData()
        self.trader = CryptoTrader()
        self.price_history = []
        self.time_history = []
        
        # إنشاء الواجهة
        self.init_ui()
        
        # تحديث البيانات كل 5 ثواني
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)
        self.timer.start(5000)

    def init_ui(self):
        # إنشاء القائمة الرئيسية
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        # إنشاء علامات التبويب
        tabs = QTabWidget()
        
        # علامة التبويب الرئيسية
        main_tab = QWidget()
        main_layout = QVBoxLayout()
        
        # الجزء العلوي - معلومات السوق
        market_info = QHBoxLayout()
        
        # السعر الحالي
        self.price_label = QLabel("السعر الحالي: ")
        self.price_label.setFont(QFont('Arial', 12))
        market_info.addWidget(self.price_label)
        
        # حجم التداول
        self.volume_label = QLabel("حجم التداول: ")
        self.volume_label.setFont(QFont('Arial', 12))
        market_info.addWidget(self.volume_label)
        
        main_layout.addLayout(market_info)
        
        # الرسم البياني
        self.graph_widget = pg.PlotWidget()
        self.graph_widget.setBackground('w')
        self.graph_widget.setTitle("سعر العملة", color="k", size="20pt")
        self.graph_widget.showGrid(x=True, y=True)
        main_layout.addWidget(self.graph_widget)
        
        # أزرار التحكم
        controls = QHBoxLayout()
        
        # زر بدء/إيقاف التداول
        self.start_button = QPushButton("بدء التداول")
        self.start_button.clicked.connect(self.toggle_trading)
        controls.addWidget(self.start_button)
        
        # اختيار زوج العملات
        self.pair_combo = QComboBox()
        self.pair_combo.addItems(["BTC/USDT", "ETH/USDT", "BNB/USDT"])
        controls.addWidget(self.pair_combo)
        
        main_layout.addLayout(controls)
        
        # جدول الصفقات
        self.trades_table = QTableWidget()
        self.trades_table.setColumnCount(5)
        self.trades_table.setHorizontalHeaderLabels(["الوقت", "النوع", "السعر", "الكمية", "الحالة"])
        main_layout.addWidget(self.trades_table)
        
        main_tab.setLayout(main_layout)
        tabs.addTab(main_tab, "الرئيسية")
        
        # علامة تبويب الإعدادات
        settings_tab = QWidget()
        settings_layout = QVBoxLayout()
        
        # إعدادات API
        api_layout = QVBoxLayout()
        api_key_label = QLabel("مفتاح API:")
        self.api_key_input = QLineEdit()
        api_secret_label = QLabel("كلمة السر API:")
        self.api_secret_input = QLineEdit()
        self.api_secret_input.setEchoMode(QLineEdit.EchoMode.Password)
        
        api_layout.addWidget(api_key_label)
        api_layout.addWidget(self.api_key_input)
        api_layout.addWidget(api_secret_label)
        api_layout.addWidget(self.api_secret_input)
        
        settings_layout.addLayout(api_layout)
        
        # إعدادات التداول
        trading_settings = QVBoxLayout()
        
        stop_loss_label = QLabel("نسبة وقف الخسارة (%):")
        self.stop_loss_input = QLineEdit("2.0")
        
        take_profit_label = QLabel("نسبة جني الأرباح (%):")
        self.take_profit_input = QLineEdit("3.0")
        
        trading_settings.addWidget(stop_loss_label)
        trading_settings.addWidget(self.stop_loss_input)
        trading_settings.addWidget(take_profit_label)
        trading_settings.addWidget(self.take_profit_input)
        
        settings_layout.addLayout(trading_settings)
        
        # زر حفظ الإعدادات
        save_button = QPushButton("حفظ الإعدادات")
        save_button.clicked.connect(self.save_settings)
        settings_layout.addWidget(save_button)
        
        settings_tab.setLayout(settings_layout)
        tabs.addTab(settings_tab, "الإعدادات")
        
        layout.addWidget(tabs)

    def update_data(self):
        try:
            # تحديث السعر الحالي
            current_price = self.market_data.get_current_price()
            if current_price:
                self.price_label.setText(f"السعر الحالي: {current_price:.2f} USDT")
                self.price_history.append(current_price)
                self.time_history.append(len(self.price_history))
                
                # تحديث الرسم البياني
                if len(self.price_history) > 100:
                    self.price_history = self.price_history[-100:]
                    self.time_history = self.time_history[-100:]
                
                self.graph_widget.clear()
                self.graph_widget.plot(self.time_history, self.price_history, pen='b')
        
        except Exception as e:
            print(f"خطأ في تحديث البيانات: {e}")

    def toggle_trading(self):
        if self.start_button.text() == "بدء التداول":
            self.start_button.setText("إيقاف التداول")
            self.trader.run()
        else:
            self.start_button.setText("بدء التداول")
            # إيقاف التداول

    def save_settings(self):
        # حفظ الإعدادات في ملف .env
        with open('.env', 'w') as f:
            f.write(f"BINANCE_API_KEY={self.api_key_input.text()}\n")
            f.write(f"BINANCE_API_SECRET={self.api_secret_input.text()}\n")

def main():
    app = QApplication(sys.argv)
    
    # تعيين نمط التطبيق
    app.setStyle('Fusion')
    
    # تطبيق النمط العربي
    app.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
    
    window = CryptoTradingBotGUI()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
