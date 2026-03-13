import json

input_file = "data_ready.jsonl"
output_report = "analysis_report.json"

def analyze():
    success_count = 0
    total_len = 0

    with open(input_file, 'r') as f:
        for line in f:
            record = json.loads(line)
            if record.get("status") == "200":
                success_count += 1
                total_len += int(record.get("len_or_error", 0))

    report = {
        "total_successful_requests": success_count,
        "average_length": total_len / success_count if success_count > 0 else 0,
        "status": "Finalized by Data-Pipeline-Bot"
    }

    with open(output_report, 'w') as f:
        json.dump(report, f, indent=4)
    print(f"[+] تم تحليل البيانات بنجاح! التقرير موجود في: {output_report}")

if __name__ == "__main__":
    analyze()
