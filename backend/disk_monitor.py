<<<<<<< HEAD
import psutil
import time
import json

# Function to calculate reading and writing speed
def calc_speed(disk_before, disk_after):
    return {
        "read_speed": disk_after.read_bytes - disk_before.read_bytes,
        "write_speed": disk_after.write_bytes - disk_before.write_bytes
    }

# Collecting disk data
def get_disk_data():
    disk_usage = psutil.disk_usage('/')
    disk_reading_before = psutil.disk_io_counters()
    time.sleep(1)
    disk_reading_after = psutil.disk_io_counters()
    
    speeds = calc_speed(disk_reading_before, disk_reading_after)
    timestamp = time.time()

    return {
        "total_size": int(disk_usage.total / (1024 ** 3)),
        "used_size": int(disk_usage.used / (1024 ** 3)),
        "free_size": int(disk_usage.free / (1024 ** 3)),
        "percentage": disk_usage.percent,
        "read_speed": speeds["read_speed"],
        "write_speed": speeds["write_speed"],
        "timestamp": timestamp
    }

# Load or initialize data file
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
                "disk": {
                    "history": []
                        }
                }

# Save data to JSON file
def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main monitoring loop

# Load existing data
data = load_data()

while True:
    disk_data = get_disk_data()
    data["disk"].setdefault("history", []).append(disk_data)
    
    # Keep only last 20 entries
    if len(data["disk"]["history"]) > 20:
        data["disk"]["history"].pop(0)

    save_data(data)
    time.sleep(3)
=======
import json
import time
import threading
import psutil

data_file = "data.json"

def monitor():
    """Fetch disk usage statistics"""
    disk_info = psutil.disk_usage('/')
    return {
        "total": round(disk_info.total / (1024 ** 3), 3),
        "used": round(disk_info.used / (1024 ** 3), 3),
        "free": round(disk_info.free / (1024 ** 3), 3),
        "percent": disk_info.percent
    }

def save_disk_data():
    """Fetch and save disk data periodically"""
    while True:
        disk_data = monitor()
        disk_data["timestamp"] = time.time()
        
        try:
            with open(data_file, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if "disk" not in data:
            data["disk"] = {"history": []}

        data["disk"]["history"].append(disk_data)
        if len(data["disk"]["history"]) > 20:
            data["disk"]["history"].pop(0)

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

        time.sleep(3)

threading.Thread(target=save_disk_data, daemon=True).start()
>>>>>>> str
