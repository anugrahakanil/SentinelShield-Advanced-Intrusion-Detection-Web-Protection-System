# 🛡️ SentinelShield

**SentinelShield** is a Flask-based Web Application Firewall (WAF) simulation and Intrusion Detection System (IDS) developed to detect and analyze common web application attacks. It provides real-time attack detection, interactive analytics, logging, and security reporting through a user-friendly dashboard.

---

## 📌 Features

- 🔍 Detects common web attacks:
  - Cross-Site Scripting (XSS)
  - SQL Injection
  - Directory Traversal
  - Local File Inclusion (LFI)
  - Command Injection

- 📊 Interactive Dashboard
  - Real-time attack statistics
  - Bar chart visualization
  - Pie chart visualization
  - Threat Intelligence panel

- 📜 Attack Logging
  - Timestamp
  - IP Address
  - Attack Type
  - Payload
  - Severity Level

- 🚨 Security Alerts
  - Malicious request detection
  - Abusive request detection
  - IP attack tracking

- 📄 Security Report Generation
  - Downloadable security report
  - Attack history logging

- 🎯 Attack Simulation Panel
  - Simulate XSS
  - Simulate SQL Injection
  - Simulate Directory Traversal
  - Simulate Local File Inclusion (LFI)
  - Simulate Command Injection

---

## 🏗️ Project Structure

```
SentinelShield/
│
├── dataset/
├── detector/
│   └── waf_engine.py
│
├── logs/
│   └── attack_logs.txt
│
├── model/
│
├── reports/
│   └── security_report.txt
│
├── rules/
│   └── attack_signatures.py
│
├── static/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- Chart.js

---

## 🚀 Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/SentinelShield.git
```

Navigate to the project folder

```bash
cd SentinelShield
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser and visit

```
http://127.0.0.1:5000
```

---

## 🔐 Supported Attack Types

| Attack | Description |
|---------|-------------|
| XSS | Detects Cross-Site Scripting payloads |
| SQL Injection | Detects malicious SQL queries |
| Directory Traversal | Detects path traversal attempts |
| LFI | Detects Local File Inclusion attempts |
| Command Injection | Detects operating system command injection |

---

## 📊 Dashboard Modules

- System Statistics
- Attack Category Analytics
- Threat Intelligence
- Attack Simulation
- Security Alerts
- Recent Attack Logs
- Download Security Report

---

## 📸 Screenshots

Project screenshots are available in the project documentation and demonstrate:

- Dashboard
- Attack Simulation
- XSS Detection
- SQL Injection Detection
- Directory Traversal Detection
- LFI Detection
- Command Injection Detection
- Attack Logs
- Analytics Charts
- Security Report Generation

---

## 📈 Future Enhancements

- Machine Learning based anomaly detection
- User Authentication
- Database integration (SQLite/MySQL)
- Real-time email alerts
- Geo-location based IP tracking
- Advanced threat intelligence feeds
- PDF report generation

---

## 🎯 Learning Outcomes

This project demonstrates:

- Web Application Firewall (WAF) concepts
- Intrusion Detection Systems (IDS)
- Rule-based attack detection
- HTTP request inspection
- Security event logging
- Threat visualization
- Flask web development
- Cybersecurity dashboard implementation

---

## 👨‍💻 Author

**Anugraha K Anil**

B.Tech Computer Science & Engineering (Cyber Security)

---

## 📜 License

This project is developed for educational and learning purposes.