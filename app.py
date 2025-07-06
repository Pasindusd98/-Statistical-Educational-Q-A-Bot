import pandas as pd
from sentence_transformers import SentenceTransformer, util
import gradio as gr

# Load the CSV file with 300 Q&A pairs
qa_df = pd.read_csv("statistics_qa_300.csv")

# sentence embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

# Precompute embeddings for all questions in the CSV
qa_df["embedding"] = qa_df["question"].apply(lambda q: model.encode(q, convert_to_tensor=True))

# Function to find the most similar question and return its answer
def get_answer(user_input):
    user_embedding = model.encode(user_input, convert_to_tensor=True)
    similarities = qa_df["embedding"].apply(lambda emb: float(util.pytorch_cos_sim(emb, user_embedding)))
    best_match = qa_df.loc[similarities.idxmax()]
    return best_match["answer"]

# Gradio UI
iface = gr.Interface(
    fn=get_answer,
    inputs=gr.Textbox(lines=2, placeholder="Ask a statistics question..."),
    outputs="text",
    title="📊 Statistics Q&A Chatbot",
    description="Ask me anything about statistics! (e.g., What is standard deviation?)",
    allow_flagging="never"
)

iface.launch()
