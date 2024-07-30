from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatMessagePromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3.1")
prompt = ChatMessagePromptTemplate.from_template(template, role="system")

def handle_covo():
    context = ""
    print("Welcome To Lama Ai")
    while True:
        userinput = input("You: ")
        if userinput.lower() == "exit":
            break
        # Create the prompt with the current context and user input
        formatted_prompt = prompt.format(context=context, question=userinput)
        # Convert the formatted prompt to a string
        formatted_prompt_str = str(formatted_prompt)
        # Invoke the model with the formatted prompt string
        result = model.invoke(formatted_prompt_str)
        print("Bot: ", result)
        context += f"\nUser: {userinput}\nAI: {result}"

if __name__ == "__main__":
    handle_covo()
