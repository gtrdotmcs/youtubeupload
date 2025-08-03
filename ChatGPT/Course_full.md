# 🧠 Generative AI Course — From Basics to Intermediate (Free & Open Source)

**Duration**: ~14 weeks (2 hours per weekend)  
**Total Time Commitment**: 28–30 hours  
**Goal**: Learn the foundations of Generative AI and build text, image, and chatbot apps using free tools like Hugging Face, OpenAI (free-tier), and Google Colab.

---

## 📌 Course Structure

| Month | Focus                              | Key Topics                                   |
|-------|-------------------------------------|----------------------------------------------|
| 1     | Foundations                         | AI vs ML, LLMs, Text Generation, Prompting   |
| 2     | Hands-on GenAI                      | Chatbots, Image Generation, Fine-tuning Intro|
| 3     | Build & Deploy                      | Streamlit, OpenAI API, Responsible AI        |
| 4     | Intermediate Concepts (Optional)    | Fine-tuning with LoRA, Mini Project           |

---

## 🗓️ WEEKLY PLAN

---

## 🧠 Week 1 – What is AI, ML, Deep Learning & Generative AI?
**Goal**: Understand key differences and try GenAI tools.

- 🧾 [IBM Intro to AI/ML](https://www.ibm.com/cloud/learn/machine-learning)
- 🎥 [YouTube – GenAI Explained](https://www.youtube.com/watch?v=7LkyouUAEAA)
- 🧪 Try: [ChatGPT](https://chat.openai.com), [DALL·E Mini](https://huggingface.co/spaces/dalle-mini/dalle-mini)
- ⚙️ Set up: [Google Colab](https://colab.research.google.com)

✅ Checklist:
- [ ] Read IBM article
- [ ] Watch YouTube video
- [ ] Try text and image generation
- [ ] Set up Google Colab

---

## 📖 Week 2 – Introduction to Large Language Models (LLMs)

- 📘 [Hugging Face NLP Course – Chapter 1](https://huggingface.co/learn/nlp-course/chapter1)
- Learn tokenization, transformers, embeddings (high-level)
- Tool: Try `pipeline("text-generation")` with GPT-2 in Colab

✅ Checklist:
- [ ] Read Hugging Face Chapter 1
- [ ] Try text-generation in Colab

---

## ✍️ Week 3 – Text Generation with GPT-2

- Use Hugging Face Transformers in Colab to:
  - Load GPT-2
  - Generate poems, summaries, jokes
- 📘 Code Example: [GPT-2 Text Generation Notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/examples/text_generation.ipynb)

✅ Checklist:
- [ ] Generate your own text
- [ ] Try 3 different styles (story, summary, Q&A)

---

## 🪄 Week 4 – Prompt Engineering Basics

- What is a prompt? How to improve output quality?
- Try:
  - Instruction prompts
  - Role-based prompts
  - Few-shot examples
- 📘 Resource: [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)

✅ Checklist:
- [ ] Create 3 custom prompts
- [ ] Write down prompt + output combos

---

## 💬 Week 5 – Build a Chatbot with Transformers (No Fine-Tuning)

- Use Hugging Face `pipeline("conversational")`
- Build a simple chatbot in Python
- Try turning your bot into a function

✅ Checklist:
- [ ] Build and test a chatbot
- [ ] Use it for a 5-turn conversation

---

## 🛠️ Week 6 – Fine-tuning Concepts

- What’s fine-tuning vs prompt tuning?
- Read: [Hugging Face Fine-tune GPT2](https://huggingface.co/blog/how-to-train)
- Try loading a custom dataset in Colab (small one)

✅ Checklist:
- [ ] Understand LoRA & fine-tuning
- [ ] Load toy dataset and tokenize it

---

## 🎨 Week 7 – Text-to-Image with Stable Diffusion

- Learn basics of diffusion models
- Tool: [Stable Diffusion Demo (Hugging Face)](https://huggingface.co/CompVis/stable-diffusion)
- Try prompts: fantasy, sci-fi, logo-style

✅ Checklist:
- [ ] Generate 3+ images with different prompts
- [ ] Compare results with prompt tuning

---

## 🖼️ Week 8 – Image Generation Projects

- Build a prompt template (e.g., "A logo of a ___ in the style of ___")
- Generate variations
- Bonus: Use [Craiyon](https://huggingface.co/spaces/dalle-mini/dalle-mini) for comparisons

✅ Checklist:
- [ ] Build a theme-based image set
- [ ] Try a style transfer via prompt (e.g., "in Pixar style")

---

## 🔌 Week 9 – Use OpenAI API (Free Tier)

- Sign up at [OpenAI Platform](https://platform.openai.com/)
- Read: [OpenAI API Docs](https://platform.openai.com/docs/)
- Use Python to call `gpt-3.5-turbo` from Colab

✅ Checklist:
- [ ] Register at OpenAI
- [ ] Call API from Colab
- [ ] Generate text programmatically

---

## 🖥️ Week 10 – Build GenAI Web App with Streamlit

- 📘 [Streamlit Docs](https://docs.streamlit.io/)
- Build app: user types a prompt, model generates text or image
- Deploy locally (or on Hugging Face Spaces later)

✅ Checklist:
- [ ] Install & run basic Streamlit app
- [ ] Build an app to generate text or image

---

## ⚖️ Week 11 – Responsible AI & Bias

- 📘 Read: [Practical AI Ethics Book (PDF)](https://link.springer.com/book/10.1007/978-3-030-21836-2)
- Explore risks:
  - Hallucinations
  - Harmful content
  - Deepfakes

✅ Checklist:
- [ ] Read 1–2 chapters of ethics book
- [ ] Write down 2 risks and 1 solution for each

---

## 🧪 Week 12 – Mini Project #1

Choose one:
- 🧠 Build a prompt-based assistant
- 🎨 Text-to-image art generator
- 🧾 AI text summarizer or email writer

✅ Checklist:
- [ ] Define project goal
- [ ] Build it in Colab or Streamlit
- [ ] Test with real inputs

---

## 📈 Week 13 – Intermediate: Fine-tuning with LoRA

- Use [PEFT + LoRA](https://github.com/huggingface/peft)
- Try fine-tuning a small model (like distilgpt2)
- Use free Google Colab GPU (T4)

✅ Checklist:
- [ ] Load PEFT
- [ ] Fine-tune on custom text
- [ ] Generate before & after samples

---

## 🎓 Week 14 – Final Mini Project + Demo

- Combine all skills into an end-to-end app
- Suggested: Hugging Face Spaces or Streamlit UI
- Optional: Publish on GitHub

✅ Checklist:
- [ ] Finish a real-world use-case app
- [ ] Share your app or notebook
- [ ] Reflect: What did you learn? What’s next?
 
---

## 📚 Free Resource Summary

| Topic                 | Link                                                                 |
|----------------------|----------------------------------------------------------------------|
| Hugging Face Course  | https://huggingface.co/learn/nlp-course/chapter1                    |
| Google Colab         | https://colab.research.google.com                                   |
| OpenAI API Docs      | https://platform.openai.com/docs/                                   |
| Streamlit Docs       | https://docs.streamlit.io/                                           |
| DALL·E Mini          | https://huggingface.co/spaces/dalle-mini/dalle-mini                 |
| Stable Diffusion     | https://huggingface.co/CompVis/stable-diffusion                     |
| AI Ethics Book       | https://link.springer.com/book/10.1007/978-3-030-21836-2             |
| Awesome Prompts      | https://github.com/f/awesome-chatgpt-prompts                        |

---

## ✅ Progress Tracking Template (Optional)

You can copy this to a notebook or checklist app:

text

1. [ ] Week 1 - AI/ML/GenAI Concepts  
2. [ ] Week 2 - LLMs & Tokenization  
3. [ ] Week 3 - Text Generation  
4. [ ] Week 4 - Prompt Engineering  
5. [ ] Week 5 - Chatbot Pipeline  
6. [ ] Week 6 - Fine-tuning Basics  
7. [ ] Week 7 - Stable Diffusion Intro  
8. [ ] Week 8 - Image Generation Project  
9. [ ] Week 9 - OpenAI API Integration  
10. [ ] Week 10 - Streamlit App  
11. [ ] Week 11 - AI Ethics  
12. [ ] Week 12 - Mini Project 1  
13. [ ] Week 13 - LoRA Fine-tuning  
14. [ ] Week 14 - Final Project

[Link](https://chatgpt.com/s/t_688f6f656e608191bdfaed7bf057ca4e)