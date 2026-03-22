import json
import numpy as np
from utils.embeddings import get_embedding

class VectorStore:
    def __init__(self, data_path):
        with open(data_path, 'r') as f:
            self.data = json.load(f)

        self.embeddings = []
        for item in self.data:
            text = item["error"] + " " + item["code"]
            emb = get_embedding(text)
            self.embeddings.append(emb)

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    def search(self, query, top_k=3):
        query_emb = get_embedding(query)

        results = []
        for i, emb in enumerate(self.embeddings):
            score = self.cosine_similarity(query_emb, emb)
            results.append((score, self.data[i]))

        results.sort(reverse=True, key=lambda x: x[0])
        return results[:top_k]