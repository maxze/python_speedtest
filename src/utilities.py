import requests
from configuration import logfile_location
from configuration import test_download, test_upload
from datetime import datetime
from speedtest import Speedtest


def has_access_to_internet():
    # tries to ping google.com to see if we're online
    resp = requests.get("https://www.google.de")
    if resp.status_code == 200:
        return True
    else:
        return False


def bits_to_mbit(bits):
    # converts bits to the more readable megabits
    mbits = bits / 1048576
    return "%.3f" % mbits


def get_current_date_and_time():
    now = datetime.now()  # current date and time
    date_time = now.strftime("%Y.%m.%d %H:%M:%S")
    date_and_time_split = date_time.split(" ")
    date = date_and_time_split[0]
    time = date_and_time_split[1]
    return date, time


def add_result_to_logfile(text_to_write):
    with open(logfile_location, "a+") as logfile:
        logfile.write(str(text_to_write) + "\n")


def run_speedtest():
    a = Speedtest()
    if test_download:
        a.download()
    if test_upload:
        a.upload()
    result = a.results.dict()
    download_speed = bits_to_mbit(result["download"])
    upload_speed = bits_to_mbit(result["upload"])
    ping = str(result["ping"])
    test_configuration = {"upload_tested": test_upload, "download_tested": test_download}
    return {"upload": upload_speed, "download": download_speed, "ping": ping, "test_configuration": test_configuration}


def calculate_average(list_of_results):
    sum_of_all_values = 0
    for result in list_of_results:
        sum_of_all_values = sum_of_all_values + result
    calculated_average = sum_of_all_values / len(list_of_results)
    return "%.3f" % calculated_average