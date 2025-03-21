import threading
import cpu_monitor
import memory_monitor
import disk_monitor
import network_monitor

# Main function
def main():
    # Starting CPU Monitoring
    cpu_thread = threading.Thread(target=cpu_monitor, daemon=True)
    cpu_thread.start()

    # Starting Memory Monitoring
    memory_thread = threading.Thread(target=memory_monitor, daemon=True)
    memory_thread.start()

    # Starting Disk Monitoring
    disk_thread = threading.Thread(target=disk_monitor, daemon=True)
    disk_thread.start()

    # Starting Network Monitoring
    network_thread = threading.Thread(target=network_monitor, daemon=True)
    network_thread.start()
    
    # Running the backend forever
    try:
        while True:
            pass  
    except KeyboardInterrupt:
        print("The Software has stopped.")

# Starting the Function
if __name__ == "__main__":
    main()

