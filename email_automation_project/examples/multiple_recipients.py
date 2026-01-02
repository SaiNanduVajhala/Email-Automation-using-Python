#!/usr/bin/env python3
"""
Send email to multiple recipients.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from email_sender.smtp_client import EmailClient

def main():
    # Initialize client with Gmail provider
    client = EmailClient('gmail')
    
    # Option 1: List of recipients
    recipients = [
        "user1@example.com",
        "user2@example.com", 
        "user3@example.com"
    ]
    
    # Option 2: Get recipients from user input
    print("Enter recipient emails (comma-separated):")
    user_input = input("> ")
    recipients = [email.strip() for email in user_input.split(",")]
    
    # Send email to multiple recipients
    result = client.send_email(
        to=recipients,
        subject="Greetings!🙌",
        body="Thank You!\nNandu"
    )
    
    print(f"Status: {result['status']}")
    print(f"Sent to: {', '.join(result['recipients'])}")

if __name__ == "__main__":
    main()
