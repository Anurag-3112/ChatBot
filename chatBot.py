from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

model = init_chat_model(model="google_genai:gemini-3.5-flash-lite")

print("chosse your AI mode")
print("press 1 for Angry mode")
print("press 2 for funny mode ")
print("press 3 for sad mode")

choice = int(input("Choose one : "))

if choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif choice == 3:
    mode = "You are an sad AI agent. You respond in depression and sadness ."

message=[
    SystemMessage(content=mode)
]

while True:
    you= input("You: ")
    message.append(HumanMessage(content=you))
    if you=="0":
        break
    response = model.invoke(message)
    message.append(AIMessage(content=response.content))
    print("Bot: ",response.content)

