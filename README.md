<h1>📌 HardMonX 0.1.0 Documentation</h1>
<p>This documentation provides a comprehensive guide on how to install, run, and use HardMonX. It also includes a breakdown of the file structure, features, and future improvements. HardMonX is a real-time system monitoring tool created as a final project for <strong>CS50x: Introduction to Computer Science</strong> by <strong>David J. Malan</strong>. This project was developed by <strong>Bourenane Chàabane</strong>.</p>

<h2>🎥 Presentation Video</h2>
<p>Watch the full project demonstration here:</p>
<p><a href="https://youtu.be/9TUZCqUVokM">CS50x final project presentation - HardMonX</a></p>

<h2>📖 1. Project Overview</h2>
<p>HardMonX is a real-time system performance monitoring tool that provides users with detailed insights into their computer's health and resource usage. It collects and displays:</p>
<ul>
    <li>🔹 <strong>CPU Usage & Temperature</strong> - Tracks processor performance in real-time.</li>
    <li>🔹 <strong>Memory Usage</strong> - Displays RAM consumption and available memory.</li>
    <li>🔹 <strong>Disk Usage</strong> - Monitors free and used disk space.</li>
    <li>🔹 <strong>Network Speed</strong> - Tests and tracks internet speed.</li>
</ul>
<p>The backend is built using Python, leveraging various system-monitoring libraries. A JSON file acts as a mini-database to store performance history.</p>
<p>The frontend is designed using <strong>Tkinter</strong> to provide a simple and interactive graphical user interface.</p>

<h2>⚙️ 2. Requirements</h2>
<p>Before running the program, ensure you have the following:</p>
<ul>
    <li>✅ Python 3.x installed</li>
    <li>✅ Required Python libraries:</li>
    <ul>
        <li>- psutil (for system monitoring)</li>
        <li>- cpuinfo (for CPU details)</li>
        <li>- speedtest-cli (for internet speed testing)</li>
        <li>- fastAPI & uvicorn (for backend server)</li>
    </ul>
</ul>

<h2>📂 3. Project Structure</h2>
<pre>HardMonX 0.1.0/
│
├── backend/
│   ├── __init__.py
│   ├── app.py                # Backend server
│   ├── cpu_monitor.py        # CPU Monitoring Module
│   ├── memory_monitor.py     # Memory Monitoring Module
│   ├── disk_monitor.py       # Disk Monitoring Module
│   ├── network_monitor.py    # Network Monitoring Module
│   └── requirements.txt      # Required dependencies
│
├── frontend/
│   ├── __init__.py
│   ├── ui.py                 # GUI implementation
│   └── ui_styles.py          # UI styling and theming
│
├── main.py                   # Entry point to start the application
│
├── data.json                 # Performance history storage
│
├── .gitignore                # Files to exclude from Git
│
└── README.md                 # Project documentation</pre>

<h2>🚀 4. Running the Program</h2>
<h3>Step 1: Install Python (if not installed)</h3>
<h3>Step 2: Install the required libraries</h3>
<p>Open the terminal and run the following commands:</p>
<code><pre>cd HardMonX
cd backend</pre></code>
<p>Then, install dependencies:</p>
<code><pre>pip install -r requirements.txt</pre></code>
<h3>Step 3: Run the Program</h3>
<p>Navigate back to the main folder:</p>
<code><pre>cd ..</pre></code>
<p>Run the program:</p>
<code><pre>python main.py</pre></code>

<h2>🌟 5. Features</h2>
<ul>
    <li>✅ Real-time system performance monitoring</li>
    <li>✅ Displays CPU, Memory, Disk, and Network status</li>
    <li>✅ Automatic data updates every 3 seconds</li>
    <li>✅ Simple and user-friendly graphical interface</li>
    <li>✅ Works on Windows, Linux, and MacOS</li>
    <li>✅ Lightweight and resource-efficient</li>
</ul>

<h2>🛠 6. Future Enhancements</h2>
<p>Future improvements planned for HardMonX:</p>
<ul>
    <li>🔹 Enhanced GUI with better design</li>
    <li>🔹 Performance analysis and recommendations</li>
    <li>🔹 Email or notifications for high CPU/RAM usage</li>
    <li>🔹 Integration of an API for remote monitoring</li>
    <li>🔹 Database support for historical performance tracking</li>
    <li>🔹 GPU performance and temperature monitoring</li>
    <li>🔹 User authentication to monitor multiple devices</li>
</ul>

<h2>🖥 7. Converting to an Executable (EXE)</h2>
<p>If you want to use HardMonX as a standalone Windows application without needing Python, you can create an EXE file:</p>
<p>1. Install PyInstaller:</p>
<code><pre>pip install pyinstaller</pre></code>
<p>2. Convert Python script to EXE:</p>
<code><pre>pyinstaller --onefile --windowed main.py</pre></code>
<p>3. The EXE file will be available in the <strong>dist/</strong> folder.</p>

<h2>📞 8. Support & Contributions</h2>
<p>If you want to contribute to this project, suggest features, or report issues, feel free to open an Issue or Pull Request on GitHub.</p>
<p>Thank you for using HardMonX! 🚀</p>
