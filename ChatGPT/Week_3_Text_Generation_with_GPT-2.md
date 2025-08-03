# ✍️ Generative AI Course — Week 3  
**Topic**: Text Generation with GPT-2  
**Duration**: ~2 hours  
**Goal**: Learn to use GPT-2 to generate creative text like poems, stories, and summaries using Hugging Face Transformers in Google Colab.

---

## 🪜 PART 1 – Learn by Reading (~20–30 min)

### 📘 1.1 Understand How GPT-2 Generates Text

Quick primer:
- GPT-2 is an autoregressive model — it predicts the next word based on previous ones.
- You can adjust how much text it generates, how creative it is, and how random it should be.

📖 Read:
🔗 [Hugging Face: Text Generation with Transformers](https://huggingface.co/transformers/task_summary.html#text-generation)

---

## 🪜 PART 2 – Hands-On with Google Colab (~60–70 min)

### 🧪 2.1 Set Up GPT-2 in Google Colab

Open [Google Colab](https://colab.research.google.com) and run this to install:

`python !pip install transformers`

✅ Load GPT-2 Model and Generate Text

```
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

# Basic prompt
prompt = "The future of humanity lies"
result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])
```
---
🧪 2.2 Try Creative Prompts

Try these:

- “She opened the door and saw...”

- “In the year 2120, humans live on...”

- “The secret recipe for happiness is...”

```
result = generator(prompt, 
                   max_length=60, 
                   num_return_sequences=2, 
                   temperature=0.8, 
                   top_p=0.95, 
                   do_sample=True)
```

📘 Documentation:
🔗 [Text Generation Pipeline Options](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextGenerationPipeline)
---

🧪 2.3 Explore GPT-2 Variants (Optional)
Try a smaller or larger model:

- "gpt2-medium"

- "distilgpt2" (lighter, faster)
---

Update the model like this:
```
generator = pipeline("text-generation", model="distilgpt2")
```
---

✅ Wrap-Up: Self Review

🧠 Try answering:

- What are temperature, top_p, and do_sample used for?

- How does changing max_length affect the output?

- What surprised you about the model’s creativity or logic?

---

### Track

- 📋 Week 3 Progress Checklist
    - [ ] Read Hugging Face’s text generation summary    
    - [ ] Installed Transformers and ran GPT-2 in Colab    
	- [ ] Generated text from 2–3 different prompts  
	- [ ] Experimented with `temperature`, `top_p`, or different model sizes  
	- [ ] Answered 3 self-review questions         
	
---

Coming Next:

Week 4 — Prompt Engineering Basics

In Week 4, you’ll:

- Learn how to write better prompts for more accurate or creative results

- Understand few-shot prompting and role-based prompts

- Start building your own prompt library for different use-cases (e.g., summarizing, writing emails, storytelling)