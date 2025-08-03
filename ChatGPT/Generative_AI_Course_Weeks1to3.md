
# 🎓 Generative AI Course — Week 1
**Topic**: Introduction to AI & Generative AI  
**Duration**: ~2 hours  
**Goal**: Build foundational understanding of AI, ML, and what makes generative AI unique.

---

## 🧠 PART 1 – Understanding AI, ML, and DL (30–40 min)

### 📘 Learn the Concepts

#### What is AI?
- Any machine that mimics human intelligence (e.g., rule-based systems).

#### What is ML?
- Algorithms that learn from data instead of being explicitly programmed.

#### What is Deep Learning?
- Subset of ML using neural networks with many layers.

📚 **Free Resources**:
- [Elements of AI (First 2 chapters)](https://www.elementsofai.com/)
- [YouTube: AI vs ML vs DL by Simplilearn](https://www.youtube.com/watch?v=IoZGSQ07e8g)

---

## 🎨 PART 2 – What is Generative AI? (30–40 min)

### 📘 Learn the Concepts

#### What is Generative AI?
- Models that **generate** content: text, images, code, music, etc.

#### Common Examples
- Text: ChatGPT, Claude, LLaMA
- Images: DALL·E, Stable Diffusion
- Audio: Jukebox
- Video: Sora (OpenAI)

📚 **Free Resources**:
- [YouTube: What is Generative AI? by Google](https://www.youtube.com/watch?v=SFJm4BQKnEo)
- [Google AI Glossary](https://ai.google/discover/glossary/)
- [Blog: A Beginner’s Guide to Generative AI](https://www.analyticsvidhya.com/blog/2023/05/a-beginners-guide-to-generative-ai/)

---

## 🧪 PART 3 – Try a Live Demo (20–30 min)

### 🔬 Try ChatGPT or Gemini

No setup needed, just open:
- [ChatGPT Free](https://chat.openai.com/)
- [Gemini by Google](https://gemini.google.com/app)

Try:
- "Write a short poem about the monsoon."
- "Give me a packing list for a weekend trip."
- "What is generative AI in simple words?"

---

## ✅ Week 1 Progress Checklist

| Task                                                          | Done? ✅ |
|---------------------------------------------------------------|----------|
| Watched AI vs ML vs DL video                                  |          |
| Read first 2 chapters of Elements of AI                       |          |
| Watched Google’s Generative AI intro video                    |          |
| Tried at least 2 prompts in ChatGPT or Gemini                 |          |
| Can explain the difference between AI, ML, DL, and Generative AI |       |

---
## 📌 Coming Next: Week 2 — Dive into Language Models (LLMs)
You'll explore:
- What is a language model (LM)?
- What makes a large language model (LLM)?
- How models like GPT-2 and GPT-3 are trained.



# 🤖 Generative AI Course — Week 2  
**Topic**: Understanding Language Models & LLMs  
**Duration**: ~2 hours  
**Goal**: Learn how large language models work, what tokens are, and how these models learn to generate language.

---

## 🧠 PART 1 – What is a Language Model? (30–40 min)

### 📘 Learn the Concepts

- A **language model (LM)** predicts the next word in a sequence.
- LLMs like GPT-2, GPT-3, LLaMA are trained on billions of words (tokens).
- Training involves unsupervised learning on large text datasets.

📚 **Free Resources**:
- [The Illustrated GPT-2 – by Jay Alammar](https://jalammar.github.io/illustrated-gpt2/)
- [What are LLMs? – AssemblyAI Blog](https://www.assemblyai.com/blog/large-language-models/)
- [Short Video: How GPT Works (2 min)](https://www.youtube.com/watch?v=Te5rOTcEalU)

---

## 💡 PART 2 – What Are Tokens and Why Do They Matter? (15–20 min)

### 📘 Learn the Concepts

- Models don’t “see” words — they process **tokens** (chunks of text).
- Common tokenizers: Byte-Pair Encoding (BPE), WordPiece, SentencePiece.

Try tokenizing a sentence:

🔗 [OpenAI Tokenizer Tool (Free)](https://platform.openai.com/tokenizer)

Example:
```
Input: "I love learning generative AI."
→ Tokens: ['I', ' love', ' learning', ' gener', 'ative', ' AI', '.']
```

---

## 🧪 PART 3 – Watch & Explore Model Internals (30–40 min)

### 🧠 Understanding Attention & Transformers

📚 **Resources**:
- [The Illustrated Transformer – by Jay Alammar](https://jalammar.github.io/illustrated-transformer/)
- [How Attention Mechanism Works (Video)](https://www.youtube.com/watch?v=U0s0f995w14)

---

## ✅ Week 2 Progress Checklist

| Task                                                       | Done? ✅ |
|------------------------------------------------------------|----------|
| Read "Illustrated GPT-2"                                   |          |
| Understood what tokens are using tokenizer tool            |          |
| Watched the 2-minute GPT explanation video                 |          |
| Explored the "Illustrated Transformer" visualization       |          |
| Can explain what LLMs are in your own words                |          |

---
## 📌 Coming Next: Week 3 — Text Generation with GPT-2  
You'll start writing code using the Hugging Face `transformers` library and generate creative text!



# ✍️ Generative AI Course — Week 3  
**Topic**: Text Generation with GPT-2  
**Duration**: ~2 hours  
**Goal**: Use Hugging Face Transformers to generate creative text using GPT-2 and learn how to experiment with model parameters.

---

## 🪜 PART 1 – Learn the Concepts (20–30 min)

### 📘 1.1 What is GPT-2 and How Does It Work?

GPT-2 is an **autoregressive language model** — it generates text word by word, predicting the next word based on previous ones.

📚 **Free Resources**:
- 🔗 [Text Generation Task Summary – Hugging Face](https://huggingface.co/transformers/task_summary.html#text-generation)
- 🔗 [Hugging Face Model Card for GPT-2](https://huggingface.co/gpt2)
- 🔗 [Hugging Face Transformers GitHub](https://github.com/huggingface/transformers)

**Concepts to focus on:**
- Autoregressive generation
- Token-by-token prediction
- Prompt sensitivity
- Common parameters: `temperature`, `top_p`, `max_length`, `do_sample`

---

## 🪜 PART 2 – Hands-On with Google Colab (60–70 min)

### 🧪 2.1 Set Up GPT-2 in Colab

🔗 Open: [Google Colab](https://colab.research.google.com)

Install the library (first-time only):

```python
!pip install transformers
```

Then load GPT-2 and generate basic text:

```python
from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
prompt = "The future of artificial intelligence is"
result = generator(prompt, max_length=50, num_return_sequences=1)

print(result[0]['generated_text'])
```

---

### 🧪 2.2 Try Creative Prompts & Tweak Parameters

Experiment with prompts like:
- “Once upon a time, a robot decided to…”
- “In the year 3000, Earth was ruled by…”
- “The recipe for happiness is…”

Try this advanced version:

```python
result = generator(
    prompt,
    max_length=80,
    num_return_sequences=2,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)
for i, output in enumerate(result):
    print(f"\nResult {i+1}:\n", output["generated_text"])
```

📚 **Docs to help**:  
🔗 [Text Generation Pipeline Reference](https://huggingface.co/docs/transformers/main_classes/pipelines#transformers.TextGenerationPipeline)

---

### 🧪 2.3 Try Other GPT-2 Variants (Optional)

You can test smaller/faster or larger models:
- `"distilgpt2"` – faster, lighter
- `"gpt2-medium"` – more powerful

Update the pipeline like this:

```python
generator = pipeline("text-generation", model="distilgpt2")
```

📚 Hugging Face Model Hub:  
🔗 [https://huggingface.co/models](https://huggingface.co/models)

---

## ✅ Self Review Questions

1. What happens when you change `temperature` or `top_p`?
2. What’s the effect of a vague vs. clear prompt?
3. What model surprised you the most in its output?

---

## 📋 Week 3 Progress Checklist

| Task                                                                 | Done? ✅ |
|----------------------------------------------------------------------|----------|
| Read the Hugging Face summary on text generation                     |          |
| Installed `transformers` library in Google Colab                     |          |
| Ran GPT-2 to generate basic text using a prompt                      |          |
| Tried 2+ creative prompts and modified parameters (`max_length`, etc) |          |
| Tested another variant (e.g., `distilgpt2` or `gpt2-medium`)         |          |
| Answered 3 self-review questions                                     |          |

---

## 📌 Coming Next: Week 4 — Prompt Engineering Basics

In Week 4, you’ll:
- Learn how to write better prompts for more accurate or creative results
- Understand **few-shot prompting** and **role-based prompts**
- Start building your own **prompt library** for different use-cases (e.g., summarizing, writing emails, storytelling)
