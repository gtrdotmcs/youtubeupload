
# 🔧 Generative AI Course — Week 5  
**Topic**: Fine-Tuning a Language Model (NLP)  
**Duration**: ~2 hours  
**Goal**: Learn how and when to fine-tune a language model using open-source tools.

---

## 📘 PART 1 – Fine-Tuning Basics (30–40 min)

### 🤔 Why Fine-Tune?
- Improve performance for domain-specific tasks
- Embed brand tone or persona
- Extend or adapt LLMs for specific vocab or use cases

### 🔍 Key Concepts
- Pre-training vs Fine-tuning vs Prompt-tuning
- Overfitting and underfitting in fine-tuned models
- Datasets and evaluation metrics

📚 **Open-Source Learning Resources**:
- 🔗 [Hugging Face Course - Chapter: Fine-Tuning Transformers](https://huggingface.co/course/chapter3/3)
- 🔗 [Google Colab: Fine-tune DistilBERT on IMDB dataset](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_classification.ipynb)
- 🔗 [SimpleTransformers Fine-Tuning Examples](https://simpletransformers.ai/docs/fine_tuning/)
- 🔗 [Understanding Transfer Learning in NLP](https://rpradeepmenon.medium.com/understanding-transfer-learning-in-nlp-1a0553ed59ab) *(blog)*

---

## 🧪 PART 2 – Hands-on with Hugging Face Transformers (60–75 min)

### 🔧 Tools Required
- Google Colab (Free GPU)
- `transformers`, `datasets`, `accelerate`, `evaluate` (install via pip)

### 🧰 What You'll Build:
- Fine-tune a small BERT or DistilBERT model on a sentiment analysis dataset (IMDb or SST2)
- Evaluate accuracy and predictions

### ▶️ Tutorial Steps (via Colab)
1. Load IMDb dataset using `datasets`
2. Load a pretrained DistilBERT model
3. Tokenize the dataset
4. Fine-tune for 2–3 epochs
5. Evaluate predictions

📦 Optional GitHub Projects:
- 🔗 [text-classification on IMDb — Hugging Face Example](https://github.com/huggingface/notebooks/blob/main/examples/text_classification.ipynb)

---

## ✅ Week 5 Progress Checklist

| Task                                                                  | Done? ✅ |
|-----------------------------------------------------------------------|----------|
| Read about fine-tuning vs prompt-tuning                              |          |
| Explored Hugging Face course on fine-tuning                          |          |
| Ran the IMDb dataset fine-tuning notebook on Colab                   |          |
| Understood model evaluation and overfitting                          |          |
| Tuned a model and tested predictions                                 |          |
| Saved/Exported your fine-tuned model                                 |          |

---

## 📌 Coming Next: Week 6 — Text-to-Image Generation

You’ll learn:
- How models like DALL·E, Stable Diffusion generate images
- Generate images from prompts using Hugging Face, Colab, or Replicate API
