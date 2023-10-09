import weaviate
import json
from embedding_util import generate_embeddings

client = weaviate.Client(
    url="http://localhost:8080",  # Replace with your endpoint
)

# Just to illustrate a simple Weaviate health check, if part of a larger system
print('is_ready:', client.is_ready())

# Class definition object. Weaviate's autoschema feature will infer properties
# when importing.
class_obj = {
    "class": "DocumentSearch",
    "vectorizer": "none",
}

# Add the class to the schema
client.schema.create_class(class_obj)


# Test source documents
documents = [
    "A group of vibrant parrots chatter loudly, sharing stories of their tropical adventures.",
    "The mathematician found solace in numbers, deciphering the hidden patterns of the universe.",
    "The robot, with its intricate circuitry and precise movements, assembles the devices swiftly.",
    "The chef, with a sprinkle of spices and a dash of love, creates culinary masterpieces.",
    "The ancient tree, with its gnarled branches and deep roots, whispers secrets of the past.",
    "The detective, with keen observation and logical reasoning, unravels the intricate web of clues.",
    "The sunset paints the sky with shades of orange, pink, and purple, reflecting on the calm sea.",
    "In the dense forest, the howl of a lone wolf echoes, blending with the symphony of the night.",
    "The dancer, with graceful moves and expressive gestures, tells a story without uttering a word.",
    "In the quantum realm, particles flicker in and out of existence, dancing to the tunes of probability."]

# Configure a batch process. Since our "documents" is small, just setting the
# whole batch to the size of the "documents" list
client.batch.configure(batch_size=len(documents))
with client.batch as batch:
    for i, doc in enumerate(documents):
        print(f"document: {i}")

        properties = {
            "source_text": doc,
        }
        vector = generate_embeddings(doc)

        batch.add_data_object(properties, "DocumentSearch", vector=vector)

# test query
query = "Give me some content about the ocean"
query_vector = generate_embeddings(query)

# The default metric for ranking documents is by cosine distance.
# Cosine Similarity = 1 - Cosine Distance
result = client.query.get(
    "DocumentSearch", ["source_text"]
).with_near_vector(
    {
        "vector": query_vector,
        "certainty": 0.7
    }
).with_limit(2).with_additional(['certainty', 'distance']).do()

print(json.dumps(result, indent=4))
