from langchain_community.llms import Ollama
llm = Ollama(model="phi")

print(llm.invoke("hello"))