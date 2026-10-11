"""Typed Brave Search client for the Crawlora hosted API."""

from .platform import BraveClient, AsyncBraveClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BraveClient
AsyncClient = AsyncBraveClient
__version__ = '0.1.0'
DISPLAY_NAME = 'Brave Search'
PLATFORM = 'brave'
CONTRACT_REVISION = 'sha256:2548401e77b60108e6195aa3c83842dc0c1caa7f04e8c777b61ccab2ca397777'

__all__ = [
    "BraveClient", "AsyncBraveClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
