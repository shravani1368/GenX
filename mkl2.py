import smtplib
from email.message import EmailMessage

def send_email():
    sender_email = "shravaniyenpure10@gmail.com"
    receiver_email = "a92740576@gmail.com"
    app_password = "qlwk gzkb hjmu sxpa"  

    msg = EmailMessage()
    msg["Subject"] = "Bad Words Alert Report"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Bad word detected! See attached report.")

    
    with open("mkl.txt", "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(file_data, maintype="application", subtype="octet-stream", filename=file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

    print(" Email sent successfully!")

def main():
    bad_words = ["dangerous", "dirty", "disaster"]

    print("Start typing (Press Ctrl+C to stop):")

    try:
        with open("mkl.txt", "a") as file:
            while True:
                text = input("Enter text: ")
                words = text.lower().split()

                for word in words:
                    if word in bad_words:
                        message = f"Flagged word detected: {word}\n"
                        print(message)

                        file.write(message)
                        file.flush()

                        send_email()

    except KeyboardInterrupt:
        print("\nProgram stopped.")

if __name__ == "__main__":
    main()