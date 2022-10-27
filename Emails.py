import email
from email import message
import os
import random
import smtplib

def automatic_email():
    user = input("Input Your Name >>: ")
    email = input("Input Your Email >>: ")
    message = (f"Dear {User}, Welcome to _")
    s = smtplib.SMTP('smpt.gmail.com', 587)
    s.starttls()
    s.login("Input Your GMAIL Account", "Input Password")
    s.sendmail('&&&&&&&&&&&', email, message)
    print("Email Sent!")
    
automatic_email()