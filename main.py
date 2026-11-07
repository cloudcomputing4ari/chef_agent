from langchain.agents import create_agent
from dotenv import load_dotenv
from prompt import SYSTEM_PROMPT, CHEF_PROMPT
from langchain.messages import HumanMessage
from tools import search_recipes
from image_decoder import build_image_message, choose_image_file
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

load_dotenv()

logging.info("Starting the Chef Agent...")
agent = create_agent(
    model="gpt-5-nano",
    tools=[search_recipes],
    system_prompt=SYSTEM_PROMPT
)

logging.info("Agent created successfully. Ready to process images.")
path=choose_image_file()
image_message = build_image_message(path, CHEF_PROMPT)

# response = agent.invoke(
#     {"messages":[{"role": "user", "content": "How are you?"}]}
# )

# response = agent.invoke(
#     {"messages":[HumanMessage(content="How are you?")]}
# )

# print(response.keys())

logging.info("Invoking the agent with the image message...")
response = agent.invoke(
    {"messages":[image_message]}
)

print(response["messages"][-1].content)


