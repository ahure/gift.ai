import requests
import json

# Import API keys from config
from config import ETSY_API_KEY

BASE_URL = "https://openapi.etsy.com/v3/application/"

def get_etsy_data(keywords, min_price=None, max_price=None, limit=5):
    """
    Fetches product data from the Etsy API based on user input.

    Parameters:
        keywords (str): Search term(s) to query Etsy.
        min_price (int, optional): Minimum price filter.
        max_price (int, optional): Maximum price filter.
        limit (int, optional): Number of results to fetch. Defaults to 5.

    Returns:
        list: A list of product dictionaries containing title, price, and URL.
    """
    headers = {
        "x-api-key": ETSY_API_KEY,
    }

    # Construct query parameters
    params = {
        "keywords": keywords,
        "limit": limit,
    }
    if min_price:
        params["min_price"] = min_price
    if max_price:
        params["max_price"] = max_price

    # Make API request
    try:
        response = requests.get(f"{BASE_URL}listings/active", headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        # Parse and format the results
        results = []
        for listing in data.get("results", []):
            results.append({
                "title": listing.get("title"),
                "price": listing.get("price"),
                "currency": listing.get("currency_code"),
                "url": listing.get("url"),
                "image": listing.get("image", {}).get("src"),
            })

        return results

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Etsy API: {e}")
        return []

# Example usage (for testing purposes):
if __name__ == "__main__":
    products = get_etsy_data("handmade jewelry", min_price=50, max_price=100, limit=3)
    print(json.dumps(products, indent=2))