# /usr/local/bin/python
# encoding declaration
"""coding = utf-8"""


# import packages
from colorama import Fore, Back
import weather
import mailer


# function definition
def get_emails():
    # # method of list
    # emails = []
    #
    # # read external file and verify for error
    # try:
    #     email_file = open('emails.txt', 'r')
    #     for line in email_file:
    #         emails.append(line.strip())
    # except FileNotFoundError as err:
    #     print(err)
    #
    # return emails

    # method of dictionery
    emails = {}

    # read external file and verify for error
    try:
        email_file = open('emails2.txt', 'r')
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()
    except FileNotFoundError as err:
        print(err)

    return emails


def get_message():
    # read external file and verify for error
    try:
        message_file = open('message.txt', 'r')
        message = message_file.read()
    except FileNotFoundError as err:
        print(err)

    return message


def main():
    emails = get_emails()

    message = get_message()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, message, forecast)

    print(Back.GREEN + Fore.WHITE + ' Done!!! ' + Fore.RESET + Back.RESET + '\n')


# call function main
main()
