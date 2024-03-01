import requests
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

time_date = time.strftime("%H-%M-%S_%d-%m-%Y")

def fetch_website_content(url):
    response = requests.get(url)
    return response.text

def save_html_to_file(html_content, filename):
    with open(filename, 'w') as file:
        file.write(html_content)

def send_email_notification(sender_email, sender_password, receiver_email, subject, message, attachment_filename=None):
    try:
        # Outlook SMTP server details
        smtp_server = 'smtp-mail.outlook.com'
        smtp_port = 587

        # Set up connection to SMTP server
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)

        # Compose email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        if attachment_filename:
            with open(attachment_filename, "rb") as attachment:
                part = MIMEApplication(attachment.read(), Name=attachment_filename)
            part['Content-Disposition'] = f'attachment; filename="{attachment_filename}"'
            msg.attach(part)

        # Send email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email notification sent successfully!")
    except Exception as e:
        print("Error sending email notification:", e)
    finally:
        server.quit()

def check_website_for_changes(url, sender_email, sender_password, receiver_email, interval=5):
    previous_content = fetch_website_content(url)
    
    while True:
        current_content = fetch_website_content(url)
        if current_content != previous_content:
            print("Website has changed!")
            html_filename = f"{time_date}_website_content.html"
            save_html_to_file(current_content, html_filename)
            send_email_notification(sender_email, sender_password, receiver_email, 'Flagged website has changed!', f'''The website {website_url} that you have previously flagged has changed at {time_date}. Please visit the website to see the changes. Any additional changes will be monitored and you will be notified if the website changes again.
                                    
An HTML document has been produced to keep a record of the websites changes and is attached to this email.''', attachment_filename=html_filename)
            previous_content = current_content
        
        time.sleep(interval) 

# Example usage:
website_url = "https://google.com/"  # Replace with the URL of the website you want to monitor
sender_email = "test6454321@outlook.com"  # Outlook email address created for this purpose. Not used for any other purpose. This account holds no sensitive information.
sender_password = "Test!!!!1234"  # Outlook email address created for this purpose. Not used for any other purpose. This account holds no sensitive information.
receiver_email = "test6454321@outlook.com"  # Email address to receive notifications(Your email address)

check_website_for_changes(website_url, sender_email, sender_password, receiver_email)
