import smtplib


def send_emails(emails, schedule, forecast):
    # connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # start TLS encryption
    server.starttls()

    # login
    from_email = input('Enter your email: ')
    password = input('Enter your password: ')
    server.login(from_email, password)

    # send to email list
    for to_email, name in emails.items():
        message = 'Subject: My Today Schedule!!!\n'
        message += 'Hi ' + name + '!\n\n'
        message += forecast + '\n\n'
        message += schedule + '\n'
        message += 'Have a Nice Day!!!'
        server.sendmail(from_email, to_email, message)

    # close server request
    server.quit()
