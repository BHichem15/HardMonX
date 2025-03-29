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
