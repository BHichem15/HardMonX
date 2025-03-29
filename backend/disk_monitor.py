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
