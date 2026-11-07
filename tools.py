from tavily import TavilyClient
from dotenv import load_dotenv
from langchain.tools import tool
from typing import Dict, Any
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

load_dotenv()

tavily_client = TavilyClient()

@tool
def search_recipes(ingredients: str) -> Dict[str, Any]:
    """
    Search for recipes based on the given ingredients.

    Args:
        ingredients (str): A string containing the ingredients to search for.
        """

    logging.info(f"Searching for recipes with ingredients: {ingredients}")
    # Use the TavilyClient to search for recipes
    recipes = tavily_client.search(ingredients)
    
    return {"recipes": recipes}