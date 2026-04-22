from src.ingestion import ingest_pdf
from src.workflow import build_graph

def run():
    ingest_pdf("data/knowledge_base.pdf")

    app = build_graph()

    print("\n🤖 Bot Ready (type exit to quit)\n")

    while True:
        q = input("User: ")

        if q.lower() == "exit":
            break

        result = app.invoke({"query": q})

        print("\nBot:", result["answer"], "\n")

if __name__ == "__main__":
    run()