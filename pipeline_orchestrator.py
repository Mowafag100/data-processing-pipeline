import subprocess
import os

def run_step(script_name):
    print(f"\n--- جاري تنفيذ: {script_name} ---")
    result = subprocess.run(['python', script_name], capture_output=True, text=True)
    if result.returncode == 0:
        print(result.stdout)
    else:
        print(f"حدث خطأ في {script_name}: {result.stderr}")
        exit(1)

def run_pipeline():
    # ترتيب العمليات: الاختبار -> التحويل -> التحليل
    steps = ['test_data.py', 'convert_to_jsonl.py', 'analyze_data.py']
    
    for step in steps:
        run_step(step)
    
    print("\n[SUCCESS] تم تشغيل كامل الأتمتة بنجاح!")

if __name__ == "__main__":
    run_pipeline()
