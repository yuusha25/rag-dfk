from embedder import Embedder
from retriever import search, filter_results
from utils import build_context
from config import *

embedder = Embedder()

def rag_pipeline(query):
    query_vec = embedder.embed(query)

    fact_raw = search(FACT_COLLECTION, query_vec, TOP_K_FACT)
    legal_raw = search(LEGAL_COLLECTION, query_vec, TOP_K_LEGAL)

    fact = filter_results(fact_raw)
    legal = filter_results(legal_raw)
    context_text = build_context(fact, legal)

    return {
        "query": query,
        "fact_contexts": fact,
        "legal_contexts": legal,
        "context_text": context_text,
    }