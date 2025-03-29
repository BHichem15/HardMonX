import subprocess
<<<<<<< HEAD

# تشغيل الـ Backend
backend_process = subprocess.Popen(["python", "backend/app.py"])

# تشغيل الـ Frontend
try:
    subprocess.run(["python", "frontend/ui.py"])
finally:
    # التأكد من إنهاء backend عند إغلاق الواجهة
    backend_process.terminate()
=======
import time
import sys

def start_backend():
    # Start the backend FastAPI server
    return subprocess.Popen([sys.executable, "backend/app.py"])

def start_frontend():
    # Start the frontend Tkinter application
    return subprocess.Popen([sys.executable, "frontend/ui.py"])

if __name__ == "__main__":
    print("Starting backend server...")
    backend_process = start_backend()
    # Delay to ensure the backend starts before the frontend
    time.sleep(3)  
    print("Starting frontend application...")
    frontend_process = start_frontend()
    
    try:
        # Keep running until the UI is closed
        frontend_process.wait() 
    except KeyboardInterrupt:
        print("Shutting down...")
    # Shutting the program
    finally:
        print("Terminating backend server...")
        backend_process.terminate()
        backend_process.wait()

>>>>>>> str
