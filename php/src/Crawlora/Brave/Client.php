<?php

declare(strict_types=1);

namespace Crawlora\Brave;

class CrawloraException extends \RuntimeException
{
    public function __construct(string $message, public readonly ?int $status = null, public readonly ?string $operationId = null, public readonly ?string $responseBody = null, ?\Throwable $previous = null)
    {
        parent::__construct($message, 0, $previous);
    }
}

class ClientException extends CrawloraException {}
class ServerException extends CrawloraException {}
class NetworkException extends CrawloraException {}

final class Client
{
    private static array $operations;
    private bool $closed = false;
    private string $apiKey;
    private string $baseUrl;
    private float $timeout;
    private ?\Closure $transport;

    public const PLATFORM = 'brave';
    public const VERSION = '0.1.0';
    public const OPERATION_COUNT = 5;
    public const OPERATION_IDS = ["brave-images", "brave-news", "brave-search", "brave-suggest", "brave-videos"];

    public function __construct(?string $apiKey = null, string $baseUrl = 'https://api.crawlora.net/api/v1', float $timeout = 30.0, ?callable $transport = null)
    {
        $this->apiKey = $apiKey ?? (getenv('CRAWLORA_API_KEY') ?: '');
        $this->baseUrl = rtrim($baseUrl, '/');
        $this->timeout = $timeout;
        $this->transport = $transport === null ? null : \Closure::fromCallable($transport);
        self::$operations ??= json_decode(<<<'JSON'
{"brave-images": {"bodyParam": null, "bodyRequired": false, "id": "brave-images", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Zero-based Brave result page; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 0}, {"description": "Results to return; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Brave result country; defaults to us", "enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Brave UI language; defaults to en-us", "enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}], "path": "/brave/images", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string"}, {"enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string"}], "security": ["ApiKeyAuth"]}, "brave-news": {"bodyParam": null, "bodyRequired": false, "id": "brave-news", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Zero-based Brave result page; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 0}, {"description": "Results to return; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Brave result country; defaults to us", "enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Brave UI language; defaults to en-us", "enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Preset time filter: any, day, week, month, year, or custom", "enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"description": "Custom start date in YYYY-MM-DD; requires date_to", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-03-01"}, {"description": "Custom end date in YYYY-MM-DD; requires date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-03-30"}], "path": "/brave/news", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string"}, {"enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string"}, {"enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}], "security": ["ApiKeyAuth"]}, "brave-search": {"bodyParam": null, "bodyRequired": false, "id": "brave-search", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Zero-based Brave result page", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 1}, {"description": "Brave result country; defaults to us", "enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Brave UI language; defaults to en-us", "enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Preset time filter: any, day, week, month, year, or custom", "enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"description": "Custom start date in YYYY-MM-DD; requires date_to", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-03-01"}, {"description": "Custom end date in YYYY-MM-DD; requires date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-03-30"}], "path": "/brave/search", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string"}, {"enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string"}, {"enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}], "security": ["ApiKeyAuth"]}, "brave-suggest": {"bodyParam": null, "bodyRequired": false, "id": "brave-suggest", "method": "GET", "params": [{"description": "Search query prefix", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Suggestions to return; defaults to 10, clamped to 1..12", "in": "query", "maximum": 12, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Brave result country; defaults to us", "enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Brave UI language; defaults to en-us", "enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Add entity name, description, category, and image to suggestions Brave resolves to a known entity; defaults to false", "in": "query", "name": "rich", "type": "boolean", "x-example": false}], "path": "/brave/suggest", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "count", "type": "integer"}, {"enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string"}, {"enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string"}, {"in": "query", "name": "rich", "type": "boolean"}], "security": ["ApiKeyAuth"]}, "brave-videos": {"bodyParam": null, "bodyRequired": false, "id": "brave-videos", "method": "GET", "params": [{"description": "Search query", "in": "query", "name": "q", "required": true, "type": "string", "x-example": "openai"}, {"description": "Zero-based Brave result page; defaults to 0", "in": "query", "minimum": 0, "name": "offset", "type": "integer", "x-example": 0}, {"description": "Results to return; defaults to 10, clamped to 1..50", "in": "query", "maximum": 50, "minimum": 1, "name": "count", "type": "integer", "x-example": 10}, {"description": "Brave result country; defaults to us", "enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string", "x-example": "us"}, {"description": "Brave UI language; defaults to en-us", "enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string", "x-example": "en-us"}, {"description": "Preset time filter: any, day, week, month, year, or custom", "enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"description": "Custom start date in YYYY-MM-DD; requires date_to", "in": "query", "name": "date_from", "type": "string", "x-example": "2026-03-01"}, {"description": "Custom end date in YYYY-MM-DD; requires date_from", "in": "query", "name": "date_to", "type": "string", "x-example": "2026-03-30"}], "path": "/brave/videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "q", "required": true, "type": "string"}, {"in": "query", "name": "offset", "type": "integer"}, {"in": "query", "name": "count", "type": "integer"}, {"enum": ["all", "ar", "at", "au", "be", "br", "ca", "ch", "cl", "cn", "de", "dk", "es", "fi", "fr", "gb", "gr", "hk", "id", "in", "it", "jp", "kr", "mx", "my", "nl", "no", "nz", "ph", "pl", "pt", "ru", "sa", "se", "sg", "tr", "tw", "us", "za"], "in": "query", "name": "country", "type": "string"}, {"enum": ["de-de", "en-ca", "en-gb", "en-in", "en-us", "fi-fi", "fr-ca", "fr-fr", "ja-jp", "pt-br", "sq-al", "sw-ke", "zh-tw"], "in": "query", "name": "lang", "type": "string"}, {"enum": ["any", "day", "week", "month", "year", "custom"], "in": "query", "name": "time_range", "type": "string"}, {"in": "query", "name": "date_from", "type": "string"}, {"in": "query", "name": "date_to", "type": "string"}], "security": ["ApiKeyAuth"]}}
JSON, true, 512, JSON_THROW_ON_ERROR);
    }

    public function request(string $operationId, array $params = [], string $responseType = 'auto'): mixed
    {
        if ($this->closed) {
            throw new ClientException('Client is closed', null, $operationId);
        }
        $operation = self::$operations[$operationId] ?? null;
        if ($operation === null) {
            throw new ClientException('Unknown operation: ' . $operationId, null, $operationId);
        }
        if ($this->apiKey === '') {
            throw new ClientException('Crawlora API key is required', null, $operationId);
        }
        $payload = $this->requestBody($operation, $params);
        $url = $this->buildUrl($operation, $params);
        $headers = [
            'x-api-key: ' . $this->apiKey,
            'User-Agent: crawlora-brave-php/0.1.0',
            'Accept: ' . (in_array('text/plain', $operation['produces'], true) ? 'application/json, text/plain' : 'application/json'),
        ];
        if ($payload !== null) {
            $headers[] = 'Content-Type: application/json';
        }
        try {
            [$status, $contentType, $body] = $this->send($url, $headers, $operationId, $operation['method'], $payload);
        } catch (CrawloraException $exception) {
            throw $exception;
        } catch (\Throwable $exception) {
            throw new NetworkException('Crawlora request failed: ' . $exception->getMessage(), null, $operationId, null, $exception);
        }
        if ($status < 200 || $status >= 300) {
            $class = $status >= 500 ? ServerException::class : ClientException::class;
            throw new $class('Crawlora returned HTTP ' . $status, $status, $operationId, $body);
        }
        return $this->parseResponse($body, $contentType, $operation, $params, $responseType);
    }

    public function close(): void
    {
        $this->closed = true;
    }

    public function isClosed(): bool
    {
        return $this->closed;
    }

    public function operationCount(): int
    {
        return self::OPERATION_COUNT;
    }

    public function operationIds(): array
    {
        return self::OPERATION_IDS;
    }

    public function operations(): array
    {
        return self::$operations;
    }

    public function images(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("brave-images", $params, $responseType);
    }
    public function news(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("brave-news", $params, $responseType);
    }
    public function search(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("brave-search", $params, $responseType);
    }
    public function suggest(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("brave-suggest", $params, $responseType);
    }
    public function videos(mixed ...$params): mixed
    {
        $responseType = $params['_response_type'] ?? $params['response_type'] ?? 'auto';
        unset($params['_response_type'], $params['response_type']);
        return $this->request("brave-videos", $params, $responseType);
    }

    /** POST operations take their JSON body under the body parameter name or "body". */
    private function requestBody(array $operation, array $params): ?string
    {
        $name = $operation['bodyParam'] ?? null;
        if ($name === null) {
            return null;
        }
        $value = $params[$name] ?? ($params['body'] ?? null);
        if ($value === null) {
            if ($operation['bodyRequired'] ?? false) {
                throw new ClientException('Missing request body: ' . $name, null, $operation['id']);
            }
            return null;
        }
        return is_string($value) ? $value : json_encode($value, JSON_THROW_ON_ERROR);
    }

    private function buildUrl(array $operation, array $params): string
    {
        $known = array_column($operation['params'], 'name');
        if (($operation['bodyParam'] ?? null) !== null) {
            $known[] = 'body';
        }
        $unknown = array_diff(array_keys($params), $known, ['response_type', '_response_type']);
        if ($unknown !== []) {
            throw new ClientException('Unknown parameters: ' . implode(', ', $unknown), null, $operation['id']);
        }
        $path = $operation['path'];
        foreach ($operation['params'] as $param) {
            if ($param['in'] !== 'path') {
                continue;
            }
            $name = $param['name'];
            if (!array_key_exists($name, $params) || $params[$name] === null) {
                throw new ClientException('Missing path parameter: ' . $name, null, $operation['id']);
            }
            $path = str_replace('{' . $name . '}', rawurlencode((string) $params[$name]), $path);
        }
        $pairs = [];
        foreach ($operation['queryParams'] as $param) {
            $name = $param['name'];
            $value = $params[$name] ?? ($param['default'] ?? null);
            if ($value === null) {
                if ($param['required'] ?? false) {
                    throw new ClientException('Missing query parameter: ' . $name, null, $operation['id']);
                }
                continue;
            }
            $enumValues = $param['enum'] ?? ($param['items']['enum'] ?? null);
            $values = is_array($value) ? $value : [$value];
            $invalidEnum = false;
            foreach ($values as $item) {
                if ($enumValues !== null && !in_array((string) $item, array_map('strval', $enumValues), true)) {
                    $invalidEnum = true;
                    break;
                }
            }
            if ($invalidEnum) {
                throw new ClientException('Invalid value for ' . $name, null, $operation['id']);
            }
            if (is_array($value)) {
                $format = $param['collectionFormat'] ?? 'csv';
                if ($format === 'multi') {
                    foreach ($value as $item) {
                        $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($item))];
                    }
                } else {
                    $separator = ['csv' => ',', 'ssv' => ' ', 'tsv' => "\t", 'pipes' => '|'][$format] ?? ',';
                    $pairs[] = [rawurlencode($name), rawurlencode(implode($separator, array_map([$this, 'stringify'], $value)))];
                }
            } else {
                $pairs[] = [rawurlencode($name), rawurlencode($this->stringify($value))];
            }
        }
        $query = implode('&', array_map(static fn(array $pair): string => $pair[0] . '=' . $pair[1], $pairs));
        return $this->baseUrl . $path . ($query === '' ? '' : '?' . $query);
    }

    private function stringify(mixed $value): string
    {
        if (is_bool($value)) {
            return $value ? 'true' : 'false';
        }
        if (is_array($value)) {
            return json_encode($value, JSON_THROW_ON_ERROR);
        }
        return (string) $value;
    }

    private function send(string $url, array $headers, string $operationId, string $method = 'GET', ?string $payload = null): array
    {
        if ($this->transport !== null) {
            $result = $method === 'POST'
                ? ($this->transport)($url, $headers, $this->timeout, $method, $payload)
                : ($this->transport)($url, $headers, $this->timeout);
            return [(int) $result['status'], (string) ($result['content_type'] ?? ''), (string) ($result['body'] ?? '')];
        }
        $handle = curl_init($url);
        if ($handle === false) {
            throw new NetworkException('Could not initialize cURL', null, $operationId);
        }
        curl_setopt_array($handle, $method === 'POST' ? [
            CURLOPT_POST => true,
            CURLOPT_POSTFIELDS => $payload ?? '',
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ] : [
            CURLOPT_HTTPGET => true,
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_HTTPHEADER => $headers,
            CURLOPT_TIMEOUT_MS => (int) ($this->timeout * 1000),
            CURLOPT_CONNECTTIMEOUT_MS => (int) ($this->timeout * 1000),
        ]);
        $body = curl_exec($handle);
        if ($body === false) {
            $message = curl_error($handle);
            curl_close($handle);
            throw new NetworkException('Crawlora request failed: ' . $message, null, $operationId);
        }
        $status = (int) curl_getinfo($handle, CURLINFO_RESPONSE_CODE);
        $contentType = (string) curl_getinfo($handle, CURLINFO_CONTENT_TYPE);
        curl_close($handle);
        return [$status, $contentType, (string) $body];
    }

    private function parseResponse(string $body, string $contentType, array $operation, array $params, string $responseType): mixed
    {
        if (!in_array($responseType, ['auto', 'json', 'text'], true)) {
            throw new ClientException('responseType must be auto, json, or text', null, $operation['id']);
        }
        $format = null;
        foreach ($operation['params'] as $param) {
            if ($param['name'] === 'format') {
                $format = $param;
                break;
            }
        }
        $textFormats = array_values(array_filter($format['enum'] ?? [], static fn($value): bool => !in_array(strtolower((string) $value), ['json', 'application/json'], true)));
        $rawFormat = isset($params['format']) && in_array((string) $params['format'], array_map('strval', $textFormats), true);
        $jsonFormat = isset($params['format']) && in_array(strtolower((string) $params['format']), ['json', 'application/json'], true);
        $isJson = $jsonFormat || stripos($contentType, 'json') !== false || $operation['produces'] === ['application/json'];
        if ($responseType === 'text' || $rawFormat || ($responseType === 'auto' && !$isJson)) {
            return $body;
        }
        try {
            return json_decode($body, true, 512, JSON_THROW_ON_ERROR);
        } catch (\JsonException $exception) {
            throw new CrawloraException('Invalid JSON response from Crawlora: ' . $exception->getMessage(), null, $operation['id'], $body, $exception);
        }
    }
}
