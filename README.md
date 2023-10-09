# Example Weaviate vector embeddings

This is the companion code repository for [my blog post on vector embeddings with Weaviate](https://stephencollins.tech/posts/how-to-use-weaviate-to-store-and-query-vector-embeddings).

## Getting Started

To run weaviate in server mode in a _foreground_ process for easier testing with `app.py`, I've setup a simple docker compose configuration to pull down the latest Weaviate server docker image, that will run on port `8080`. Just run the following script, assuming you have both docker and docker compose installed from the root of this project:

`sh start.sh`

## Run the Example

To run the example `app.py` Python application, install the requirements.txt file for `app.py`. And assuming you have a modern Python 3 version installed simply:

`python app.py`

This will do the following:

1. Create a Weaviate client
2. Print a Weaviate server health check
3. Create a Weaviate class, `DocumentSearch`
4. Add documents to the `DocumentSearch` class-based collection
5. Query the collection using Cosine Distance
6. Print the results including Cosine Similarity scores\*

_NOTE: Cosine Similarity = 1 - Cosine Distance_
