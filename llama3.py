import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'what is role option',
  },
])
print(response['message']['content'])