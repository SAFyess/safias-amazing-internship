import json
from nearai.agents.environment import Environment

VECTOR_STORE_ID = "vs_36e692784feb45a5bb10cfa8"


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
                You are a tourism agent helping people find what to do with
                their vacations. Answer the user staying as true as possible
                to the provided touristic_information.

                If you don't have information about the city, simply
                invent something.
            """
        }
    ]

    answer = env.completion(prompt)

    env.add_reply(answer)

run(env)