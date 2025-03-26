from psutil import virtual_memory
import json
import time
import os

# Define the path of the JSON file in the same directory
json_file = os.path.join(os.path.dirname(__file__), "data.json")

def get_memory_info():
    """Collects current memory usage data."""
    return {
        "timestamp": time.time(),
        "size": round(virtual_memory().total / (1024 ** 3), 2),
        "used": round(virtual_memory().used / (1024 ** 3), 2),
        "percent": virtual_memory().percent,
        "free": round(virtual_memory().available / (1024 ** 3), 2)
    }

# Initial memory data collection
data = {"memory": {"history": [get_memory_info()]}}

# Automatic data update every 3 seconds
while True:
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"memory": {"history": []}}

    # Collect new data
    data["memory"]["history"].append(get_memory_info())

    # If history length exceeds 20, remove the oldest entry (FIFO queue)
    if len(data["memory"]["history"]) > 20:
        data["memory"]["history"].pop(0)
    
    # Save the data to a JSON file
    with open(json_file, "w") as file:
        json.dump(data, file, indent=4)
    
    # Sleep for 3 seconds before the next update
    time.sleep(3)
