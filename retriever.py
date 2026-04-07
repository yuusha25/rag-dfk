from qdrant_client import QdrantClient
from config import *

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def search(collection, query_vector, top_k):
    return client.search(
        collection_name=collection,
        query_vector=query_vector,
        limit=top_k
    )

def filter_results(results):
    return [
        {
            "text": r.payload["text"],
            "score": r.score,
            "meta": {k:v for k,v in r.payload.items() if k not in ["text", "chunk_id"]}
        }
        for r in results if r.score >= SIM_THRESHOLD
    ]
