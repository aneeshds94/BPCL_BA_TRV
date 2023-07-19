import random


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


def generate_name(name_list):
    try:
        random_name = random.choice(name_list)
        return random_name
    except:
        pass