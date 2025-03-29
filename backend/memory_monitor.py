import json
import time
import threading
from psutil import virtual_memory

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
