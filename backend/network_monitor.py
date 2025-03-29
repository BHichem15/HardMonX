import speedtest
import json
import time

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
