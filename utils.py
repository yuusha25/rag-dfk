from config import MAX_CONTEXT_CHARS

def build_context(fact_docs, legal_docs):
    context = "FACT CHECK:\n\n"

    for d in fact_docs:
        context += f"- {d['text']}\n\n"

    context += "\nLEGAL BASIS:\n\n"

    for d in legal_docs:
        context += f"- {d['text']}\n\n"

    return context[:MAX_CONTEXT_CHARS]