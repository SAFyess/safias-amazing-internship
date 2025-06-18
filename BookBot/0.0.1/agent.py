import json
from nearai.agents.environment import Environment

VECTOR_STORE_ID = "vs_54a28cc3cef0443a94341af0"


def run(env: Environment):
    # Take the last message from the user
    user_query = env.list_messages()[-1]["content"]

    # Query the vector store for relevant information
    vector_results = env.query_vector_store(VECTOR_STORE_ID, user_query)

    # Take the content of the first 4 files returned by the vector store
    cities = [{"file": res["chunk_text"]} for res in vector_results[:4]]

    prompt = [
        {
            "role": "user_query",
            "content": user_query,
        },
        {
            "role": "touristic_information",
            "content": json.dumps(cities),
        },
        {
            "role": "system",
            "content": """
                You're like a kind of library agent.
                 When users ask you for book recommendations based on their
                   criteria (book genre, subject, authors, etc.), you'll have to recommend the book that best meets their expectations.

                Respond only in French, Arabic, and English.

=======

                If you don't have information about a book, simply
                invent something.
>>>>>>> 5de25a020fbf0a05a1e93bc604130a9a9fd82ef6
            """
        }
    ]

    answer = env.completion(prompt)

    env.add_reply(answer)

run(env)