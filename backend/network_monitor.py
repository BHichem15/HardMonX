import speedtest, json

#Collecting upload & download speed and ping data
down_speed = round(speedtest.Speedtest().download()/1000000,2)
up_speed = round(speedtest.Speedtest().upload()/1000000,2)

if (down_speed == 0 or up_speed == 0):
    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        data = {
        "network": {}
        }

    data["network"] = {
    "download": "No Internet Connection",
    "upload": "No Internet Connection"
    }
    with open("data.json","w") as file:
        json.dump(data,file,indent=4)
else:

    try:
        with open("data.json","r") as file:
            data = json.load(file)
    except (FileNotFoundError,json.decoder.JSONDecodeError):
        data = {
            "network": {}
        }

    data["network"] = {
        "download": down_speed,
        "upload": up_speed
    }

    with open("data.json","w") as file:
        json.dump(data,file,indent=4)
