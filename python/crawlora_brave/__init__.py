"""Typed Brave Search client for the Crawlora hosted API."""

from .platform import BraveClient, AsyncBraveClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = BraveClient
AsyncClient = AsyncBraveClient
__version__ = '0.2.0'
DISPLAY_NAME = 'Brave Search'
PLATFORM = 'brave'
CONTRACT_REVISION = 'sha256:18fad8582a4a32958daafc4d0e435a8917a78048abc17daa817169a107ea2fba'

__all__ = [
    "BraveClient", "AsyncBraveClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
