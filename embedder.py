from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("intfloat/multilingual-e5-large")

    def embed(self, text: str):
        return self.model.encode(text).tolist()