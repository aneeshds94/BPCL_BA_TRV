import time
from datetime import datetime
import pytz


# for calculating difference in time between two runs
def get_current_time():
    current_time = time.time()
    return current_time


# IST for display
def get_display_datetime():
    ist = pytz.timezone("Asia/Kolkata")
    datetime_ist = datetime.now(ist)
    display_time = datetime_ist.strftime("%d-%m-%Y %H:%M:%S")
    date = datetime_ist.strftime("%d-%m-%Y")
    return display_time, date





