# Brave Search clients for Crawlora

Official Crawlora client packages for the hosted Brave Search API. Access 5 API endpoints covering web, news, image, and video search plus query suggestions from JavaScript/TypeScript, Python, Go, Ruby, Java, PHP, and Rust. These clients call Crawlora's hosted API; they do not scrape Brave Search locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Brave Search or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/brave`](javascript/README.md)
- Python: [`crawlora-brave`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-brave`](go.mod)
- Ruby: [`crawlora-brave`](ruby/README.md)
- Java: [`net.crawlora:crawlora-brave:0.2.0`](java/README.md)
- PHP: [`crawlora/brave`](php/README.md)
- Rust: [`crawlora-brave`](rust/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage and supported endpoints

The seven language clients provide access to all 5 selected public Brave Search API operations. Search or browse by endpoint path and operation ID below; the [complete API reference](docs/usage.md) adds parameters, enums, and response details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/brave/images` | `brave-images` | Search Brave image results |
| `GET` | `/brave/news` | `brave-news` | Search Brave news results |
| `GET` | `/brave/search` | `brave-search` | Search Brave |
| `GET` | `/brave/suggest` | `brave-suggest` | Suggest Brave search queries |
| `GET` | `/brave/videos` | `brave-videos` | Search Brave video results |

## License

MIT. See [LICENSE](LICENSE).
