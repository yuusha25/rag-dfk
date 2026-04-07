import glob
import os
import uuid
import json
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from config import *

client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)

def create_collection(name):
    print(f"Creating collection: {name}")
    client.recreate_collection(
        collection_name=name,
        vectors_config=VectorParams(size=VECTOR_SIZE, distance=Distance.COSINE)
    )

def load_json(path):
    print(f"Loading {path}...")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_uuid(text_id):
    # Ensures deterministic UUID based on chunk_id
    return str(uuid.uuid5(uuid.NAMESPACE_DNS, str(text_id)))

def upload(collection_name, data):
    print(f"Uploading {len(data)} points to {collection_name}...")
    # Batch uploading is better for large datasets
    batch_size = 500
    for i in range(0, len(data), batch_size):
        batch = data[i:i+batch_size]
        points = []
        for d in batch:
            chunk_id = d.get("chunk_id", d.get("id", ""))
            points.append(
                PointStruct(
                    id=generate_uuid(chunk_id),
                    vector=d["embedding"],
                    payload={
                        "chunk_id": chunk_id,
                        "text": d["text"],
                        **d["metadata"]
                    }
                )
            )
        client.upsert(collection_name=collection_name, points=points)
    print(f"Done uploading to {collection_name}.")

if __name__ == "__main__":
    create_collection(FACT_COLLECTION)
    create_collection(LEGAL_COLLECTION)

    # Load and upload based on dataset folder
    dataset_files = glob.glob("dataset/*.json")
    
    for file in dataset_files:
        data = load_json(file)
        if "turnbackhoax" in os.path.basename(file).lower():
            upload(FACT_COLLECTION, data)
        else:
            upload(LEGAL_COLLECTION, data)