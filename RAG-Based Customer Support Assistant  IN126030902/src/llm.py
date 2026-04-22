from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

def generate_answer(context, question):
    prompt = f"""
You are a customer support assistant.

Answer ONLY from context.
If answer not found, say "I don't know".

Context:
{context}

Question:
{question}
"""

    response = llm.invoke(prompt)
    return response.content