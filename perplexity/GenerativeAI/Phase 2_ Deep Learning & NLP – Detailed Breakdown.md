<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Phase 2: Deep Learning \& NLP – Detailed Breakdown

*All resources here are free and open source. Use the checklist at the bottom to stay on track!*

### **Week 5: Introduction to Neural Networks**

**Objectives:**

- Understand basic neural network concepts: perceptrons, layers, activation functions, loss, and training.
- Build, visualize, and experiment with a simple neural network.

**Study Plan:**

- **Theory (45min):**
    - What are neural networks? How are they inspired by the brain?
    - How do forward \& backward propagation work?
    - Activation functions: sigmoid, ReLU, tanh.
- **Hands-on (45min):**
    - Follow a basic neural network build in Python (see references below)
    - Try interactive demos—adjust hyperparameters and see learning in action.
- **Exercise (30min):**
    - Visualize how changing layers, activation, or loss changes performance.
    - Make predictions and interpret results.

**References:**

- [Intro to Neural Networks – Victor Zhou](https://victorzhou.com/blog/intro-to-neural-networks/)[^1]
- [GeeksforGeeks: Neural Networks Tutorial](https://www.geeksforgeeks.org/machine-learning/neural-networks-a-beginners-guide/)[^2][^3]
- [Interactive Demos – Google Neural Networks](https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises)[^4]
- [Step-by-step Build – RealPython](https://realpython.com/python-ai-neural-network/)[^5]
- [Neural Networks and Deep Learning (book)](http://neuralnetworksanddeeplearning.com)[^6]
- [YouTube: But what is a Neural Network? (3Blue1Brown)](https://www.youtube.com/watch?v=aircAruvnKk&vl=en)[^7]


### **Week 6: Deep Learning with PyTorch**

**Objectives:**

- Install PyTorch and dive into defining, training, and evaluating models.
- Learn how to use tensors, build a neural network, and run real data.

**Study Plan:**

- **Theory (30min):**
    - What is PyTorch, and how does it differ from TensorFlow?
    - Core concepts: tensors, autograd, modules.
- **Hands-on (60min):**
    - Complete a beginner PyTorch tutorial: create and train a simple classifier (e.g., digit recognizer).
    - Use free cloud GPU on Colab or OpenCV's free bootcamp.
- **Exercise (30min):**
    - Tune basic hyperparameters, like epochs, learning rate, or optimizer.
    - Export results to notebook or script.

**References:**

- [Learn PyTorch for Deep Learning (Zero to Mastery – free book and video)](https://www.learnpytorch.io)[^8]
- [Scaler Free PyTorch Deep Learning Course](https://www.scaler.com/topics/course/pytorch-for-deep-learning-free-course/)[^9]
- [OpenCV Free PyTorch Bootcamp](https://opencv.org/university/free-pytorch-course/)[^10]
- [GeeksforGeeks: Deep Learning Tutorial](https://www.geeksforgeeks.org/deep-learning/deep-learning-tutorial/)[^3]
- [Kaggle Intro to Deep Learning Micro-course](https://www.kaggle.com/learn/intro-to-deep-learning)[also search result]


### **Week 7: Natural Language Processing (NLP) Basics**

**Objectives:**

- What is NLP, and why is it crucial for generative AI?
- Learn text processing: tokenization, cleaning, word embeddings.
- Use libraries like NLTK, spaCy, scikit-learn.

**Study Plan:**

- **Theory (40min):**
    - What are Bag-of-Words, TF-IDF, and embeddings?
    - Text pre-processing: stopwords, stemming, lemmatization.
- **Hands-on (50min):**
    - Tokenize text with spaCy or NLTK.
    - Build a basic text classifier (e.g., sentiment analysis).
- **Exercise (30min):**
    - Try classifying text and visualizing results.
    - Use an open dataset (IMDB, Twitter, etc).

**References:**

- [Free NLP Course – Simplilearn](https://www.simplilearn.com/learn-basics-of-natural-language-processing-free-course-skillup)[^11]
- [5 Free NLP Courses – KDnuggets](https://www.kdnuggets.com/5-free-courses-to-master-natural-language-processing)[^12]
- [Kaggle NLP Resources](https://www.kaggle.com/questions-and-answers/278543)[^13]
- [Stanford Speech \& Language Processing Book (PDF, free)](https://web.stanford.edu/~jurafsky/slp3/9.pdf)[^14]
- [spaCy Official Course](https://course.spacy.io/)[also search result]


### **Week 8: Transformers Architecture**

**Objectives:**

- Learn the core architecture of transformer models.
- Discover how transformers drove the leap to LLMs.
- Understand self-attention, encoder-decoder, positional encoding.

**Study Plan:**

- **Theory (50min):**
    - Read The Illustrated Transformer (with animations and diagrams).
    - Key ideas: self-attention, positional encodings, large-scale training.
- **Hands-on (40min):**
    - Run a transformer model with Hugging Face or Colab (e.g., text summarization).
    - Visualize attention patterns.
- **Exercise (30min):**
    - Summarize how transformers differ from RNN/CNN.
    - Experiment: tweak input, see model response.

**References:**

- [The Illustrated Transformer (Jay Alammar, now with 2025 update)](https://jalammar.github.io/illustrated-transformer/)[^15]
- [Stanford NLP Book chapter: The Transformer (PDF)](https://web.stanford.edu/~jurafsky/slp3/9.pdf)[^14]
- [YouTube: Evolution of Transformer Architecture](https://www.youtube.com/watch?v=8WBS0dT0h2I)[^16]
- [FreeCodeCamp course: Transformers in LLMs](https://www.freecodecamp.org/news/learn-the-evolution-of-the-transformer-architecture-used-in-llms/)[^17]
- [Hugging Face Transformers Courses \& Tutorials (open)](https://huggingface.co/docs/transformers/index)[also search result]


## Markdown Progress Checklist

Copy this to your repo or notes and tick off as you master each step:

```markdown
## Phase 2: Deep Learning & NLP – Progress Tracker

- [ ] **Week 5: Introduction to Neural Networks**
  - [ ] Read an intro neural networks tutorial (Victor Zhou, GFG, or similar)
  - [ ] Complete a hands-on neural network playground or notebook
  - [ ] Record notes on activation functions and loss

- [ ] **Week 6: Deep Learning with PyTorch**
  - [ ] Install PyTorch and run beginner tutorial/project (Scaler, ZTM, OpenCV Bootcamp)
  - [ ] Train a simple deep learning model and tune hyperparameters
  - [ ] Save and comment on your model results

- [ ] **Week 7: NLP Basics**
  - [ ] Complete a free NLP crash course (Simplilearn, spaCy, etc)
  - [ ] Tokenize and classify a real dataset (IMDB, Twitter, etc)
  - [ ] Investigate word embeddings and create text visualizations

- [ ] **Week 8: Transformers Architecture**
  - [ ] Study The Illustrated Transformer and videos/courses
  - [ ] Run a real transformer model on Hugging Face or Colab
  - [ ] Document key differences between transformers and other models
```

**Pro Tip:** Always save your code, notes, and results each week. At the end of Phase 2, you’ll have both a strong theoretical understanding _and_ several hands-on projects/code samples for your portfolio! If you want any notebook labs or detailed tutorials for any specific week, just ask.

<div style="text-align: center">⁂</div>

[^1]: https://victorzhou.com/blog/intro-to-neural-networks/

[^2]: https://www.geeksforgeeks.org/machine-learning/neural-networks-a-beginners-guide/

[^3]: https://www.geeksforgeeks.org/deep-learning/deep-learning-tutorial/

[^4]: https://developers.google.com/machine-learning/crash-course/neural-networks/interactive-exercises

[^5]: https://realpython.com/python-ai-neural-network/

[^6]: http://neuralnetworksanddeeplearning.com

[^7]: https://www.youtube.com/watch?v=aircAruvnKk\&vl=en

[^8]: https://www.learnpytorch.io

[^9]: https://www.scaler.com/topics/course/pytorch-for-deep-learning-free-course/

[^10]: https://opencv.org/university/free-pytorch-course/

[^11]: https://www.simplilearn.com/learn-basics-of-natural-language-processing-free-course-skillup

[^12]: https://www.kdnuggets.com/5-free-courses-to-master-natural-language-processing

[^13]: https://www.kaggle.com/questions-and-answers/278543

[^14]: https://web.stanford.edu/~jurafsky/slp3/9.pdf

[^15]: https://jalammar.github.io/illustrated-transformer/

[^16]: https://www.youtube.com/watch?v=8WBS0dT0h2I

[^17]: https://www.freecodecamp.org/news/learn-the-evolution-of-the-transformer-architecture-used-in-llms/

[^18]: https://www.baeldung.com/cs/ml-open-source-libraries

[^19]: https://www.edx.org/learn/natural-language-processing

[^20]: https://www.coursera.org/learn/advanced-deep-learning-with-pytorch

