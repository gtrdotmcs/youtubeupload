<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

## Phase 4: Advanced Applications – Detailed Breakdown (with Free \& Open Source References)

This phase focuses on using vector databases, retrieval-augmented generation (RAG), fine-tuning large language models (LLMs) with Hugging Face, and deploying a generative AI project. These are the skills that turn advanced knowledge into real, production-ready GenAI apps.

### **Week 13: Vector Databases \& Embeddings**

**Objectives**:

- Understand vector embeddings and why they’re crucial for semantic search and AI.
- Learn to store, retrieve, and search embeddings in a vector database (like ChromaDB, Milvus, Redis, or PostgreSQL’s pgvector).

**Study Plan**:

- **Theory (45min):**
    - What are vector embeddings? Use cases in AI.
    - How vector databases work: indexing, similarity search.
- **Hands-on (45min):**
    - Generate embeddings for text using Python libraries.
    - Store and query embeddings in an open-source vector database (Redis, ChromaDB, or Milvus).
- **Exercise (30min):**
    - Build a mini semantic search app.
    - Compare results of vector-based vs keyword search.

**References**:

- [Embeddings and Vector Databases With ChromaDB (RealPython)](https://realpython.com/chromadb-vector-database/)[^1]
- [Redis as a Vector Database Quick Start](https://redis.io/docs/latest/develop/get-started/vector-database/)[^2]
- [Pgvector for PostgreSQL Tutorial](https://www.tigerdata.com/blog/postgresql-as-a-vector-database-using-pgvector)[^3]
- [Vector Databases: Tutorial \& Examples (Nexla)](https://nexla.com/ai-infrastructure/vector-databases/)[^4]
- [A Complete Developer Guide to Vector Embeddings](https://dev.to/pavanbelagatti/a-complete-developer-guide-to-vector-embeddings-90j)[^5]


### **Week 14: Retrieval-Augmented Generation (RAG)**

**Objectives**:

- Learn how retrieval techniques are paired with LLMs, powering robust Q\&A and chatbots.
- Build your first retrieval-augmented app using open source tools.

**Study Plan**:

- **Theory (40min):**
    - What is RAG? Advantages over pure generation.
    - Components: retrievers, vector store, generator (LLM).
- **Hands-on (50min):**
    - Build a simple RAG pipeline: index data, retrieve with embeddings, generate responses with an LLM.
    - Use tools like LangChain or open-source notebooks in Python.
- **Exercise (30min):**
    - Fine-tune your retrieval data. Experiment with prompt fusion and multiple retrievers.

**References**:

- [Learn RAG from Scratch – Python AI Tutorial (freeCodeCamp)](https://www.freecodecamp.org/news/mastering-rag-from-scratch/)[^6]
- [RAG Tutorial – LangChain Docs](https://python.langchain.com/docs/tutorials/rag/)[^7]
- [RAG Video Tutorial (YouTube)](https://www.youtube.com/watch?v=qN_2fnOPY-M)[^8]
- [A Guide to Retrieval-Augmented Generation (SingleStore)](https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/)[^9]


### **Week 15: Fine-tuning LLMs with Hugging Face**

**Objectives**:

- Learn how to customize (fine-tune) a large language model (LLM) for your data or task.
- Master open-source LLMs and Hugging Face’s tools.

**Study Plan**:

- **Theory (40min):**
    - What is fine-tuning? When is it needed?
    - Overview of Hugging Face ecosystem—Transformers, Datasets, and Training scripts.
- **Hands-on (50min):**
    - Prepare your dataset for training (format, splits).
    - Fine-tune an open-source LLM using Hugging Face’s `transformers` and `trl` libraries.
    - Evaluate and experiment with training configs.
- **Exercise (30min):**
    - Deploy your fine-tuned model as an API or in a demo notebook.

**References**:

- [How to Fine-Tune LLMs in 2024 with Hugging Face (Philipp Schmid)](https://www.philschmid.de/fine-tune-llms-in-2024-with-trl)[^10]
- [Fine-Tuning LLMs Using HuggingFace (dev.to)](https://dev.to/pavanbelagatti/fine-tuning-llms-using-huggingface-a05)[^11]
- [Official Hugging Face Fine-tuning Docs](https://huggingface.co/docs/transformers/en/training)[^12]
- [Finetune LLMs to Teach Them Anything (YouTube)](https://www.youtube.com/watch?v=bZcKYiwtw1I)[^13]


### **Week 16: Final Project \& Deployment**

**Objectives**:

- Build a complete generative AI application with retrieval, generation, or custom tuning.
- Learn how to deploy models and apps for others to use.

**Study Plan**:

- **Theory (30min):**
    - GenAI project architecture: key components, open-source deployment options.
    - MLOps / DevOps for GenAI: versioning, monitoring, and CI/CD basics.
- **Hands-on (60min):**
    - Build and test your end-to-end project (semantic search engine, RAG Q\&A bot, etc.).
    - Deploy on free/OSS platforms (Hugging Face Spaces, GitHub Pages, Streamlit, or even Google Colab).
- **Exercise (30min):**
    - Present your project.
    - Write a project report, highlighting what you learned.

**References**:

- [End-to-End Generative AI Projects (GitHub)](https://github.com/GURPREETKAURJETHRA/END-TO-END-GENERATIVE-AI-PROJECTS)[^14]
- [Deploy and Operate Generative AI Apps (Google Cloud)](https://cloud.google.com/architecture/deploy-operate-generative-ai-applications)[^15]
- [35+ Best Generative AI Projects (ProjectPro)](https://www.projectpro.io/article/generative-ai-projects/1004)[^16]
- [Awesome Generative AI Projects (GitHub list)](https://github.com/steven2358/awesome-generative-ai)[^17]


## Markdown Progress Checklist

Copy this to your project README or notes and check off as you go:

```markdown
## Phase 4: Advanced GenAI Applications – Progress Tracker

- [ ] **Week 13: Vector Databases & Embeddings**
  - [ ] Read a tutorial on vector databases (ChromaDB, Redis, or Milvus)
  - [ ] Complete a hands-on demo (store and search embeddings)
  - [ ] Build and test a basic semantic search app

- [ ] **Week 14: Retrieval-Augmented Generation (RAG)**
  - [ ] Study RAG concepts (course or blog)
  - [ ] Build your first simple RAG pipeline (index, retrieve, generate)
  - [ ] Experiment with different prompt or retrieval setups

- [ ] **Week 15: Fine-tuning LLMs with Hugging Face**
  - [ ] Read and understand LLM fine-tuning basics
  - [ ] Prepare and preprocess your custom dataset
  - [ ] Fine-tune a model with Hugging Face tools
  - [ ] Deploy/demo your model (API, notebook, or public demo)

- [ ] **Week 16: Final Project & Deployment**
  - [ ] Design and build your end-to-end GenAI project
  - [ ] Deploy your app or model using a public/free platform
  - [ ] Write and present your project report
```

**Tip:** Log all code, configs, and findings in your repo each week. Mark checkboxes to visualize your momentum and get ready to showcase your expertise! If you want a guided notebook or specific project ideas for the final deployment, let me know.

<div style="text-align: center">⁂</div>

[^1]: https://realpython.com/chromadb-vector-database/

[^2]: https://redis.io/docs/latest/develop/get-started/vector-database/

[^3]: https://www.tigerdata.com/blog/postgresql-as-a-vector-database-using-pgvector

[^4]: https://nexla.com/ai-infrastructure/vector-databases/

[^5]: https://dev.to/pavanbelagatti/a-complete-developer-guide-to-vector-embeddings-90j

[^6]: https://www.freecodecamp.org/news/mastering-rag-from-scratch/

[^7]: https://python.langchain.com/docs/tutorials/rag/

[^8]: https://www.youtube.com/watch?v=qN_2fnOPY-M

[^9]: https://www.singlestore.com/blog/a-guide-to-retrieval-augmented-generation-rag/

[^10]: https://www.philschmid.de/fine-tune-llms-in-2024-with-trl

[^11]: https://dev.to/pavanbelagatti/fine-tuning-llms-using-huggingface-a05

[^12]: https://huggingface.co/docs/transformers/en/training

[^13]: https://www.youtube.com/watch?v=bZcKYiwtw1I

[^14]: https://github.com/GURPREETKAURJETHRA/END-TO-END-GENERATIVE-AI-PROJECTS

[^15]: https://cloud.google.com/architecture/deploy-operate-generative-ai-applications

[^16]: https://www.projectpro.io/article/generative-ai-projects/1004

[^17]: https://github.com/steven2358/awesome-generative-ai

[^18]: https://www.instaclustr.com/education/vector-database/top-10-open-source-vector-databases/

[^19]: https://platform.openai.com/docs/guides/embeddings

[^20]: https://www.youtube.com/watch?v=sVcwVQRHIc8

