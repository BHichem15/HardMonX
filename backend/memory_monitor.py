from psutil import virtual_memory
import json
import time


mem_size = float(virtual_memory().total / (1024 ** 3))
mem_used = float(virtual_memory().used / (1024 ** 3))
mem_percent = virtual_memory().percent 
mem_free = float(virtual_memory().available / (1024 ** 3))
timestamp = time.time()

#Storing data in a dictionary
data = {
    "memory": {
        "history": [{
            "timestamp": timestamp,
            "size": mem_size,
            "used": mem_used,
            "percent": mem_percent,
            "free": mem_free
        }]
    }
}


#Restoring data every 3 seconds
while True:
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {"memory": {"history": {}}}

    #Collecting new data
    mem_size_now = round(virtual_memory().total / (1024 ** 3),2)
    mem_usage_now = round(virtual_memory().used / (1024 ** 3),2)
    mem_percent_now = virtual_memory().percent
    mem_free_now = round(virtual_memory().available / (1024 ** 3),2)
    timestamp_now = time.time()
    
    #Appending the new data
    data["memory"]["history"].append({
        "timestamp": timestamp_now,
        "size": mem_size_now,
        "used": mem_usage_now,
        "percent": mem_percent_now,
        "free": mem_free_now
    })

    #If the history length passes 20, deleting the first history(queue FIFO)
    if len(data["memory"]["history"]) > 20:
        data["memory"]["history"].pop(0)
    
    #Saving the data into .json file
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)
    file.close()


    #Sleeping for 3 seconds before restarting the loop
    time.sleep(3)
