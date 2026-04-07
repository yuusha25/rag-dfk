from pipeline import rag_pipeline
import json

if __name__ == "__main__":
    # Simulate an input passed down by the Keyword Generator or the input text
    query = "Dana HAJI 30% akan Dialokasikan ke sumber dana MBG"

    print(f"=== INPUT ===")
    print(query)
    
    result = rag_pipeline(query)

    print("\n=== GROUND TRUTH / FACT DOCS ===")
    for d in result["fact_contexts"]:
        print(f"[{d['score']:.4f}] {d['meta'].get('title')} ({d['meta'].get('url')})")

    print("\n=== LEGAL DOCS ===")
    for d in result["legal_contexts"]:
        print(f"[{d['score']:.4f}] {d['meta'].get('pasal')} - {d['meta'].get('document_title')}")

    print("\n=== CONTEXT TEXT ===")
    print(result["context_text"])
        