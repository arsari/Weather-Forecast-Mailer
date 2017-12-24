# /usr/local/bin/python
# encoding declaration
"""coding = utf-8"""


# import package
from colorama import Fore, Style
import smtplib


# function definition
def send_emails(emails, message, forecast):
    # connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    # start TLS encryption
    server.starttls()

    # login
    print(Fore.RED + '\n===========================================' + Fore.YELLOW + 'v1.1.171223' + Fore.RESET)
    print(Fore.CYAN + 'This Python2/Python3 script will email a local weather\nforecast and a message to a list of contacts.' + Style.DIM + Fore.WHITE + '\n(For exit, enter 0 in any of the inputs.)' + Fore.RESET + Style.RESET_ALL)
    print(Fore.BLUE + '----------------------------------------------------' + Fore.RESET)
    from_email = input('Enter your email: ')
    password = input('Enter your password: ')
    print(Fore.RED + '======================================================\n' + Fore.RESET)
    server.login(from_email, password)

    # send to email list
    for to_email, name in emails.items():
        body_msg = 'Subject: For Your Information!!!\n'
        body_msg += 'Hi ' + name + '!\n\n'
        body_msg += forecast + '\n\n'
        body_msg += message + '\n'
        body_msg += 'Have a Nice Day!!!'
        server.sendmail(from_email, to_email, body_msg)

    # close server request
    server.quit()
