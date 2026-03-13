import json
import os

def test_jsonl_structure():
    file_path = "data_ready.jsonl"
    if not os.path.exists(file_path):
        print("[-] ملف البيانات غير موجود!")
        return
    
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            try:
                data = json.loads(line)
                if "id" not in data:
                    print(f"[-] خطأ في السطر {i}: مفتاح 'id' مفقود")
                    return
            except json.JSONDecodeError:
                print(f"[-] خطأ في صيغة JSON في السطر {i}")
                return
    print("[+] تم فحص سلامة البيانات بنجاح: الهيكلية سليمة.")

if __name__ == "__main__":
    test_jsonl_structure()
