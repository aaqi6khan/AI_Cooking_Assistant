from serpapi import GoogleSearch
from config import Config
import logging

serpapi_key = Config.get_serpapi_key()

def get_info(product_keyword):
    params = {
        "api_key": serpapi_key,
        "engine": "google",
        "google_domain": "google.com",
        "q": product_keyword,
        "hl": "en",
        "gl": "us",
        "location": "United States",
        "num": "2"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    logging.info(results)

    # Return the shopping results for this product
    out = results.get('organic_results', [])
    logging.info(out)

    return out

