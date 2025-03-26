import psutil
import time
import json
import os

# Define the path of the JSON file in the same directory
disk_json_file = os.path.join(os.path.dirname(__file__), "disk_data.json")

# Function to calculate reading and writing speed
def calc_reading(disk_before, disk_after):
    return disk_after.read_bytes - disk_before.read_bytes

def calc_writing(disk_before, disk_after):
    return disk_after.write_bytes - disk_before.write_bytes

# Collecting Disk data
def get_disk_info():
    total_size = int(psutil.disk_usage('/').total / (1024 ** 3))
    used_size = int(psutil.disk_usage('/').used / (1024 ** 3))
    free_size = int(psutil.disk_usage('/').free / (1024 ** 3))
    percentage = psutil.disk_usage('/').percent
    
    disk_reading_before = psutil.disk_io_counters()
    time.sleep(1)
    disk_reading_after = psutil.disk_io_counters()
    
    read_speed = calc_reading(disk_reading_before, disk_reading_after)
    write_speed = calc_writing(disk_reading_before, disk_reading_after)
    
    return {
        "read_speed": read_speed,
        "write_speed": write_speed,
        "percentage": percentage,
        "total_size": total_size,
        "used_size": used_size,
        "free_size": free_size
    }

# Load existing disk data or create a new structure
def load_disk_data():
    try:
        with open(disk_json_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"disk": {}}

# Save disk data to JSON file
def save_disk_data(data):
    with open(disk_json_file, "w") as file:
        json.dump(data, file, indent=4)

# Main process
disk_data = load_disk_data()
disk_data["disk"] = get_disk_info()
save_disk_data(disk_data)
