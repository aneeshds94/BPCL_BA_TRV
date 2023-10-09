import random
from send_email import send_email
import timer
import pandas as pd

date = timer.get_display_datetime()[1]


def get_names(filepath='employee_list.txt'):
    with open(filepath, 'r') as file:
        return file.readlines()


def get_time():
    with open('time.txt', 'r') as file:
        last_time = float(file.read())
        return last_time


def post_time(last_time):
    with open('time.txt', 'w') as file:
        file.write(str(last_time))


def generate_name(name_list, shift):
    try:
        random_name = random.choice(name_list)
        message = f"""\
Subject: IOCL BA Test

The following employee has been selected for BA test on {date} Shift {shift}:
{random_name}
"""
        send_email(message)
        return random_name
    except:
        pass

