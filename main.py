from src.utilities import has_access_to_internet
from src.utilities import run_speedtest
from src.utilities import add_result_to_logfile
from src.utilities import get_current_date_and_time
from configuration import continuous_run
from configuration import run_every_n_seconds
from configuration import print_result_in_stdout
from time import sleep
import json


def start_run():
    machine_is_online = has_access_to_internet()
    if machine_is_online:
        time_and_date = get_current_date_and_time()
        current_date = time_and_date[0]
        current_time = time_and_date[1]
        speedtest_result = run_speedtest()
        logline = {
            "Date": current_date,
            "Time": current_time,
            "Download mbps": speedtest_result["download"],
            "Upload mbps": speedtest_result["upload"],
            "Ping in ms": speedtest_result["ping"],
            "Test Configuration": speedtest_result["test_configuration"]
        }
        logline = json.dumps(logline, ensure_ascii=False)
        add_result_to_logfile(logline)
        if print_result_in_stdout:
            print(f"{logline}")


def main():
    if continuous_run:
        while True:
            start_run()
            sleep(run_every_n_seconds)
    else:
        start_run()


if __name__ == '__main__':
    main()
