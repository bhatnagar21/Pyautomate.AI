import smtplib
import ssl

if __name__ == "__main__":
    result = send_email( # type: ignore
        "shreyabhatnagar49@gmail.com",
        "rfxvtxintclidrym",
        "abhishantruhelarajput7@gmail.com",
        "Test from Script",
        "This is just a test."
    )
    print(result)


def send_email(sender_email, app_password, receiver_email, subject, body):
    try:
        email_message = f"Subject: {subject}\n\n{body}"
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, email_message)
        return "✅ Email sent successfully!"
    except Exception as e:
        return f"❌ Error: {e}"
