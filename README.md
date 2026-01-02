# All Project READMEs

## 1. Email-Automation-using-Python
[![GitHub stars](https://img.shields.io/github/stars/SaiNanduVajhala/Email-Automation-using-Python?style=social)](https://github.com/SaiNanduVajhala/Email-Automation-using-Python)
[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)

Streamline your email workflows with this Python script that automates sending personalized emails, attachments, and HTML content using SMTP. Perfect for bulk notifications, reports, or reminders from your BTech project. [conversation_history:1][web:15]

### Features
- Send plain text, HTML, or rich emails to multiple recipients
- Attach files like PDFs, CSVs, or images dynamically
- Read recipient lists from Excel/CSV for personalization
- Secure Gmail SMTP integration with app passwords
- Customizable templates for professional emails [conversation_history:3]

### Quick Start
```python
from email_automator import send_email

send_email(to="user@example.com", subject="Update", body="Hello!")
send_email(to="team@company.com", attachment="report.pdf")
html = f"<h2>Hi {name}!</h2>"
send_email(to=email, body=html, is_html=True)

### Project Structure
├── email_automator.py
├── recipients.xlsx
├── templates/
├── attachments/
├── requirements.txt
└── README.md

### Contributing
1. Fork the repo
2. Create feature branch: `git checkout -b feature/email-scheduling`
3. Commit: `git commit -m 'Add scheduling support'`
4. Push: `git push origin feature/email-scheduling`
5. Open PR [conversation_history:2]

MIT License - Free to use in your full-stack/AI projects!
