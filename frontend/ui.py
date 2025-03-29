import tkinter as tk
import threading
import requests
import ui_styles as style

API_URL = "http://127.0.0.1:5000/data"
SPEEDTEST_URL = "http://127.0.0.1:5000/speedtest"

class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HardMonX")
        self.root.geometry("480x775")
        self.root.resizable(False, False)
        self.root.configure(bg=style.COLOR_BACKGROUND)

        self.setup_ui()
        self.auto_refresh()

    def setup_ui(self):
        # Set up the UI components
        title_label = tk.Label(self.root, text="HardMonX", **style.title_style)
        title_label.pack(pady=10)

        # Manual refresh button
        self.refresh_button = tk.Button(self.root, text="Refresh Data", command=self.update_ui, **style.button_style)
        self.refresh_button.pack(pady=10)

        # Data frame
        self.info_frame = tk.Frame(self.root, **style.frame_style)
        self.info_frame.pack(pady=20, fill=tk.BOTH, expand=True)

        # CPU Information
        self.cpu_frame = tk.LabelFrame(self.info_frame, text="CPU Information", **style.label_style)
        self.cpu_frame.pack(fill=tk.X, padx=10, pady=5)
        self.cpu_name_label = tk.Label(self.cpu_frame, text="CPU Name: Loading...", **style.data_style)
        self.cpu_name_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_usage_label = tk.Label(self.cpu_frame, text="CPU Usage: Loading...", **style.data_style)
        self.cpu_usage_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_freq_label = tk.Label(self.cpu_frame, text="CPU Frequency: Loading...", **style.data_style)
        self.cpu_freq_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_cores_label = tk.Label(self.cpu_frame, text="CPU Cores: Loading...", **style.data_style)
        self.cpu_cores_label.pack(anchor="w", padx=10, pady=5)

        # Memory Information
        self.memory_frame = tk.LabelFrame(self.info_frame, text="Memory Information", **style.label_style)
        self.memory_frame.pack(fill=tk.X, padx=10, pady=5)
        self.memory_usage_label = tk.Label(self.memory_frame, text="Memory Usage: Loading...", **style.data_style)
        self.memory_usage_label.pack(anchor="w", padx=10, pady=5)
        self.memory_size_label = tk.Label(self.memory_frame, text="Memory Size: Loading...", **style.data_style)
        self.memory_size_label.pack(anchor="w", padx=10, pady=5)
        self.memory_used_label = tk.Label(self.memory_frame, text="Memory Used: Loading...", **style.data_style)
        self.memory_used_label.pack(anchor="w", padx=10, pady=5)
        self.memory_free_label = tk.Label(self.memory_frame, text="Memory Free: Loading...", **style.data_style)
        self.memory_free_label.pack(anchor="w", padx=10, pady=5)

        # Disk Information
        self.disk_frame = tk.LabelFrame(self.info_frame, text="Disk Information", **style.label_style)
        self.disk_frame.pack(fill=tk.X, padx=10, pady=5)
        self.disk_usage_label = tk.Label(self.disk_frame, text="Disk Usage: Loading...", **style.data_style)
        self.disk_usage_label.pack(anchor="w", padx=10, pady=5)
        self.disk_total_label = tk.Label(self.disk_frame, text="Disk Total: Loading...", **style.data_style)
        self.disk_total_label.pack(anchor="w", padx=10, pady=5)
        self.disk_used_label = tk.Label(self.disk_frame, text="Disk Used: Loading...", **style.data_style)
        self.disk_used_label.pack(anchor="w", padx=10, pady=5)
        self.disk_free_label = tk.Label(self.disk_frame, text="Disk Free: Loading...", **style.data_style)
        self.disk_free_label.pack(anchor="w", padx=10, pady=5)

        # Network Information
        self.network_frame = tk.LabelFrame(self.info_frame, text="Network Information", **style.label_style)
        self.network_frame.pack(fill=tk.X, padx=10, pady=5)
        self.network_download_label = tk.Label(self.network_frame, text="Download Speed: Loading...", **style.data_style)
        self.network_download_label.pack(anchor="w", padx=10, pady=5)
        self.network_upload_label = tk.Label(self.network_frame, text="Upload Speed: Loading...", **style.data_style)
        self.network_upload_label.pack(anchor="w", padx=10, pady=5)

        # Internet Speed Test Button
        self.speedtest_button = tk.Button(self.network_frame, text="Test Internet Speed", command=self.run_speedtest, **style.button_style)
        self.speedtest_button.pack(pady=5)

    def auto_refresh(self):
        """Refresh UI every 3 seconds without freezing"""
        self.update_ui()
        self.root.after(3000, self.auto_refresh)

    def update_ui(self):
        """Fetch data from backend API and update UI"""
        try:
            response = requests.get(API_URL)
            data = response.json()

            # Update CPU
            self.cpu_name_label.config(text=f"CPU Name: {data['cpu']['name']}")
            self.cpu_usage_label.config(text=f"CPU Usage: {data['cpu']['usage']}%")
            self.cpu_freq_label.config(text=f"CPU Frequency: {data['cpu']['frequency']} MHz")
            self.cpu_cores_label.config(text=f"CPU Cores: {data['cpu']['cores']}")

            # Update Memory
            self.memory_usage_label.config(text=f"Memory Usage: {data['memory']['usage']}%")
            self.memory_size_label.config(text=f"Memory Size: {data['memory']['size']} GB")
            self.memory_used_label.config(text=f"Memory Used: {data['memory']['used']} GB")
            self.memory_free_label.config(text=f"Memory Free: {data['memory']['free']} GB")

            # Update Disk
            self.disk_usage_label.config(text=f"Disk Usage: {data['disk']['percent']}%")
            self.disk_total_label.config(text=f"Disk Total: {data['disk']['total']} GB")
            self.disk_used_label.config(text=f"Disk Used: {data['disk']['used']} GB")
            self.disk_free_label.config(text=f"Disk Free: {data['disk']['free']} GB")

            # Update Network
            latest_network = data.get("network", {})
            self.network_download_label.config(text=f"Download Speed: {latest_network.get('download', 'N/A')} Mbps")
            self.network_upload_label.config(text=f"Upload Speed: {latest_network.get('upload', 'N/A')} Mbps")

        except Exception as e:
            print("Error fetching data:", e)

    def run_speedtest(self):
        """Run internet speed test in the background"""
        threading.Thread(target=self.speedtest_request, daemon=True).start()

    def speedtest_request(self):
        """Send request to backend to perform speed test"""
        try:
            response = requests.post(SPEEDTEST_URL)
            print("Speed test started successfully!")
        except Exception as e:
            print("Error during speed test:", e)

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
