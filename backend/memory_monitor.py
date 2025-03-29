<<<<<<< HEAD
import psutil
=======
>>>>>>> str
import json
import time
import threading
from psutil import virtual_memory

<<<<<<< HEAD
# Function to collect memory data
def get_memory_data():
    memory_info = psutil.virtual_memory()
    timestamp = time.time()
    
    return {
        "size": round(memory_info.total / (1024 ** 3), 2),
        "used": round(memory_info.used / (1024 ** 3), 2),
        "percent": memory_info.percent,
        "free": round(memory_info.available / (1024 ** 3), 2),
        "timestamp": timestamp
    }

# Load or initialize data file
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"memory": {"history": []}}

# Save data to JSON file
def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main monitoring loop

data = load_data()

# Initial memory data collection
memory_data = get_memory_data()
data["memory"]["history"].append(memory_data)
if len(data["memory"]["history"]) > 20:
    data["memory"]["history"].pop(0)

save_data(data)

# Restoring data every 3 seconds
while True:
    memory_data = get_memory_data()
    data["memory"]["history"].append(memory_data)
    if len(data["memory"]["history"]) > 20:
        data["memory"]["history"].pop(0)

    save_data(data)
    time.sleep(3)
=======
data_file = "data.json"

def monitor():
    """Fetch memory usage statistics"""
    mem_info = virtual_memory()
    return {
        "usage": mem_info.percent,
        "size": round(mem_info.total / (1024 ** 3), 3),
        "used": round(mem_info.used / (1024 ** 3), 3),
        "free": round(mem_info.free / (1024 ** 3), 3)
    }

def save_memory_data():
    """Fetch and save memory data periodically"""
    while True:
        mem_data = monitor()
        mem_data["timestamp"] = time.time()
        
        try:
            with open(data_file, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {}

        if "memory" not in data:
            data["memory"] = {"history": []}

        data["memory"]["history"].append(mem_data)
        if len(data["memory"]["history"]) > 20:
            data["memory"]["history"].pop(0)

        with open(data_file, "w") as file:
            json.dump(data, file, indent=4)

        time.sleep(3)

threading.Thread(target=save_memory_data, daemon=True).start()
>>>>>>> str
