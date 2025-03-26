from psutil import cpu_percent, cpu_freq
from cpuinfo import get_cpu_info
import time, json, os

# Define the path of the JSON file in the same directory
json_file = os.path.join(os.path.dirname(__file__), "data.json")

# Collect initial CPU data
cpu_usage = cpu_percent()
cpu_clock = cpu_freq()
cpu_name = get_cpu_info().get('brand_raw', 'Unknown')
cpu_cores = get_cpu_info().get('count', 0)

timestamp = time.time()

# Create a dictionary to store data
cpu_data = {
    "cpu": {
        "name": cpu_name,
        "cores": cpu_cores,
        "history": [
            {"timestamp": timestamp, "usage": cpu_usage, "frequency": cpu_clock.current},
        ]
    }
}

# Auto-update loop every 3 seconds
while True:
    try:
        with open(json_file, "r") as file:
            cpu_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        cpu_data = {"cpu": {"name": cpu_name, "cores": cpu_cores, "history": []}}

    # Collect new data
    cpu_usage_now = cpu_percent()
    cpu_clock_now = cpu_freq()
    timestamp = time.time()

    # Append new data to the history
    cpu_data["cpu"]["history"].append({
        "timestamp": timestamp,
        "usage": cpu_usage_now,
        "frequency": cpu_clock_now.current
    })

    # Limit the stored values to 20
    if len(cpu_data["cpu"]["history"]) > 20:
        cpu_data["cpu"]["history"].pop(0)

    # Save data to the JSON file
    with open(json_file, "w") as file:
        json.dump(cpu_data, file, indent=4)
    
    # Wait 3 seconds before the next update
    time.sleep(3)
