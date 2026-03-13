import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DataHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("data_ready.jsonl"):
            print(f"[!] تنبيه: تم تعديل ملف البيانات. جاري إعادة فحص الجودة...")
            # هنا يمكنك ربط الـ orchestrator الخاص بك للتشغيل التلقائي
            import subprocess
            subprocess.run(['python', 'test_data.py'])

def start_watchdog():
    observer = Observer()
    event_handler = DataHandler()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    print("[+] الحارس (Watchdog) يعمل الآن... يراقب البيانات!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watchdog()
