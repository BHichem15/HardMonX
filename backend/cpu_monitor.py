from psutil import cpu_percent, cpu_freq
from cpuinfo import get_cpu_info
import time,json


#Collecting CPU data.
cpu_usage = cpu_percent()
cpu_clock = cpu_freq()
cpu_name = get_cpu_info()['brand_raw']
cpu_cores = get_cpu_info()['count']

try:
    cpu_temp = get_cpu_info()['temp']
except:
    cpu_temp = 0
    pass

timestamp = time.time()

#Storing data in a dictionary
data = {
    "cpu": {
        "name": cpu_name,
        "cores": cpu_cores,
        "history": [
            {"timestamp": timestamp, "usage": cpu_usage, "temperature": cpu_temp, "frequency": cpu_clock.current},
        ]
    }  
}

#Restoring data every 3 seconds
while True:
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except(FileNotFoundError, json.JSONDecodeError):
        data = {"cpu": {
            "name": cpu_name,
            "cores": cpu_cores,
            "history": []}}

    # Collecting new data
    cpu_usage_now = cpu_percent()
    cpu_clock_now = cpu_freq()
    try:
        cpu_temp_now = cpu_temp = get_cpu_info()['temp'].current
    except:
        cpu_temp_now = 0
        pass
    timestamp = time.time()

    # Appending the new data
    data["cpu"]["history"].append({
        "timestamp": timestamp,
        "usage": cpu_usage_now,
        "temperature": cpu_temp_now,
        "frequency": cpu_clock_now.current
        })

    # If the history length passes 20, deleting the first history(queue FIFO)
    if len(data["cpu"]["history"]) > 20:
        data["cpu"]["history"].pop(0)

    # Saving the data into .json file
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)
    file.close()


    # Sleeping for 3 seconds before restarting the loop
    time.sleep(3)



