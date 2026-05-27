import time
from datetime import datetime

import schedule

from email_sender import send_email
from file_processor import prepare_file, archive_file


RECIPIENTS = [
    "example@email.com"
]


def run_pipeline():

    file_path = prepare_file()

    if not file_path:
        return

    subject = f"Automated Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

    body = """
    <h3>Automated report attached.</h3>
    <p>This email was generated automatically.</p>
    """

    success = send_email(
        subject=subject,
        body=body,
        attachment_path=file_path,
        recipients=RECIPIENTS
    )

    if success:
        archive_file(file_path)


# Run immediately
run_pipeline()

# Schedule every 60 minutes
schedule.every(60).minutes.do(run_pipeline)

print("Scheduler started...")

while True:

    schedule.run_pending()
    time.sleep(1)