# Bulk Email Sender

A Python script to send bulk emails using a CSV file. The script uses the `smtplib` library to connect to an SMTP server and send emails to a list of recipients.

## Features

- Send bulk emails using a CSV file containing email addresses.
- Customize the body of the email.
- Add a delay between sending each email to avoid spam filters.

## Prerequisites

- Python 3.x
- `pandas` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Ms-Pankhania/bulk-email-sender.git
    cd bulk-email-sender
    ```

2. Install the required Python libraries:

    ```bash
    pip install pandas
    ```

## Usage

1. Prepare a CSV file (`recipients.csv`) with a column named `email` containing the email addresses of the recipients.

    Example `recipients.csv`:

    ```csv
    email
    recipient1@example.com
    recipient2@example.com
    ```

2. Run the script:

    ```bash
    python bulk_email_sender.py
    ```

3. Enter the required information when prompted:

    - Your email address
    - Your email password (Note: It's recommended to use an app-specific password or OAuth2 for Gmail)
    - The path to your CSV file
    - The body of the email (This will be the same for all recipients)
    - The delay between sending each email (in seconds)

## Notes

- Ensure that the SMTP server and port are correctly configured.
- For Gmail users, it's recommended to use an app-specific password instead of your regular email password for security reasons.
- Respect the privacy of your recipients and comply with email regulations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

