from __future__ import annotations

import sys
from typing import Any, Callable, Iterable, Iterator, Literal, Mapping, overload

if sys.version_info >= (3, 11):
    from typing import NotRequired, Required, TypedDict, Unpack
else:
    from typing_extensions import NotRequired, Required, TypedDict, Unpack

ResponseType = Literal["auto", "json", "text", "stream"]

class CrawloraError(Exception):
    status: int
    code: int | None
    body: Any
    raw_body: str
    headers: Mapping[str, str]
    request_id: str | None
    def __init__(self, message: str, *, status: int = ..., code: int | None = ..., body: Any = ..., raw_body: str = ..., headers: Mapping[str, str] | None = ..., request_id: str | None = ..., cause: BaseException | None = ...) -> None: ...

class CrawloraClientError(CrawloraError): ...
class CrawloraServerError(CrawloraError): ...
class CrawloraNetworkError(CrawloraError): ...

class _RequestOptions(TypedDict, total=False):
    _response_type: ResponseType
    _timeout: float
    _headers: Mapping[str, str]

ModelAppResponse = TypedDict('ModelAppResponse', {
    'code': NotRequired[int],
    'data': NotRequired[Any],
    'msg': NotRequired[Any],
}, total=False)

ModelBraveVideosResponseDoc = TypedDict('ModelBraveVideosResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveVideosResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveVideosResponse = TypedDict('ModelBraveVideosResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveVideoResult]],
}, total=False)

ModelBraveVideoResult = TypedDict('ModelBraveVideoResult', {
    'age': NotRequired[str],
    'creator': NotRequired[str],
    'description': NotRequired[str],
    'duration': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'platform': NotRequired[str],
    'position': NotRequired[int],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'views': NotRequired[str],
}, total=False)

ModelBraveSearchPagination = TypedDict('ModelBraveSearchPagination', {
    'next_offset': NotRequired[int],
    'offset': NotRequired[int],
    'previous_offset': NotRequired[int],
}, total=False)

ModelBraveSuggestResponseDoc = TypedDict('ModelBraveSuggestResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveSuggestResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveSuggestResponse = TypedDict('ModelBraveSuggestResponse', {
    'query': NotRequired[str],
    'suggestions': NotRequired[list[ModelBraveSuggestionResult]],
}, total=False)

ModelBraveSuggestionResult = TypedDict('ModelBraveSuggestionResult', {
    'entity': NotRequired[ModelBraveSuggestionEntity],
    'position': NotRequired[int],
    'query': NotRequired[str],
}, total=False)

ModelBraveSuggestionEntity = TypedDict('ModelBraveSuggestionEntity', {
    'category': NotRequired[str],
    'description': NotRequired[str],
    'image_url': NotRequired[str],
    'logo': NotRequired[bool],
    'name': NotRequired[str],
}, total=False)

ModelBraveSearchResponseDoc = TypedDict('ModelBraveSearchResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveSearchResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveSearchResponse = TypedDict('ModelBraveSearchResponse', {
    'discussions': NotRequired[list[ModelBraveDiscussion]],
    'knowledge_card': NotRequired[ModelBraveKnowledgeCard],
    'pagination': NotRequired[ModelBraveSearchPagination],
    'related_queries': NotRequired[list[str]],
    'results': NotRequired[list[ModelBraveSearchResult]],
    'videos': NotRequired[list[ModelBraveVideoResult]],
}, total=False)

