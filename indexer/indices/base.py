from elasticsearch import Elasticsearch


class BaseIndex:
    """
    TODO: Docstring this class.
    """

    def __init__(self, es_url: str = "http://localhost:9200") -> None:
        """
        TODO: Docstring this.
        TODO: Do self.es_client.info() to check if the url was valid.
        """
        self.es_client = Elasticsearch(es_url)
        self.tokenizer_pattern = r"(\w|·)+(\.?(\w|·)+)*"

    def create_index(self, index_name: str, mappings: dict) -> None:
        """
        TODO: Docstring this.
        """
        if self.es_client.indices.exists(index=index_name):
            self.es_client.indices.delete(index=index_name)

        self.es_client.indices.create(index=index_name, body=mappings)

    def _verbs_to_ignore_in_autocomplete(self, mode: str, tense: str) -> bool:
        if mode == "Indicatiu" and any(
            t in tense
            for t in [
                "Perfet",
                "Plusquamperfet",
                "Passat perifràstic",
                "Passat anterior",
                "Passat anterior perifràstic",
                "Futur perfet",
                "Condicional perfet",
            ]
        ):
            return True

        if mode == "Subjuntiu" and any(
            t in tense for t in ["Perfet", "Plusquamperfet"]
        ):
            return True

        return bool(
            mode == "Formes no personals"
            and any(
                t in tense for t in ["Infinitiu compost", "Gerundi compost"]
            )
        )
