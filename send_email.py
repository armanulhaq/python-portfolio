import smtplib, ssl

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "armanulhaq10@gmail.com"
    password = "nawy qltn liun cbkq"

    receiver = "armanulhaq10@gmail.com"
    context = ssl.create_default_context()
    #holds various settings and configurations related to establishing secure SSL (Secure Sockets Layer) connections.

    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server: #establishes a secure connection
            server.login(username, password)
            server.sendmail(username, receiver, message)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
