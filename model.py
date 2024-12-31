from openai import OpenAI
from config import API_KEY, DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE

# Initialize OpenAI client
client = OpenAI(api_key=API_KEY)

def get_ai_response(messages, model=DEFAULT_MODEL, max_tokens=DEFAULT_MAX_TOKENS, temperature=DEFAULT_TEMPERATURE):
    """
    Sends the conversation history to OpenAI and retrieves a response.
    Args:
        messages (list): Conversation history as a list of dicts.
        model (str): Model to use (default: `DEFAULT_MODEL`).
        max_tokens (int): Maximum number of tokens for the response.
        temperature (float): Sampling temperature (default: `DEFAULT_TEMPERATURE`).
    Returns:
        str: AI's response.
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        raise RuntimeError(f"Error while calling OpenAI API: {e}")