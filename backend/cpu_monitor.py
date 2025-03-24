import psutil
from cpuinfo import get_cpu_info
import time
import json

# Collecting CPU data.
def get_cpu_data():
    cpu_usage = psutil.cpu_percent()
    cpu_clock = psutil.cpu_freq()
    cpu_name = get_cpu_info()['brand_raw']
    cpu_cores = get_cpu_info()['count']

    try:
        cpu_temp = psutil.sensors_temperatures().get('coretemp', [{}])[0].get('current', 0)
    except:
        cpu_temp = 0

    timestamp = time.time()

    return {
        "name": cpu_name,
        "cores": cpu_cores,
        "usage": cpu_usage,
        "temperature": cpu_temp,
        "frequency": cpu_clock.current,
        "timestamp": timestamp
    }

# Load or initialize data file
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"cpu": {"name": "", "cores": 0, "history": []}}

# Save data to JSON file
def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main monitoring loop
data = load_data()

# Updating CPU info initially
cpu_data = get_cpu_data()
data["cpu"]["name"] = cpu_data["name"]
data["cpu"]["cores"] = cpu_data["cores"]

data["cpu"]["history"].append(cpu_data)
if len(data["cpu"]["history"]) > 20:
    data["cpu"]["history"].pop(0)

save_data(data)

# Restoring data every 3 seconds
while True:
    cpu_data = get_cpu_data()
    data["cpu"]["history"].append(cpu_data)
    if len(data["cpu"]["history"]) > 20:
        data["cpu"]["history"].pop(0)

    save_data(data)
    time.sleep(3)
