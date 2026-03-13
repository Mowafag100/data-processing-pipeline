from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments, Trainer
from datasets import load_dataset

# إعداد النموذج
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# تحميل البيانات المعالجة
dataset = load_dataset("json", data_files="data_ready.jsonl")

# إعدادات التدريب المتقدمة
training_args = TrainingArguments(
    output_dir="./results",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    save_steps=100,
    logging_steps=50,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset['train'],
)

# تنفيذ التدريب
if __name__ == "__main__":
    trainer.train()
