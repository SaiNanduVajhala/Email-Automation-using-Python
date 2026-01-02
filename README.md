# Email Automation using Python 🚀

[![GitHub stars](https://img.shields.io/github/stars/SaiNanduVajhala/Email-Automation-using-Python?style=social)](https://github.com/SaiNanduVajhala/Email-Automation-using-Python)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

Streamline your email workflows with this Python script that automates sending personalized emails, attachments, and HTML content using SMTP. Perfect for bulk notifications, reports, or reminders from your BTech projects portfolio.

## ✨ Features
- Send plain text, HTML, or rich emails to multiple recipients
- Attach files like PDFs, CSVs, or images dynamically
- Read recipient lists from Excel/CSV for personalization
- Secure Gmail SMTP integration with app passwords
- Customizable templates for professional emails

## 📦 Quick Start
1. **Clone the repo:**
   ```bash
   git clone https://github.com/SaiNanduVajhala/Email-Automation-using-Python.git
   cd Email-Automation-using-Python
Install dependencies:

'''bash
pip install smtplib pandas openpyxl email
Setup Gmail: Enable 2FA → Generate App Password → Update credentials

Prepare recipients.xlsx:

Name	Email
John	john@example.com
Jane	jane@example.com
Run: python email_automator.py

💻 Usage Examples
'''python
# Simple email
send_email(to="user@example.com", subject="Update", body="Hello!")

# With attachment
send_email(to="team@company.com", attachment="report.pdf")

# HTML personalized
html = f"<h2>Hi {name}!</h2>"
send_email(to=email, body=html, is_html=True)
🛠️ Project Structure

├── email_automator.py
├── recipients.xlsx
├── templates/
├── attachments/
├── requirements.txt
└── README.md
🔒 Security
'''python
import os
password = os.getenv('GMAIL_APP_PASSWORD')
🤝 Contributing
Fork → Branch → Commit → PR

📄 License
MIT [web:72]
