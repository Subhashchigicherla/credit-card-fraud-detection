import yagmail

EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_PASSWORD = "your_app_password"  # 16-character Gmail App Password

def send_confirmation_email(to_email, username):
    try:
        yag = yagmail.SMTP(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        subject = "Confirm Your Email - Fraud Detection System"
        contents = f"""
Hi {username},

Thank you for signing up for the Credit Card Fraud Detection System.
Please confirm your email to access the dashboard.

-- Fraud Detection Team
"""
        yag.send(to=to_email, subject=subject, contents=contents)
        return True
    except Exception as e:
        print("Email sending failed:", e)
        return False