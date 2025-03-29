from fastapi import FastAPI
import cpu_monitor
import memory_monitor
import disk_monitor
import network_monitor
import threading

app = FastAPI()

def run_speed_test():
    download_speed, upload_speed = network_monitor.monitor()
    network_monitor.save_network_data(download_speed, upload_speed)
    print(f"Speed Test Completed: Download {download_speed:.2f} Mbps, Upload {upload_speed:.2f} Mbps")

@app.get("/data")
def get_system_data():
    """Fetch system data from all monitors and return as JSON"""
    try:
        cpu_data = cpu_monitor.monitor() if cpu_monitor else ["N/A"] * 4
        memory_data = memory_monitor.monitor() if memory_monitor else ["N/A"] * 4
        disk_data = disk_monitor.monitor() if disk_monitor else ["N/A"] * 4
        network_data = network_monitor.get_latest_data() if network_monitor else ["N/A"] * 2

        return {
            "cpu": cpu_data,
            "memory": memory_data,
            "disk": disk_data,
            "network": network_data
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/speedtest")
def start_speed_test():
    """Start network speed test in a separate thread."""
    threading.Thread(target=run_speed_test, daemon=True).start()
    return {"message": "Speed test started"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5000)
