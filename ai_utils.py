from ollama import Client

# Connect to Ollama locally
client = Client(host='http://localhost:11434')  # default Ollama endpoint

def generate_answer(prompt):
    response = client.chat(model='tinyllama', messages=[
        {"role": "user", "content": prompt}
    ])
    return response['message']['content']
