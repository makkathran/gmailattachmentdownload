# Gmail Attachment Downloader

## Description

A Python script that automates the process of connecting to Gmail via IMAP, searching for emails from a specified sender, and downloading PDF attachments. The attachments are saved to the user's `Downloads` directory under a folder named `downloaded_attachments`.

## Requirements

- Python 3.x
- `imaplib` and `email` libraries (typically come with the standard Python distribution)

## Setup

1. **Clone the repository**:

2. **Navigate to the directory**:

3. **Update the script**:
Open `gmailattachmentdownload.py` in your favorite editor. Update the following placeholders with your credentials and desired settings:

- `your_email_address`: Your Gmail email address.
- `your_application-specific_password`: Your Gmail app-specific password.
- `from_who_email_address`: The email address of the sender whose emails you want to search.

## Usage

1. **Run the script**:

2. Check the `Downloads/downloaded_attachments` directory for the downloaded PDF attachments.

## Notes

- Ensure you have set up an [application-specific password](https://support.google.com/accounts/answer/185833) for your Gmail account. This is required to securely connect to the Gmail IMAP server.
- The script is currently set to only download `.pdf` attachments. You can modify this by changing the respective condition in the script.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
