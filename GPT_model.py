
import os
from dotenv import load_dotenv
from openai import OpenAI
import constants
from cachetools import cached, TTLCache
import json

# Cache API responses for 24 hours with a maximum of 100 entries and a time to live (TTL) of 1 day
cache = TTLCache(maxsize=100, ttl=86400)
load_dotenv()
openai = OpenAI()

api_key = os.getenv("OPENAI_API_KEY")

def analyze_openai(claim: str) -> str:
    """
    Analyzes a claim using the OpenAI API.

    Args:
        claim (str): The claim to be analyzed.

    Returns:
        str: The response from the OpenAI API.
    """
    # Create a list of messages with the system prompt and user input
    messages = [
        {"role": "system", "content": constants.SYSTEM_PROMPT},
        {"role": "user", "content": f"Claim: {claim}"}  # Include the claim in the user input
    ]

    # Create a response from the OpenAI API
    response = openai.chat.completions.create(
        model=constants.MODEL_NAME,  # Use the specified model name
        messages=messages,
        temperature=0.1,  # Set the temperature parameter to 0.1
        max_tokens=200  # Set the maximum number of tokens
    )

    return response.choices[0].message.content

# Cache analysis of a claim with the OpenAI API for up to 24 hours
@cached(cache)
def cached_analyze_claim_with_openai(claim: str) -> str:
    """
    Analyzes a claim using the OpenAI API, caching the result for up to 24 hours.

    Args:
        claim (str): The claim to be analyzed.

    Returns:
        str: The response from the OpenAI API.
    """
    return analyze_openai(claim)

# Parse the JSON response from the OpenAI API
def parse_openai_response(response_text: str) -> dict:
    """
    Parses the JSON response from the OpenAI API.

    Args:
        response_text (str): The JSON response text.

    Returns:
        dict or None: The parsed JSON response, or None if parsing fails.
    """
    try:
        # Attempt to parse the JSON response
        parsed_response = json.loads(response_text)
        return parsed_response
    except json.JSONDecodeError as e:
        # Print an error message if parsing fails
        print(f"Error parsing JSON: {e}")
        return None

# Test the functions
# print(cached_analyze_claim_with_openai(claim="Wisconsin is on pace to double the number of layoffs this year."))
# print(cached_analyze_claim_with_openai(claim="Bellamy Young Opens Up About Being Adopted, Her Real First Name and How She Almost Missed Out on Scandal."))
