import tkinter as tk
from tkinter import ttk
import json
import threading
import time
import os
import ui_styles as style


class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HardMonX")
        self.root.geometry("480x775")
        self.root.resizable(False, False)
        self.root.configure(bg=style.COLOR_BACKGROUND)
        
        # Define the full path of the JSON file in the backend
        self.data_file = os.path.join(os.path.dirname(__file__), "..", "backend", "data.json")
        
        # Set up the user interface
        self.setup_ui()
        
        # Start automatic refresh
        self.start_auto_refresh()

    def setup_ui(self):
        # User interface settings
        title_label = tk.Label(self.root, text="HardMonX", **style.title_style)
        title_label.pack(pady=10)

        # Manual refresh button
        self.refresh_button = tk.Button(self.root, text="Refresh Data", command=self.refresh_data, **style.button_style)
        self.refresh_button.pack(pady=10)
        
        # Data frame
        self.info_frame = tk.Frame(self.root, **style.frame_style)
        self.info_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # CPU information
        self.cpu_frame = tk.LabelFrame(self.info_frame, text="CPU Information", **style.label_style)
        self.cpu_frame.pack(fill=tk.X, padx=10, pady=5)
        self.cpu_name_label = tk.Label(self.cpu_frame, text="CPU Name: Loading...", **style.data_style)
        self.cpu_name_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_core_label = tk.Label(self.cpu_frame, text="CPU Cores: Loading...", **style.data_style)
        self.cpu_core_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_usage_label = tk.Label(self.cpu_frame, text="CPU Usage: Loading...", **style.data_style)
        self.cpu_usage_label.pack(anchor="w", padx=10, pady=5)
        self.cpu_frequency_label = tk.Label(self.cpu_frame, text="CPU Frequency: Loading...", **style.data_style)
        self.cpu_frequency_label.pack(anchor="w", padx=10, pady=5)

        # Memory information
        self.memory_frame = tk.LabelFrame(self.info_frame, text="Memory Information", **style.label_style)
        self.memory_frame.pack(fill=tk.X, padx=10, pady=5)
        self.memory_usage_label = tk.Label(self.memory_frame, text="Memory Usage: Loading...", **style.data_style)
        self.memory_usage_label.pack(anchor="w", padx=10, pady=5)
        self.memory_total_label = tk.Label(self.memory_frame, text="Total Memory: Loading...", **style.data_style)
        self.memory_total_label.pack(anchor="w", padx=10, pady=5)
        self.memory_free_label = tk.Label(self.memory_frame, text="Free Memory: Loading...", **style.data_style)
        self.memory_free_label.pack(anchor="w", padx=10, pady=5)

        # Disk information
        self.disk_frame = tk.LabelFrame(self.info_frame, text="Disk Information", **style.label_style)
        self.disk_frame.pack(fill=tk.X, padx=10, pady=5)
        self.disk_usage_label = tk.Label(self.disk_frame, text="Disk Usage: Loading...", **style.data_style)
        self.disk_usage_label.pack(anchor="w", padx=10, pady=5)
        self.disk_total_label = tk.Label(self.disk_frame, text="Total Disk Size: Loading...", **style.data_style)
        self.disk_total_label.pack(anchor="w", padx=10, pady=5)
        self.disk_free_label = tk.Label(self.disk_frame, text="Free Disk Space: Loading...", **style.data_style)
        self.disk_free_label.pack(anchor="w", padx=10, pady=5)

        # Network information
        self.network_frame = tk.LabelFrame(self.info_frame, text="Network Information", **style.label_style)
        self.network_frame.pack(fill=tk.X, padx=10, pady=5)
        self.network_download_label = tk.Label(self.network_frame, text="Download Speed: Loading...", **style.data_style)
        self.network_download_label.pack(anchor="w", padx=10, pady=5)
        self.network_upload_label = tk.Label(self.network_frame, text="Upload Speed: Loading...", **style.data_style)
        self.network_upload_label.pack(anchor="w", padx=10, pady=5)

    def refresh_data(self):
        self.update_ui_from_json()

    def start_auto_refresh(self):
        self.auto_refresh_thread = threading.Thread(target=self.auto_refresh, daemon=True)
        self.auto_refresh_thread.start()

    def auto_refresh(self):
        while True:
            self.root.after(0, self.update_ui_from_json)
            time.sleep(3)

    def update_ui_from_json(self):
        try:
            with open(self.data_file, "r") as file:
                data = json.load(file)
                
                # Update CPU data
                cpu_data = data.get("cpu", {})
                self.cpu_name_label.config(text=f"CPU Name: {cpu_data.get('name', 'N/A')}")
                self.cpu_core_label.config(text=f"CPU Cores: {cpu_data.get('cores', 'N/A')}")
                latest_cpu_usage = cpu_data.get("history", [{}])[-1].get("usage", "N/A")
                self.cpu_usage_label.config(text=f"CPU Usage: {latest_cpu_usage}%")
                latest_cpu_frequency = cpu_data.get("history", [{}])[-1].get("frequency", "N/A")
                self.cpu_frequency_label.config(text=f"CPU Frequency: {latest_cpu_frequency} MHz")
                
                # Update memory data
                memory_data = data.get("memory", {})
                latest_memory_usage = memory_data.get("history", [{}])[-1].get("percent", "N/A")
                self.memory_usage_label.config(text=f"Memory Usage: {latest_memory_usage}%")
                latest_memory_total = memory_data.get("history", [{}])[-1].get("size", "N/A")
                self.memory_total_label.config(text=f"Total Memory: {latest_memory_total} GB")
                latest_memory_free = memory_data.get("history", [{}])[-1].get("free", "N/A")
                self.memory_free_label.config(text=f"Free Memory: {latest_memory_free} GB")
                
                # Update disk data
                disk_data = data.get("disk", {})
                self.disk_usage_label.config(text=f"Disk Usage: {disk_data.get('percentage', 'N/A')}%")
                self.disk_total_label.config(text=f"Total Disk Size: {disk_data.get('total_size', 'N/A')} GB")
                self.disk_free_label.config(text=f"Free Disk Space: {disk_data.get('free_size', 'N/A')} GB")
                
                # Update network data
                network_data = data.get("network", {})
                self.network_download_label.config(text=f"Download Speed: {network_data.get('download', 'N/A')} Mbps")
                self.network_upload_label.config(text=f"Upload Speed: {network_data.get('upload', 'N/A')} Mbps")
        except Exception as e:
            print(f"Error loading data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
