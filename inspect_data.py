import csv
import os

# البحث عن أي ملف CSV في مجلد المنزل والمجلدات الفرعية
def find_csv():
    for root, dirs, files in os.walk("/data/data/com.termux/files/home"):
        for file in files:
            if file.endswith(".csv"):
                return os.path.join(root, file)
    return None

file_path = find_csv()

if not file_path:
    print("[-] لم يتم العثور على أي ملف CSV في مجلد الـ home.")
    print("[-] جرب تشغيل أمر 'find / -name *.csv' لمعرفة مكان الملف.")
else:
    print(f"[+] تم العثور على ملف: {file_path}")
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader)
            print("\n--- قائمة الأعمدة المكتشفة ---")
            print(headers)
    except Exception as e:
        print(f"[-] خطأ أثناء فتح الملف: {e}")
