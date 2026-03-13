import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

# إعداد نظام التسجيل (Logging)
logging.basicConfig(filename='pipeline_activity.log', level=logging.INFO, 
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

class DataHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if "data_ready.jsonl" in event.src_path:
            msg = "[!] تم اكتشاف تعديل في ملف البيانات، جاري فحص الجودة..."
            print(msg)
            logging.info(msg)
            
            # تشغيل الفحص التلقائي
            result = subprocess.run(['python', 'test_data.py'], capture_output=True, text=True)
            
            if result.returncode == 0:
                success_msg = "[+] فحص الجودة ناجح."
                print(success_msg)
                logging.info(success_msg)
            else:
                error_msg = f"[!] فشل الفحص: {result.stderr}"
                print(error_msg)
                logging.error(error_msg)

def start_watchdog():
    observer = Observer()
    event_handler = DataHandler()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    logging.info("[+] الحارس (Watchdog) يعمل الآن...")
    print("[+] الحارس (Watchdog) يعمل الآن... يراقب البيانات!")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_watchdog()
