from pinecone import Pinecone


class Db:
    def __init__(self):
        api_key = "6317f4f1-3bc5-43c7-865d-3170f57b169c"
        host = "https://qtags-aa8d656.svc.apw5-4e34-81fa.pinecone.io"
        self.pc = Pinecone(api_key=api_key, environment=host)
        self.index = self.pc.Index("quickstart")

    def upsert(self, vectors: dict, namespace: str) -> None:
        """
        This method is used to upsert vectors into the Pinecone index.
        :param vectors: A dictionary containing the vectors to be updated and inserted.
                            Has the following format: {"id": name, "values": vector, "metadata": json}
        :param namespace: The namespace under which the vectors should be updated and inserted
        :return: None
        """
        self.index.upsert(vectors, namespace=namespace)
        return

    def query(self, namespace: str, vector: list[float], top_k: int,
              include_values=True, include_metadata=True) -> None:
        """
        This method is used to query the Pinecone index.
        :param namespace: The namespace under which the vector is being used as a query
        :param vector: The embedding vector of our user input
        :param top_k: An int representing number of top results we want to return
        :param include_values: Whether the query should return with numerical values
        :param include_metadata: Whether the query should return with metadata
        :return: None
        """
        return self.index.query(queries=vector,
                                amespace=namespace,
                                top_k=top_k,
                                include_values=include_values,
                                include_metadata=include_metadata)
