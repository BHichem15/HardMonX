import speedtest
import json
import time

<<<<<<< HEAD
# Function to get network data
def get_network_data():
    try:
        st = speedtest.Speedtest()
        down_speed = round(st.download() / 1_000_000, 2)
        up_speed = round(st.upload() / 1_000_000, 2)
    except Exception as e:
        print(f"Error measuring network speed: {e}")
        down_speed, up_speed = 0, 0

    if down_speed == 0 or up_speed == 0:
        return {"download": "No Internet Connection", "upload": "No Internet Connection"}
    else:
        return {"download": down_speed, "upload": up_speed}

# Load or initialize data file
def load_data(filename="data.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"network": {"history": []}}

# Save data to JSON file
def save_data(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

# Main monitoring loop
while True:
    data = load_data()
    network_data = get_network_data()
    network_data["timestamp"] = time.time()

    # Append the latest network data to history
    if "history" not in data["network"]:
        data["network"]["history"] = []

    data["network"]["history"].append(network_data)

    # Keep only the latest 20 entries
    if len(data["network"]["history"]) > 20:
        data["network"]["history"].pop(0)

    save_data(data)
    time.sleep(5)
=======
data_file = "data.json"

def monitor():
    #Perform a network speed test
    try:
        st = speedtest.Speedtest()
        st.get_best_server()
        download_speed = st.download() / 1024 / 1024 
        upload_speed = st.upload() / 1024 / 1024 
        return download_speed, upload_speed
    except speedtest.ConfigRetrievalError:
        return 0, 0

def save_network_data(download_speed, upload_speed):
    #Save network speed test results
    entry = {
        "timestamp": time.time(),
        "download": round(download_speed,3) if download_speed > 0 else "No Internet Connection",
        "upload": round(upload_speed,3) if upload_speed > 0 else "No Internet Connection"
    }

    try:
        with open(data_file, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = {}

    if "network" not in data:
        data["network"] = {"history": []}

    data["network"]["history"].append(entry)
    if len(data["network"]["history"]) > 20:
        data["network"]["history"].pop(0)

    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

def get_latest_data():
    #Fetch the latest network data
    try:
        with open(data_file, "r") as file:
            data = json.load(file)
        return data.get("network", {}).get("history", [])[-1] if data.get("network", {}).get("history") else {"download": "N/A", "upload": "N/A"}
    except (FileNotFoundError, json.JSONDecodeError):
        return {"download": "N/A", "upload": "N/A"}
>>>>>>> str
