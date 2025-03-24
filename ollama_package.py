import ollama


MODEL = "llama3.2"

# Create a messages list using the same format that we used for OpenAI
messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

response = ollama.chat(model=MODEL, messages=messages)
print(response['message']['content'])