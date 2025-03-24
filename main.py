import subprocess

# تشغيل الـ Backend
backend_process = subprocess.Popen(["python", "backend/app.py"])

# تشغيل الـ Frontend
try:
    subprocess.run(["python", "frontend/ui.py"])
finally:
    # التأكد من إنهاء backend عند إغلاق الواجهة
    backend_process.terminate()
