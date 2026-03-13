import csv
import json

# المسار الذي تم اكتشافه للملف
input_file = "/data/data/com.termux/files/home/lawid_scan.csv"
output_file = "data_ready.jsonl"

def convert():
    count = 0
    with open(input_file, mode='r', encoding='utf-8') as f_csv:
        reader = csv.DictReader(f_csv)
        with open(output_file, mode='w', encoding='utf-8') as f_json:
            for row in reader:
                json.dump(row, f_json)
                f_json.write('\n')
                count += 1
    print(f"[+] تم تحويل {count} سجل بنجاح إلى ملف: {output_file}")

if __name__ == "__main__":
    convert()
