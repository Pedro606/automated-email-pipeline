# Automated Email Pipeline 📧

Professional Python automation pipeline for sending scheduled emails with dynamic file attachments.

---

## Features

- Automated email sending
- File processing pipeline
- Scheduled execution
- Logging system
- Environment variable security
- Modular architecture

---

## Project Structure

``` id="a9"
automated-email-pipeline/
├── src/
├── data/
├── logs/
├── .env
├── requirements.txt
└── README.md
Installation
pip install -r requirements.txt
Configuration

Create a .env file:

SMTP_SERVER=smtp.office365.com
SMTP_PORT=587

EMAIL_ADDRESS=your_email@company.com
EMAIL_PASSWORD=your_password
Usage

Place files inside:

data/input/

Run:

python src/scheduler.py
Pipeline Flow
Detect latest file
Create temporary copy
Send email with attachment
Archive processed file
Write logs
Technologies
Python
SMTP
schedule
pathlib
pandas
dotenv
Future Improvements
Retry queue system
HTML email templates
Multi-recipient groups
Docker support
Web dashboard
Email tracking
License

MIT


---

# 🚀 Como subir no GitHub

## 1. Criar pasta do projeto

```text id="a14"
automated-email-pipeline