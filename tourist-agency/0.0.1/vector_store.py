import json
from glob import glob

import openai
import nearai

# Load NEAR AI Hub configuration
config = nearai.config.load_config_file()
base_url = config.get("api_url", "https://api.near.ai/") + "v1"
auth = config["auth"]

client = openai.OpenAI(base_url=base_url, api_key=json.dumps(auth))

# Get a list of all the markdown files in the "cities" folder
md_files = list(glob("./cities/*.md", recursive=True))
file_ids = []

print("All Files:", md_files)

for file_path in md_files:
    print(f"Processing {file_path}")

    with open(file_path, 'r', encoding='utf-8') as file:
        uploaded_file = client.files.create(
            file=(file_path, file.read(), "text/markdown"),
            purpose="assistants"
        )
        file_ids.append(uploaded_file.id)

vs = client.vector_stores.create(
    name="cities",
    file_ids=file_ids,
)

print("The vector store ID:", vs.id)
