<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Phase 3: Generative Models – Detailed Breakdown (with Open Source \& Free References)

Phase 3 is all about building, using, and understanding the generative models at the heart of modern AI: large language models, GANs, VAEs, and prompt engineering. You’ll get both theory and practical exposure, using accessible online tools and datasets.

### **Week 9: Large Language Models (LLMs)**

**Objectives:**

- Understand what LLMs are and how they’re trained.
- Learn about architectures (e.g., GPT, BERT, T5).
- Use pre-trained LLMs for text generation or Q\&A.

**Study Plan:**

- **Theory (45min):**
    - What are LLMs? How do they work?
    - Transfer learning, fine-tuning, limitations, and ethical concerns.
    - Famous models: GPT-2/3, BERT, T5.
- **Hands-on (45min):**
    - Use Hugging Face Transformers to generate text with GPT-2.
    - Try a Hugging Face Space for question-answering or summarization.
- **Exercise (30min):**
    - Experiment: Tweak prompts, analyze outputs.
    - Reflect: What are benefits and risks of LLMs in society?

**References:**

- [Hugging Face Transformers Course (chapters on LLMs)](https://huggingface.co/learn/nlp-course/chapter7/7?fw=pt)
- [Hugging Face Inference Space – Try LLMs](https://huggingface.co/spaces)
- [Google BERT Demo \& Docs](https://github.com/google-research/bert)
- [The Illustrated GPT-2 by Jay Alammar](https://jalammar.github.io/illustrated-gpt2/)


### **Week 10: Generative Adversarial Networks (GANs)**

**Objectives:**

- Understand the concept of “adversarial” training.
- Explore generator vs. discriminator roles.
- Learn about GAN applications: image, audio, data creation.

**Study Plan:**

- **Theory (40min):**
    - What are GANs? How do they train?
    - Types: Vanilla, DCGAN, conditional GANs.
    - Struggles: mode collapse, instability.
- **Hands-on (50min):**
    - Run a basic GAN code (Keras / PyTorch, Google Colab).
    - Generate MNIST digits or simple images.
- **Exercise (30min):**
    - Try: Change random seeds/parameters in the code and see the effect.
    - Write a note: “How might GANs be misused?”

**References:**

- [GANs Tutorial (TensorFlow, Recommended)](https://www.tensorflow.org/tutorials/generative/dcgan)
- [PyTorch GANs Tutorials](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)
- [The Illustrated GAN (Jay Alammar)](https://jalammar.github.io/illustrated-gan/)
- [Kaggle Deep Learning: GANs Micro-Course](https://www.kaggle.com/learn/generative-adversarial-networks)


### **Week 11: Variational Autoencoders (VAEs)**

**Objectives:**

- Discover autoencoders: encoder–decoder structure, loss functions.
- Learn the intuition and math behind *variational* autoencoders.
- Visualization and practical applications (e.g., denoising, latent space).

**Study Plan:**

- **Theory (35min):**
    - What is an autoencoder? What’s special about VAEs?
    - Latent space, sampling, KL-divergence.
- **Hands-on (55min):**
    - Build a simple autoencoder using Keras, PyTorch, or TensorFlow.
    - (Colab/Notebook) Visualize encoded/decoded images, or try interpolation in VAE latent space.
- **Exercise (30min):**
    - Quiz on VAE concepts.
    - Try reconstructing noisy images or generating new data.

**References:**

- [VAEs Explained (OpenAI blog)](https://openai.com/research/variational-autoencoders/)
- [TensorFlow VAE Tutorial](https://www.tensorflow.org/tutorials/generative/cvae)
- [Dive into Deep Learning – VAE Chapter](https://d2l.ai/chapter_generative-adversarial-networks/vae.html)
- [PyTorch VAE Tutorial (GitHub, free)](https://github.com/AntixK/PyTorch-VAE)


### **Week 12: Prompt Engineering \& ChatGPT/GPT Models**

**Objectives:**

- Learn the art/science of prompt engineering.
- Design, evaluate, and optimize prompts for LLMs.
- Experiment with open demos and reproducible playgrounds.

**Study Plan:**

- **Theory (40min):**
    - What is prompt engineering? Few-shot vs. zero-shot prompts.
    - Chain-of-thought prompting and prompt injection risks.
- **Hands-on (50min):**
    - Try prompt experiments in [Hugging Face Spaces](https://huggingface.co/spaces).
    - Use [OpenAI Playground Demo](https://platform.openai.com/examples) (free tier) or any LLM you have access to.
- **Exercise (30min):**
    - Record and analyze how prompt tweaks change outputs.
    - Group/share best and worst prompt experiments.

**References:**

- [Prompt Engineering Guide (free)](https://www.promptingguide.ai/)
- [Awesome ChatGPT Prompts (GitHub list)](https://github.com/f/awesome-chatgpt-prompts)
- [DeepLearning.AI Short Course: ChatGPT Prompt Engineering](https://www.deeplearning.ai/short-courses/chatgpt-prompt-eng/)
- [Hugging Face Prompt Engineering with Transformers](https://huggingface.co/learn/prompt-engineering-course/chapter1/introduction)


## Markdown Progress Checklist

Copy, paste, and check off as you complete each step in your markdown notes or project repo:

```markdown
## Phase 3: Generative Models – Progress Tracker

- [ ] **Week 9: Large Language Models (LLMs)**
  - [ ] Read "Hugging Face Transformers Course" chapter on LLMs
  - [ ] Try a pre-trained LLM demo (Hugging Face Spaces)
  - [ ] Experiment with prompts, record reflections
  - [ ] Summarize learnings and risks

- [ ] **Week 10: Generative Adversarial Networks (GANs)**
  - [ ] Complete TensorFlow or PyTorch GANs tutorial (MNIST/demo images)
  - [ ] Visualize generator vs. discriminator outputs
  - [ ] Write a note on GAN uses/abuses

- [ ] **Week 11: Variational Autoencoders (VAEs)**
  - [ ] Read VAE theory from “Dive into Deep Learning”
  - [ ] Run TensorFlow or PyTorch VAE demo
  - [ ] Visualize & interpret latent space
  - [ ] Complete VAE quiz

- [ ] **Week 12: Prompt Engineering & ChatGPT**
  - [ ] Read Prompt Engineering Guide/DeepLearning.AI short course
  - [ ] Run prompt experiments in open playgrounds
  - [ ] Share/compare prompt results
  - [ ] Write a short “prompt design” reflection
```

**Tip:** Log all your code, notes, and summaries each week, and review completed checkboxes to celebrate your progress! If you want **step-by-step lab notebooks** for any of these weeks, just ask.

