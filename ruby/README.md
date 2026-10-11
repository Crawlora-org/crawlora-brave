# Crawlora Brave Search API client for Ruby (`crawlora-brave`)

This Ruby gem calls Crawlora's hosted Brave Search API at `https://api.crawlora.net/api/v1`. It exposes 5 endpoints covering web, news, image, and video search plus query suggestions; it does not call or scrape Brave Search directly. Requests require your Crawlora API key and use your account's service plan.

## Install

```ruby
gem "crawlora-brave"
```

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-console) to get an API key, and set `CRAWLORA_API_KEY` before running the client:

```ruby
require "json"
require "crawlora/brave"

client = Crawlora::Brave::Client.new
result = client.request("brave-search", JSON.parse("{\"q\": \"sample\"}"))
puts result
client.close
```

Use an operation-specific method for normal calls. `request(operation_id, params = {}, response_type: :auto)` is available for every operation. `response_type: :text` returns raw response text. This gem includes 5 API operations.

```ruby
client = Crawlora::Brave::Client.new(api_key: ENV.fetch("CRAWLORA_API_KEY"), timeout: 30)
# client.<operation_method>(<endpoint parameters>)
client.close
```

Client options include `api_key`, `base_url`, and `timeout`. Ruby stdlib provides the HTTP and JSON support.

## Supported Brave Search API endpoints

Browse every route included in this gem. The [endpoint reference](https://github.com/Crawlora-org/crawlora-brave/blob/main/docs/usage.md) includes parameter and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/brave/images` | `brave-images` | Search Brave image results |
| `GET` | `/brave/news` | `brave-news` | Search Brave news results |
| `GET` | `/brave/search` | `brave-search` | Search Brave |
| `GET` | `/brave/suggest` | `brave-suggest` | Suggest Brave search queries |
| `GET` | `/brave/videos` | `brave-videos` | Search Brave video results |

See [Crawlora](https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-homepage), the [API documentation](https://crawlora.net/docs?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-ruby-api-docs), and [the package repository](https://github.com/Crawlora-org/crawlora-brave) for account setup, the API operation reference, and release history.
