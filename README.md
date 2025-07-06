# 📊 Statistical Educational Q&A Bot

A lightweight, intelligent chatbot designed to help students, educators, and self-learners explore and understand core concepts in statistics. This bot uses natural language understanding to answer questions based on a carefully curated set ofcommonly asked statistical topics.

---

## Why This Project Matters

In today’s data-driven world, **statistics is a foundational skill** across nearly every academic discipline and industry — from psychology and economics to AI and public health. Yet, many learners struggle with understanding statistical terms, the logic behind hypothesis testing, or the interpretation of results.

This Q&A bot is built to:
-  **Democratize access** to clear, concise statistical explanations
-  Support **independent learners** and students studying remotely
-  Serve as a **revision aid** or **study companion** during coursework and exam prep
- Be deployable in resource-constrained environments (low RAM, no GPU)

It brings intelligent tutoring to your browser — no need for textbooks, tutors, or expensive software.

---

## How It Works

1. The user types a statistics-related question.
2. The bot encodes the question using a **small language model** (`MiniLM`) from `sentence-transformers`.
3. The system matches it to the most relevant question in a **300-entry Q&A dataset** using cosine similarity.
4. The matching answer is returned instantly through a clean, interactive UI.

---

## Example Questions It Can Answer

- What is a p-value?
- Explain central limit theorem.
- What is the difference between mean and median?
- What is standard deviation?
- What is a confidence interval?

---

## Technologies Used

| Component | Tech |
|----------|------|
| NLP Model | `sentence-transformers` (`all-MiniLM-L6-v2`) |
| Vector Similarity | Cosine Similarity |
| UI | `Gradio` |
| Dataset | 300-question curated CSV |
| Language | Python |
| Optional Deployment | Hugging Face Spaces, Streamlit Cloud |

---

## How to Run Locally

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
