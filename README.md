Trading Bot | روبوت التداول الآلي للعملات المشفرة

[English](#english) | [العربية](#arabic)

# English

An advanced cryptocurrency trading bot built with Python. Features a professional GUI and supports advanced technical analysis with real-time risk management.

![Capture d’écran 2025-01-02 à 08 28 48](https://github.com/user-attachments/assets/ed002e10-9894-484f-99a6-2b65493dcefa)


![Capture d’écran 2025-01-02 à 08 29 07](https://github.com/user-attachments/assets/1a01690e-6fc8-40f6-835c-c105b37ede1d)


## 🌟 Key Features

- ✨ User-friendly GUI interface
- 📊 Real-time market analysis
- 📈 Interactive price charts
- 🔄 Automated trade execution
- ⚡ Advanced trading strategies (RSI, EMA)
- 🛡️ Automated risk management
- 💼 Binance exchange support

## 💻 System Requirements

- Python 3.8 or newer
- Operating System:
  - Windows 10/11
  - macOS 10.14 or newer
  - Linux (Ubuntu 20.04 or newer)
- Binance account with API keys

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/obaidmedweb/crypto-trading-bot.git
cd crypto-trading-bot
```

2. Create a Python virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install requirements:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory and add your API keys:
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

## 🚀 Usage

### Launch GUI:
```bash
python gui.py
```

### Run Bot without GUI:
```bash
python trader.py
```

## 📁 Project Structure

```
crypto-trading-bot/
├── README.md
├── requirements.txt
├── .env
├── config.py          # System settings and constants
├── gui.py            # Graphical user interface
├── trader.py         # Main trading logic
├── market_data.py    # Market data collection
├── strategy.py       # Trading strategies
└── risk_manager.py   # Risk management
```

## ⚠️ Risk Warning

- Cryptocurrency trading involves significant risk
- Test the bot in a demo environment first
- Never invest more than you can afford to lose
- This bot is for educational and research purposes, use at your own risk

## 🔒 Security

- Never share your API keys
- Restrict API permissions to trading only
- Enable 2FA on your Binance account


---

# العربية

# 🤖 روبوت التداول الآلي للعملات المشفرة

نظام تداول آلي متطور للعملات المشفرة مبني باستخدام Python. يوفر واجهة رسومية احترافية ويدعم التحليل الفني المتقدم مع إدارة المخاطر في الوقت الفعلي.

![لقطة شاشة للبرنامج](screenshot.png)

## 🌟 المميزات الرئيسية

- ✨ واجهة رسومية عربية سهلة الاستخدام
- 📊 تحليل السوق في الوقت الفعلي
- 📈 رسوم بيانية تفاعلية للأسعار
- 🔄 تنفيذ تلقائي للصفقات
- ⚡ استراتيجيات تداول متقدمة (RSI, EMA)
- 🛡️ إدارة المخاطر الآلية
- 💼 دعم منصة Binance

## 💻 متطلبات النظام

- Python 3.8 أو أحدث
- نظام التشغيل:
  - Windows 10/11
  - macOS 10.14 أو أحدث
  - Linux (Ubuntu 20.04 أو أحدث)
- حساب Binance مع مفاتيح API

## ⚙️ التثبيت

1. استنسخ المستودع:
```bash
git clone https://github.com/obaidmedweb/crypto-trading-bot.git
cd crypto-trading-bot
```

2. قم بإنشاء بيئة Python افتراضية:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. قم بتثبيت المتطلبات:
```bash
pip install -r requirements.txt
```

4. قم بإنشاء ملف `.env` في المجلد الرئيسي وأضف مفاتيح API الخاصة بك:
```
BINANCE_API_KEY=your_api_key_here
BINANCE_API_SECRET=your_api_secret_here
```

## 🚀 تشغيل البرنامج

### تشغيل الواجهة الرسومية:
```bash
python gui.py
```

### تشغيل البوت بدون واجهة رسومية:
```bash
python trader.py
```

## 📁 هيكل المشروع

```
crypto-trading-bot/
├── README.md
├── requirements.txt
├── .env
├── config.py          # إعدادات وثوابت النظام
├── gui.py            # الواجهة الرسومية
├── trader.py         # المنطق الرئيسي للتداول
├── market_data.py    # جمع بيانات السوق
├── strategy.py       # استراتيجيات التداول
└── risk_manager.py   # إدارة المخاطر
```

## 🛠️ الإعدادات

يمكنك تعديل الإعدادات التالية في الواجهة الرسومية أو مباشرة في `config.py`:

- زوج العملات للتداول
- نسب وقف الخسارة وجني الأرباح
- إعدادات المؤشرات الفنية (RSI, EMA)
- حجم الصفقات

## ⚠️ تنبيه المخاطر

- التداول في العملات المشفرة ينطوي على مخاطر كبيرة
- قم باختبار البوت في بيئة تجريبية أولاً
- لا تستثمر أكثر مما يمكنك تحمل خسارته
- البوت للأغراض التعليمية والبحثية، استخدمه على مسؤوليتك الخاصة

## 🔒 الأمان

- لا تشارك مفاتيح API الخاصة بك مع أي شخص
- قم بتقييد صلاحيات API للتداول فقط
- فعّل المصادقة الثنائية في حسابك على Binance

## 🤝 المساهمة

نرحب بمساهماتكم! إذا كنت ترغب في المساهمة:

1. Fork المشروع
2. قم بإنشاء فرع للميزة (`git checkout -b feature/amazing-feature`)
3. قم بعمل Commit للتغييرات (`git commit -m 'Add amazing feature'`)
4. قم برفع التغييرات (`git push origin feature/amazing-feature`)
5. قم بفتح Pull Request


## 📧 الدعم

إذا واجهت أي مشاكل أو لديك اقتراحات، يرجى:
- فتح issue في GitHub
- التواصل معنا عبر [البريد الإلكتروني](mailto:abidbenhammadi@gmail.com)

## 🌟 شكر خاص

شكر خاص لجميع المساهمين والمطورين الذين ساعدوا في تطوير هذا المشروع.
