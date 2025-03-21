<h1>📌HardMonX 1.0.0 Documentation</h1>
<p>This documentation provides an in-depth guide on how to install, run, and use this program, as well as a breakdown of the file structure, features, and future improvements. This is a program was created as a final project for <strong>CS50x: introduction to computer science</strong> by <strong>David J. Malan</strong>. This program was made by <strong>Bourenane Chàabane</strong>.</p>

<h2>📖 1. Project Overview</h2>
<p>This project is a real-time computer performance monitoring tool that collects data about CPU usage and temperature, memory consumption, disk usage and Network speed using Python.</p>
<p>🔹 The backend is built using Some python libraries and a .json file as a mini-database for storing history of performance.</p>
<p>🔹 The frontend is a Graphical user interface using Tkinter.</p>

<h2>⚙️ 2. Requirements</h2>
<p>Before running the project, ensure you have the following installed:</p>
<p>✅ Python 3.x</p>
<p>✅ Required Python libraries:</p>
<p>    - psutil</p>
<p>    - cpuinfo</p>

<h2>📂 3. Project Structure</h2>
<pre>HardMonX 1.0.0/
│
├── backend/
│   ├── __init__.py
│   ├── app.py              
│   ├── cpu_monitor.py        
│   ├── memory_monitor.py      
│   ├── disk_monitor.py        
│   ├── network_monitor.py    
│   ├── data.json         
│   └── requirements.txt       
│
├── frontend/
│   ├── __init__.py
│   ├── ui.py                   
│   └── ui_styles.py            
│
├── main.py                                  
│
├── .gitignore                  
│
└── README.md </pre>                  

<h2>🚀 4. Running the Program</h2>
<h3>I. Install latest version of python</h3>
<h3>II. install the required libraries using <strong>requirements.txt</strong></h3>
<p>-In the terminal write : </p>
<code><pre>cd HardMonX
cd backend</pre></code>
<p>-In the terminal write : </p>
<code><pre>pip install requirements.txt</pre></code>
<h3>III. run the program :</h3>
<p>- go to the main folder by writing :</p>
<code><pre>cd ..</pre></code>
<p>In the terminal write :</p>
<code><pre>python main.py</pre></code>

<h2>🌟 6. Features</h2>
<p>✅ Real-time system performance tracking</p>
<p>✅ Windows and MacOS support</p>
<p>✅ Beginner Friendly and easy reding</p>

<h2>🛠 7. Future Enhancements</h2>
<p>To make this project more advanced, We will add :</p>
<p>🔹 Better GUI (Graphical user interface)</p>
<p>🔹 analyzing the performance and giving advice</p>
<p>🔹 Email or Notifications alerts when CPU or RAM usage is too high</p>
<p>🔹 Adding an API</p>
<p>🔹 A database to store historical performance data and specs of CPUs and GPUs</p>
<p>🔹 Adding GPU performance and temperature</p>
<p>🔹 User authentication for monitoring multiple devices</p>

<h2>🖥 9. Converting the Project to an Executable (EXE)</h2>
<p>If you want to run this project as a standalone Windows application without installing Python, you can convert it to an EXE file:</p>
<p>1. Install PyInstaller: </p>
<code><pre>    - pip install pyinstaller</pre></code>
<p>2. Convert Python script to EXE: </p>
<code><pre>    - pyinstaller --onefile --windowed app.py</pre></code>
<p>3. The EXE file will be available in the <strong>dist/</strong> folder.</p>

<h2>📞 10. Support & Contributions</h2>
<p>If you want to improve this project or report an issue, you can open an Issue or a Pull Request on GitHub.</p>

