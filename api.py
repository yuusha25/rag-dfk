from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pipeline import rag_pipeline


class RetrievalRequest(BaseModel):
    query: str


app = FastAPI(
    title="RAG Retrieval API",
    description="API untuk melakukan retrieval fact-check dan dokumen hukum menggunakan RAG.",
    version="1.0"
)


@app.get("/health")
def health_check():
    return {"status": "ok", "detail": "RAG retrieval service is running."}


@app.post("/retrieval")
def retrieval(request: RetrievalRequest):
    query = request.query.strip()
    if not query:
        raise HTTPException(status_code=400, detail="Query must not be empty.")

    result = rag_pipeline(query)
    return result
