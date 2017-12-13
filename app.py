# encoding declaration
"""coding = utf-8"""


# import packages
import weather
import mailer


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


def get_schedule():
    # read external file and verify for error
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule


def main():
    emails = get_emails()

    schedule = get_schedule()

    forecast = weather.get_weather_forecast()

    mailer.send_emails(emails, schedule, forecast)

    print('Done!!!')


# call function main
main()
