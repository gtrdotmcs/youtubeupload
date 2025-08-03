
# 🧠 Generative AI Course — Week 4  
**Topic**: Prompt Engineering Basics  
**Duration**: ~2 hours  
**Goal**: Learn how to craft effective prompts for language models and experiment with prompt types like zero-shot, few-shot, and role-based prompting.

---

## 🪜 PART 1 – Core Concepts of Prompt Engineering (30 min)

### 📘 1.1 What is Prompt Engineering?  
Prompt engineering is the skill of designing input text to guide a language model to generate the most accurate or creative output.

📚 **Free/Open Resources**:
- 🔗 [Prompt Engineering Guide by DAIR.AI](https://github.com/dair-ai/Prompt-Engineering-Guide)
- 🔗 [OpenAI’s Prompting Examples](https://platform.openai.com/examples)
- 🔗 [LangChain Prompt Templates (Optional)](https://docs.langchain.com/docs/components/prompts/)

### 📌 Types of Prompts to Learn:
- **Zero-shot** prompting  
- **Few-shot** prompting  
- **Instructional** prompting  
- **Role-based** prompting (e.g., “You are a helpful assistant…”)

---

## 🪜 PART 2 – Practice in Google Colab (60–70 min)

### 🧪 2.1 Try Zero-shot and Instructional Prompting

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "Summarize the following text: The Earth revolves around the sun..."
output = generator(prompt, max_length=60, do_sample=True)
print(output[0]['generated_text'])
```

Try instructional prompts:
- “Explain black holes to a 10-year-old.”  
- “Write a polite email declining an invitation.”

---

### 🧪 2.2 Try Few-shot Prompting

```python
prompt = '''
Translate English to French:
English: Hello, how are you?
French: Bonjour, comment ça va?

English: I love reading books.
French:
'''
result = generator(prompt, max_length=100, do_sample=True)
print(result[0]['generated_text'])
```

Try your own few-shot tasks like:
- Grammar correction
- Email writing
- Dialogue generation

---

### 🧪 2.3 Try Role-Based Prompting (Optional but fun)

```python
prompt = "You are a wise historian. Explain the fall of the Roman Empire in simple words."
output = generator(prompt, max_length=100, do_sample=True)
print(output[0]['generated_text'])
```

---

## ✅ Week 4 Progress Checklist

| Task                                                                 | Done? ✅ |
|----------------------------------------------------------------------|----------|
| Read about prompt engineering from DAIR.AI guide                     |          |
| Tried zero-shot prompting with GPT-2                                 |          |
| Tried instructional prompts                                          |          |
| Practiced few-shot prompting with examples                           |          |
| Tried at least one role-based prompt                                 |          |
| Reflected on what made a prompt work well or not                     |          |

---

## 📌 Coming Next: Week 5 — Fine-Tuning a Small Language Model

You’ll learn:
- The difference between fine-tuning and prompting
- How to fine-tune a mini model on your own text using Colab
