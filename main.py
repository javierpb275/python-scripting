import smtplib
from email.message import EmailMessage

if __name__ == '__main__':
    email = EmailMessage()
    email['from'] = 'Python'
    email['to'] = 'pepe@gmail.com'
    email['subject'] = 'hi i am python'

    email.set_content('i am sending you an email')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('python@gmail.com', 'python')
        smtp.send_message(email)
        print('OK')

