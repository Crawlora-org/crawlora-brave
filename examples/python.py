import os

from crawlora_brave import BraveClient

api_key = os.environ.get("CRAWLORA_API_KEY")
if not api_key:
    raise RuntimeError("Set CRAWLORA_API_KEY before running this example.")

with BraveClient(api_key=api_key) as client:
    search = client.search(q='open source web crawler')
    print('search', search)
    suggest = client.suggest(q='open source')
    print('suggest', suggest)
