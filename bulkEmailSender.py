import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from rich.console import Console
from rich.prompt import Prompt
from rich.progress import track

console = Console()

# Function to send an email
def send_email(to_address, subject, body, email_address, email_password):
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(email_address, email_password)
        server.send_message(msg)

# Function to read recipients from CSV and send emails with a delay
def send_emails_from_csv(file_path, email_address, email_password, body_template, delay):
    recipients = pd.read_csv(file_path)
    
    for index, row in track(recipients.iterrows(), description="Sending emails...", total=len(recipients)):
        to_address = row['email']
        body = body_template
        send_email(to_address, "Hello!", body, email_address, email_password)
        console.print(f"[green]Email sent to {to_address}[/green]")
        time.sleep(delay)
    
    console.print("[bold green]All emails sent successfully![/bold green]")

# Main function
if __name__ == '__main__':
    SMTP_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 587

    console.print("[bold cyan]###############################[/bold cyan]")
    console.print("[bold cyan]      BULK EMAIL SENDER       [/bold cyan]")
    console.print("[bold cyan]###############################[/bold cyan]")

    console.print("\nCreated by: [blue]Your Name[/blue]")
    console.print("GitHub: [blue]https://github.com/yourusername[/blue]\n")

    # Prompt the user to enter their email credentials
    email_address = Prompt.ask("Enter your email address")

    # Prompt the user to enter their email password (masked)
    email_password = Prompt.ask("Enter your email password", password=True)

    # Prompt the user to enter the path to the CSV file
    csv_file_path = Prompt.ask("Enter the path to your CSV file")

    # Prompt the user to enter the body of the email
    body_template = Prompt.ask("Enter the body of the email")

    # Prompt the user to enter the delay between emails
    delay = float(Prompt.ask("Enter the delay between emails (in seconds): "))

    # Send emails to the recipients listed in the CSV file with a delay
    send_emails_from_csv(csv_file_path, email_address, email_password, body_template, delay)