ModelBraveSearchResult = TypedDict('ModelBraveSearchResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveKnowledgeCard = TypedDict('ModelBraveKnowledgeCard', {
    'category': NotRequired[str],
    'description': NotRequired[str],
    'image': NotRequired[str],
    'long_description': NotRequired[str],
    'provider': NotRequired[ModelBraveKnowledgeCardProvider],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveKnowledgeCardProvider = TypedDict('ModelBraveKnowledgeCardProvider', {
    'icon': NotRequired[str],
    'name': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveDiscussion = TypedDict('ModelBraveDiscussion', {
    'age': NotRequired[str],
    'comment_count': NotRequired[int],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'forum': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'score': NotRequired[int],
    'title': NotRequired[str],
    'top_comment': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveNewsResponseDoc = TypedDict('ModelBraveNewsResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveNewsResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveNewsResponse = TypedDict('ModelBraveNewsResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveNewsResult]],
}, total=False)

ModelBraveNewsResult = TypedDict('ModelBraveNewsResult', {
    'age': NotRequired[str],
    'description': NotRequired[str],
    'favicon': NotRequired[str],
    'hostname': NotRequired[str],
    'path': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
}, total=False)

ModelBraveImagesResponseDoc = TypedDict('ModelBraveImagesResponseDoc', {
    'code': NotRequired[int],
    'data': NotRequired[ModelBraveImagesResponse],
    'msg': NotRequired[str],
}, total=False)

ModelBraveImagesResponse = TypedDict('ModelBraveImagesResponse', {
    'pagination': NotRequired[ModelBraveSearchPagination],
    'results': NotRequired[list[ModelBraveImageResult]],
}, total=False)

ModelBraveImageResult = TypedDict('ModelBraveImageResult', {
    'age': NotRequired[str],
    'height': NotRequired[int],
    'image_url': NotRequired[str],
    'position': NotRequired[int],
    'source': NotRequired[str],
    'thumbnail': NotRequired[str],
    'title': NotRequired[str],
    'url': NotRequired[str],
    'width': NotRequired[int],
}, total=False)

BraveImagesResponse = ModelBraveImagesResponseDoc
BraveImagesParams = TypedDict('BraveImagesParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveNewsResponse = ModelBraveNewsResponseDoc
BraveNewsParams = TypedDict('BraveNewsParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSearchResponse = ModelBraveSearchResponseDoc
BraveSearchParams = TypedDict('BraveSearchParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSuggestResponse = ModelBraveSuggestResponseDoc
BraveSuggestParams = TypedDict('BraveSuggestParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'rich': NotRequired[bool],
}, total=False)

BraveVideosResponse = ModelBraveVideosResponseDoc
BraveVideosParams = TypedDict('BraveVideosParams', {
    '_response_type': NotRequired[ResponseType],
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

class BraveGroup:
    @overload
    def images(self, **params: Unpack[BraveImagesStreamParams]) -> BinaryIO: ...
    @overload
    def images(self, **params: Unpack[BraveImagesTextResponseParams]) -> str: ...
    @overload
    def images(self, **params: Unpack[BraveImagesDefaultParams]) -> BraveImagesResponse: ...
    @overload
    def news(self, **params: Unpack[BraveNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BraveNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BraveNewsDefaultParams]) -> BraveNewsResponse: ...
    @overload
    def search(self, **params: Unpack[BraveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BraveSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BraveSearchDefaultParams]) -> BraveSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestDefaultParams]) -> BraveSuggestResponse: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosDefaultParams]) -> BraveVideosResponse: ...

OperationId = Literal[
    'brave-images',
    'brave-news',
    'brave-search',
    'brave-suggest',
    'brave-videos',
]

class CrawloraClient:
    brave: BraveGroup
    api_key: str
    jwt_token: str
    base_url: str
    timeout: float
    retries: int
    retry_delay: float
    max_retry_delay: float
    retry_statuses: frozenset[int] | None
    retry_predicate: Callable[[int, BaseException | None], bool] | None
    on_retry: Callable[[int, BaseException, float], None] | None
    request_id: bool
    idempotency_keys: bool
    rate_limit: float | None
    max_concurrency: int | None
    logger: Callable[[Mapping[str, Any]], None] | None
    before_request: list[Callable[[dict[str, Any]], None]]
    after_response: list[Callable[[str, int, Mapping[str, str], Any], Any]]
    headers: dict[str, str]
    user_agent: str
    def _is_retryable(self, status: int, exc: BaseException | None) -> bool: ...
    def _compute_retry_delay(self, attempt: int, headers: Mapping[str, str]) -> float: ...
    def _log(self, event: Mapping[str, Any]) -> None: ...
    def __init__(
        self,
        *,
        api_key: str | None = ...,
        jwt_token: str | None = ...,
        base_url: str | None = ...,
        timeout: float = ...,
        retries: int = ...,
        retry_delay: float = ...,
        max_retry_delay: float = ...,
        retry_statuses: Iterable[int] | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
        on_retry: Callable[[int, BaseException, float], None] | None = ...,
        request_id: bool = ...,
        idempotency_keys: bool = ...,
        rate_limit: float | None = ...,
        max_concurrency: int | None = ...,
        logger: Callable[[Mapping[str, Any]], None] | None = ...,
        before_request: Callable[[dict[str, Any]], None] | Iterable[Callable[[dict[str, Any]], None]] | None = ...,
        after_response: Callable[[str, int, Mapping[str, str], Any], Any] | Iterable[Callable[[str, int, Mapping[str, str], Any], Any]] | None = ...,
        headers: Mapping[str, str] | None = ...,
        user_agent: str | None = ...,
        transport: Callable[..., Any] | None = ...,
    ) -> None: ...
    def close(self) -> None: ...
    def __enter__(self) -> CrawloraClient: ...
    def __exit__(self, *exc: Any) -> None: ...
    def paginate(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    def paginate_items(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        items: Callable[[Any], Any] | None = ...,
        page_param: str | None = ...,
        cursor_param: str | None = ...,
        next_cursor: Callable[[Any], Any] | None = ...,
        start: Any = ...,
        step: int = ...,
        max_pages: int | None = ...,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
    ) -> Iterator[Any]: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-images'],
        params: BraveImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveImagesResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-news'],
        params: BraveNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveNewsResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-search'],
        params: BraveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSearchResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-suggest'],
        params: BraveSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSuggestResponse: ...
    @overload
    def operation(
        self,
        operation_id: Literal['brave-videos'],
        params: BraveVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveVideosResponse: ...
    @overload
    def operation(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-images'],
        params: BraveImagesParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveImagesResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-news'],
        params: BraveNewsParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveNewsResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-search'],
        params: BraveSearchParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSearchResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-suggest'],
        params: BraveSuggestParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveSuggestResponse: ...
    @overload
    def request(
        self,
        operation_id: Literal['brave-videos'],
        params: BraveVideosParams,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> BraveVideosResponse: ...
    @overload
    def request(
        self,
        operation_id: str,
        params: Mapping[str, Any] | None = ...,
        *,
        response_type: ResponseType = ...,
        timeout: float | None = ...,
        headers: Mapping[str, str] | None = ...,
        retries: int | None = ...,
        retry_predicate: Callable[[int, BaseException | None], bool] | None = ...,
    ) -> Any: ...

VERSION: str

# Internal helpers reused by the async client; not part of the public API.
def _build_request(base_url: str, operation: Mapping[str, Any], params: dict[str, Any]) -> tuple[Any, Any, dict[str, str]]: ...
def _merge_headers(*sources: Mapping[str, str]) -> dict[str, str]: ...
def _auth_headers(security: list[str], api_key: str, jwt_token: str) -> dict[str, str]: ...
def _ensure_request_id(headers: dict[str, str]) -> str: ...
def _header_value(headers: Mapping[str, str], name: str) -> str: ...
def _parse_response(body: bytes, content_type: str, response_type: str) -> Any: ...
def _validate_response_type(response_type: str) -> ResponseType: ...
def _api_error_class(status: int) -> type[CrawloraError]: ...
def _run_before_request(hooks: list[Any], ctx: dict[str, Any]) -> None: ...
def _run_after_response(hooks: list[Any], operation_id: Any, status: int, headers: Mapping[str, str], body: Any) -> Any: ...
def _allowed_params(operation_id: str) -> set[str]: ...

from typing import BinaryIO

class AsyncCrawloraClient:
    def __init__(self, **kwargs: Any) -> None: ...
    async def aclose(self) -> None: ...
    async def __aenter__(self) -> AsyncCrawloraClient: ...
    async def __aexit__(self, *exc: Any) -> None: ...
    async def request(self, operation_id: str, params: Mapping[str, Any] | None = ..., *, response_type: ResponseType = ..., timeout: float | None = ..., headers: Mapping[str, str] | None = ..., retries: int | None = ..., retry_predicate: Callable[[int, BaseException | None], bool] | None = ...) -> Any: ...

class BraveClient(CrawloraClient):
    def __enter__(self) -> BraveClient: ...
    @overload
    def images(self, **params: Unpack[BraveImagesStreamParams]) -> BinaryIO: ...
    @overload
    def images(self, **params: Unpack[BraveImagesTextResponseParams]) -> str: ...
    @overload
    def images(self, **params: Unpack[BraveImagesDefaultParams]) -> BraveImagesResponse: ...
    @overload
    def news(self, **params: Unpack[BraveNewsStreamParams]) -> BinaryIO: ...
    @overload
    def news(self, **params: Unpack[BraveNewsTextResponseParams]) -> str: ...
    @overload
    def news(self, **params: Unpack[BraveNewsDefaultParams]) -> BraveNewsResponse: ...
    @overload
    def search(self, **params: Unpack[BraveSearchStreamParams]) -> BinaryIO: ...
    @overload
    def search(self, **params: Unpack[BraveSearchTextResponseParams]) -> str: ...
    @overload
    def search(self, **params: Unpack[BraveSearchDefaultParams]) -> BraveSearchResponse: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestStreamParams]) -> BinaryIO: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestTextResponseParams]) -> str: ...
    @overload
    def suggest(self, **params: Unpack[BraveSuggestDefaultParams]) -> BraveSuggestResponse: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosStreamParams]) -> BinaryIO: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosTextResponseParams]) -> str: ...
    @overload
    def videos(self, **params: Unpack[BraveVideosDefaultParams]) -> BraveVideosResponse: ...

