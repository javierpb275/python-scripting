import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

if __name__ == '__main__':
    html = Template(Path('index.html').read_text())
    email = EmailMessage()
    email['from'] = 'Python'
    email['to'] = 'pepe@gmail.com'
    email['subject'] = 'Hi! My name is Python!'

    email.set_content(html.substitute({'name': 'Nice to meet you!'}), 'html')

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('python@gmail.com', 'python123.')
        smtp.send_message(email)
        print('OK')

