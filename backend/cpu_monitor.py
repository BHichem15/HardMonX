<<<<<<< HEAD
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
=======
import json
import time
import threading
import psutil, cpuinfo

data_file = "data.json"

def monitor():
    """Fetch CPU usage statistics"""
    cpu_name = cpuinfo.get_cpu_info()['brand_raw']
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_freq = psutil.cpu_freq().current if psutil.cpu_freq() else 0
    cpu_cores = psutil.cpu_count(logical=False)
    return {
        "name": cpu_name,
        "usage": cpu_usage,
        "frequency": round(cpu_freq, 2),
        "cores": cpu_cores,
    }

def save_cpu_data():
    """Fetch and save CPU data periodically"""
    while True:
        cpu_data = monitor()
        cpu_data["timestamp"] = time.time()
        
        try:
            with open(data_file, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if "cpu" not in data:
            data["cpu"] = {"history": []}

        data["cpu"]["history"].append(cpu_data)
        if len(data["cpu"]["history"]) > 20:
            data["cpu"]["history"].pop(0)

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

        time.sleep(3)

threading.Thread(target=save_cpu_data, daemon=True).start()
>>>>>>> str
