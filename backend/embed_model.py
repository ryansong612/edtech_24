import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity



def calculate_similarity(embeddings1, embeddings2):
    similarity = cosine_similarity(embeddings1, embeddings2)
    return similarity


class Model:
    def __init__(self) -> None:
        model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model_url = model_url
        self.module = hub.load(model_url)

    def generate_embeddings(self, texts: list[str]) -> list[list[float]]:
        embeddings = self.module(texts)
        embeddings = embeddings.numpy().tolist()
        return embeddings[0]
