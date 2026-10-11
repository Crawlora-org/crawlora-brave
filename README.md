# Brave Search clients for Crawlora

Official Crawlora client packages for the hosted Brave Search API. These clients call Crawlora's hosted API; they do not scrape Brave Search locally. Requests use your Crawlora account and `CRAWLORA_API_KEY`; service usage follows your account billing plan. Crawlora is independent from and not affiliated with or endorsed by Brave Search or its owners.

## Language packages

- JavaScript / TypeScript: [`@crawlora-org/brave`](javascript/README.md)
- Python: [`crawlora-brave`](python/README.md)
- Go: [`github.com/Crawlora-org/crawlora-brave`](go.mod)
- Ruby: [`crawlora-brave`](ruby/README.md)
- Java: [`net.crawlora:crawlora-brave:0.1.0`](java/README.md)
- PHP: [`crawlora/brave`](php/README.md)

For installation and runnable examples, use the README for your language. See the [API endpoint and parameter reference](docs/usage.md) for shared operation details.

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-signup), open the [Crawlora console](https://crawlora.net/app?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-console) to get an API key, or read the [API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-repository-api-docs). Keep `CRAWLORA_API_KEY` out of source control.

## API coverage

The six clients provide access to 5 public API operations. See the [API reference](docs/usage.md) for supported operations, parameters, and response details.

## License

MIT. See [LICENSE](LICENSE).
