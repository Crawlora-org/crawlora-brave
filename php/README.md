# Crawlora Brave Search API client for PHP (`crawlora/brave`)

This PHP package calls Crawlora's hosted Brave Search API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering web, news, image, and video search plus query suggestions. It does not call or scrape Brave Search directly. Requests require a Crawlora API key and use your Crawlora account's service plan.

## Install

```sh
composer require crawlora/brave
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-php-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-php-console) to get an API key, then set `CRAWLORA_API_KEY` in your environment.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$client = new Crawlora\Brave\Client(apiKey: getenv('CRAWLORA_API_KEY'));
$result = $client->request("brave-search", ['q' => 'sample']);
print_r($result);
$client->close();
```

The client uses PHP cURL and JSON. Constructor options are `apiKey`, `baseUrl`, and `timeout`. Call the operation-specific method for direct access to each supported operation, or `request($operationId, $params, $responseType)` to dispatch by operation ID. Set `$responseType` to `text` for raw text output such as transcript formats. The package includes 5 API operations.

## Supported Brave Search API endpoints

Browse every route included in this Composer package. The [endpoint reference](https://github.com/Crawlora-org/crawlora-brave/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/brave/images` | `brave-images` | Search Brave image results |
| `GET` | `/brave/news` | `brave-news` | Search Brave news results |
| `GET` | `/brave/search` | `brave-search` | Search Brave |
| `GET` | `/brave/suggest` | `brave-suggest` | Suggest Brave search queries |
| `GET` | `/brave/videos` | `brave-videos` | Search Brave video results |

See [Crawlora](https://crawlora.net/?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-php-homepage), the [API documentation](https://crawlora.net/docs?utm_source=packagist&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-php-api-docs), and the [PHP client source](https://github.com/Crawlora-org/crawlora-brave). The complete operation and parameter reference is in the [platform repository](https://github.com/Crawlora-org/crawlora-brave/blob/main/docs/usage.md).
