import psutil, time, json


#Function to calculate reading and writing speed
def calc_reading(disk_before, disk_after):
    read_speed = (disk_after.read_bytes - disk_before.read_bytes)
    return read_speed
def calc_writing(disk_before,disk_after):
    write_speed = (disk_after.write_bytes - disk_before.write_bytes)
    return write_speed

#Collecting Disk data
total_size = int(psutil.disk_usage('/').total / (1024 * 1024 * 1024))
used_size = int(psutil.disk_usage('/').used / (1024 * 1024 * 1024))
free_size = int(psutil.disk_usage('/').free / (1024 * 1024 * 1024))
percentage = psutil.disk_usage('/').percent



#Calculating reading and writing speed
disk_reading_before = psutil.disk_io_counters()
time.sleep(1)
disk_reading_after = psutil.disk_io_counters()

read_speed = calc_reading(disk_reading_before, disk_reading_after)
write_speed = calc_writing(disk_reading_before, disk_reading_after)


#Opening the .json file or creating one if it doesn't exist:
try:
    with open("data.json", "r") as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    data = {
        "disk": {}
    }

#Appending the new data
data["disk"] = {
        "read_speed" : read_speed,
        "write_speed" : write_speed,
        "percentage" : percentage,
        "total_size" : total_size,
        "used_size" : used_size,
        "free_size" : free_size
    }

#Saving the updated data to the .json file
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)
file.close()



