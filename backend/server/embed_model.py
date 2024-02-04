import tensorflow as tf
import tensorflow_hub as hub
import numpy as np


def calculate_similarity(embeddings1, embeddings2):
    return np.inner(embeddings1, embeddings2)


class Model:
    def __init__(self) -> None:
        model_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
        self.model_url = model_url
        # self.module = hub.load(model_url)
        self.module = tf.saved_model.load('../saved_model')

    def generate_embeddings(self, texts: list[str]) -> list[float]:
        embeddings = self.module(texts)
        embeddings = embeddings.numpy().tolist()
        return embeddings[0]