class AsyncBraveClient(AsyncCrawloraClient):
    async def __aenter__(self) -> AsyncBraveClient: ...
    brave: _AsyncBraveGroup
    @overload
    async def images(self, **params: Unpack[BraveImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def images(self, **params: Unpack[BraveImagesTextResponseParams]) -> str: ...
    @overload
    async def images(self, **params: Unpack[BraveImagesDefaultParams]) -> BraveImagesResponse: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsDefaultParams]) -> BraveNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchDefaultParams]) -> BraveSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestDefaultParams]) -> BraveSuggestResponse: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosDefaultParams]) -> BraveVideosResponse: ...

class _AsyncBraveGroup:
    @overload
    async def images(self, **params: Unpack[BraveImagesStreamParams]) -> BinaryIO: ...
    @overload
    async def images(self, **params: Unpack[BraveImagesTextResponseParams]) -> str: ...
    @overload
    async def images(self, **params: Unpack[BraveImagesDefaultParams]) -> BraveImagesResponse: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsStreamParams]) -> BinaryIO: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsTextResponseParams]) -> str: ...
    @overload
    async def news(self, **params: Unpack[BraveNewsDefaultParams]) -> BraveNewsResponse: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchStreamParams]) -> BinaryIO: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchTextResponseParams]) -> str: ...
    @overload
    async def search(self, **params: Unpack[BraveSearchDefaultParams]) -> BraveSearchResponse: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestStreamParams]) -> BinaryIO: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestTextResponseParams]) -> str: ...
    @overload
    async def suggest(self, **params: Unpack[BraveSuggestDefaultParams]) -> BraveSuggestResponse: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosStreamParams]) -> BinaryIO: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosTextResponseParams]) -> str: ...
    @overload
    async def videos(self, **params: Unpack[BraveVideosDefaultParams]) -> BraveVideosResponse: ...

