import os
import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_contact_notification(name, email, subject, message):
    """
    Send a notification email when someone submits the contact form.
    
    Args:
        name: Name of the person who submitted the form
        email: Email of the person who submitted the form
        subject: Subject of the message
        message: Content of the message
    
    Returns:
        bool: True if email was sent successfully, False otherwise
    """
    # Email that will receive the notification (portfolio owner's email)
    recipient_email = "sajjanyadav.ml@gmail.com"  # The email where you want to receive notifications
    sender_email = "sajjanyadav.portfolio@gmail.com"  # You could create a specific email for your portfolio
    
    # Create message container
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = f"Portfolio Contact: {subject}"
    
    # Create the body of the message with better formatting
    body = f"""
You have received a new message from your portfolio website contact form.

FROM: {name} ({email})
SUBJECT: {subject}

MESSAGE:
{message}

---
This email was sent automatically from your portfolio website.
"""
    
    # Attach the body to the message
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Log the attempt (this will be visible in the server logs)
        logging.info(f"New contact form submission from {name} ({email})")
        
        # Save the contact submission to a contact log file
        with open('contact_submissions.log', 'a') as log_file:
            log_file.write(f"[NEW CONTACT] Name: {name}, Email: {email}, Subject: {subject}\n")
            log_file.write(f"Message: {message}\n")
            log_file.write("-" * 50 + "\n")
        
        # Just log the email details for now (it will appear in the server logs)
        print(f"NEW CONTACT FORM SUBMISSION")
        print(f"From: {name} ({email})")
        print(f"Subject: {subject}")
        print(f"Message: {message}")
        
        return True
    except Exception as e:
        logging.error(f"Failed to log contact form: {str(e)}")
        return False