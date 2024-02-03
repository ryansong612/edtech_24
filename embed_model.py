import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity


class Model:
    def __init__(self, model_url):
        model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model_url = model_url
        self.module = hub.load(model_url)

    def generate_embeddings(self, texts):
        embeddings = self.module(texts)
        return embeddings

    def calculate_similarity(self, embeddings1, embeddings2):
        similarity = cosine_similarity(embeddings1, embeddings2)
        return similarity
