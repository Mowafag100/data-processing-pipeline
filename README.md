# Data Processing Pipeline

مجموعة من سكربتات بايثون مصممة لمعالجة وتحويل مجموعات البيانات الضخمة (Large Datasets) من صيغة CSV إلى صيغة JSONL، مما يجعلها جاهزة لعمليات التدريب (Fine-tuning) لنماذج الذكاء الاصطناعي.

## المميزات:
- **تحليل تلقائي:** سكربت للكشف عن هيكلية ملفات CSV.
- **تحويل فعال:** محول بيانات (Serializer) للتعامل مع آلاف السجلات.
- **التوافق:** المخرجات متوافقة مع المعايي
يدعم النظام خاصية التسجيل التلقائي (Logging) في ملف pipeline_activity.log لضمان قابلية التتبع.
## المهارات المستخدمة:
- Python (Standard Library)
- Data Engineering & Pipeline Design
- JSONL Serialization
- Version Control (Git/GitHub)

## كيفية التشغيل:
1. تأكد من وجود ملف البيانات بصيغة .csv في المجلد.
2. يمكنك تشغيل كامل نظام الأتمتة عبر الأمر: `python pipeline_orchestrator.py`

