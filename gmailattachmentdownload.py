import imaplib
import email
from pathlib import Path

# Gmail login details
EMAIL = 'your_email_address'
PASSWORD = 'your_application-specific_password'
SENDER = 'from_who_email_address'

# Get the downloads folder path
DOWNLOADS_PATH = Path.home() / "Downloads"
OUTPUT_DIR = DOWNLOADS_PATH / "downloaded_attachments"

# Connect to the Gmail IMAP server
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Search for all emails from the given sender
result, data = mail.search(None, f'(FROM "{SENDER}")')
email_ids = data[0].split()

for e_id in email_ids:
    _, msg_data = mail.fetch(e_id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            for part in msg.walk():
                if part.get_content_maintype() == 'multipart':
                    continue
                if part.get('Content-Disposition') is None:
                    continue
                filename = part.get_filename()
                if filename and filename.endswith('.pdf'):
                    filepath = OUTPUT_DIR / filename
                    if not OUTPUT_DIR.exists():
                        OUTPUT_DIR.mkdir(parents=True)
                    with open(filepath, 'wb') as f:
                        f.write(part.get_payload(decode=True))

mail.logout()
