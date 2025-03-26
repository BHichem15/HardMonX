import subprocess
import os

# تحديد المسارات الكاملة للـ Backend و Frontend
backend_path = os.path.join("backend", "app.py")
frontend_path = os.path.join("frontend", "ui.py")

try:
    # تشغيل الـ Backend
    with subprocess.Popen(["python", backend_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE) as backend_process:
        try:
            # تشغيل الـ Frontend
            subprocess.run(["python", frontend_path], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Frontend Error: {e}")
        finally:
            # التأكد من إنهاء backend عند إغلاق الواجهة
            backend_process.terminate()
            backend_process.wait()  # التأكد من إنهاء العملية بالكامل

except FileNotFoundError:
    print("Error: تأكد من صحة مسارات الملفات.")
except Exception as e:
    print(f"Unexpected Error: {e}")
