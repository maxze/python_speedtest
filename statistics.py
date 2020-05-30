from configuration import logfile_location
from src.utilities import calculate_average

import json

with open(logfile_location, "r") as speedtest_results:
    results_download, results_upload, result_ping = [], [], []
    lines = speedtest_results.readlines()
    for one in lines:
        single_result = json.loads(one.strip())
        if single_result["Test Configuration"]["upload_tested"]:
            results_upload.append(float(single_result["Upload mbps"]))
        if single_result["Test Configuration"]["download_tested"]:
            results_download.append(float(single_result["Download mbps"]))
        result_ping.append(float(single_result["Ping in ms"]))

    # calculate average
    average_download_speed = calculate_average(results_download)
    average_upload_speed = calculate_average(results_upload)
    average_ping = calculate_average(result_ping)

    count_download_results = len(results_download)
    count_upload_results = len(results_upload)
    count_ping_results = len(result_ping)

    print(f"Using {count_download_results} results, the average Download Speed was: {average_download_speed} mbps")
    print(f"Using {count_upload_results} results, average Upload Speed was: {average_upload_speed} mbps")
    print(f"Using {count_ping_results} results, the average Ping was: {average_ping} milliseconds")



