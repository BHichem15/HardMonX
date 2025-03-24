import speedtest
import json
import time

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