BraveImagesDefaultParams = TypedDict('BraveImagesDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveImagesTextResponseParams = TypedDict('BraveImagesTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveImagesStreamParams = TypedDict('BraveImagesStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
}, total=False)

BraveNewsDefaultParams = TypedDict('BraveNewsDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveNewsTextResponseParams = TypedDict('BraveNewsTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveNewsStreamParams = TypedDict('BraveNewsStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSearchDefaultParams = TypedDict('BraveSearchDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSearchTextResponseParams = TypedDict('BraveSearchTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSearchStreamParams = TypedDict('BraveSearchStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveSuggestDefaultParams = TypedDict('BraveSuggestDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'rich': NotRequired[bool],
}, total=False)

BraveSuggestTextResponseParams = TypedDict('BraveSuggestTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'rich': NotRequired[bool],
}, total=False)

BraveSuggestStreamParams = TypedDict('BraveSuggestStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'rich': NotRequired[bool],
}, total=False)

BraveVideosDefaultParams = TypedDict('BraveVideosDefaultParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': NotRequired[Literal["auto", "json"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveVideosTextResponseParams = TypedDict('BraveVideosTextResponseParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["text"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)

BraveVideosStreamParams = TypedDict('BraveVideosStreamParams', {
    '_timeout': NotRequired[float],
    '_headers': NotRequired[Mapping[str, str]],
    '_response_type': Required[Literal["stream"]],
    'q': Required[str],
    'offset': NotRequired[int],
    'count': NotRequired[int],
    'country': NotRequired[Literal['all', 'ar', 'at', 'au', 'be', 'br', 'ca', 'ch', 'cl', 'cn', 'de', 'dk', 'es', 'fi', 'fr', 'gb', 'gr', 'hk', 'id', 'in', 'it', 'jp', 'kr', 'mx', 'my', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ru', 'sa', 'se', 'sg', 'tr', 'tw', 'us', 'za']],
    'lang': NotRequired[Literal['de-de', 'en-ca', 'en-gb', 'en-in', 'en-us', 'fi-fi', 'fr-ca', 'fr-fr', 'ja-jp', 'pt-br', 'sq-al', 'sw-ke', 'zh-tw']],
    'time_range': NotRequired[Literal['any', 'day', 'week', 'month', 'year', 'custom']],
    'date_from': NotRequired[str],
    'date_to': NotRequired[str],
}, total=False)
