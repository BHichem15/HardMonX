import tkinter as tk
from tkinter import ttk
import threading
import time
import ui_styles as style
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from backend.cpu_monitor import get_cpu_data
from backend.memory_monitor import get_memory_data
from backend.disk_monitor import get_disk_data
from backend.network_monitor import get_network_data


class SystemMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HardMonX")
        self.root.geometry("480x775")
        self.root.resizable(False, False)
        self.root.configure(bg=style.COLOR_BACKGROUND)

        # user interface setup
        self.setup_ui()

        # auto refresh
        self.start_auto_refresh()

    def setup_ui(self):
        # Title
        title_label = tk.Label(self.root, text="HardMonX", **style.title_style)
        title_label.pack(pady=10)

        # Refresh button
        self.refresh_button = tk.Button(self.root, text="Refresh Data", command=self.refresh_data, **style.button_style)
        self.refresh_button.pack(pady=10)

        # Data frames setup
        self.create_info_frames()

    def create_info_frames(self):
        # Creating sections for each type of data
        self.sections = {
            "CPU": ["name", "cores", "usage", "frequency", "temperature"],
            "Memory": ["percent", "total", "free"],
            "Disk": ["percentage", "total_size", "used_size", "free_size", "read_speed", "write_speed"],
            "Network": ["download", "upload"]
        }

        self.data_labels = {}

        for section, fields in self.sections.items():
            frame = tk.LabelFrame(self.root, text=f"{section} Information", **style.label_style)
            frame.pack(fill=tk.X, padx=10, pady=5)
            self.data_labels[section] = {}
            for field in fields:
                label = tk.Label(frame, text=f"{field.replace('_', ' ').title()}: Loading...", **style.data_style)
                label.pack(anchor="w", padx=10, pady=5)
                self.data_labels[section][field] = label

    def refresh_data(self):
        # Manual refresh
        self.update_ui()

    def start_auto_refresh(self):
        # Auto refresh in a separate thread
        self.auto_refresh_thread = threading.Thread(target=self.auto_refresh, daemon=True)
        self.auto_refresh_thread.start()

    def auto_refresh(self):
        # Auto refresh function
        while True:
            self.update_ui()
            time.sleep(3)

    def update_ui(self):
        # Fetching updated data from backend
        data_sources = {
            "CPU": get_cpu_data(),
            "Memory": get_memory_data(),
            "Disk": get_disk_data(),
            "Network": get_network_data()
        }

        # Updating UI with the new data
        for section, fields in self.sections.items():
            for field in fields:
                value = data_sources[section].get(field, "N/A")
                unit = "MHz" if field == "frequency" else "%" if field == "percent" else "GB" if "size" in field else "Mbps" if field in ["download", "upload"] else ""
                self.data_labels[section][field].config(text=f"{field.replace('_', ' ').title()}: {value} {unit}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SystemMonitorApp(root)
    root.mainloop()
