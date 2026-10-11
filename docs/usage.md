# Brave Search API endpoint reference and client usage

This reference lists all 5 public Brave Search API endpoints exposed by the `@crawlora-org/brave` and `crawlora-brave` packages, covering web, news, image, and video search plus query suggestions. The clients call Crawlora's hosted API. Set `CRAWLORA_API_KEY` to a key for your Crawlora account before making requests. Service usage is billed under that account. These clients do not run a browser or scrape Brave Search locally; Crawlora is independent from and not endorsed by Brave Search or its owners.

The package tracks the public API contract revision `sha256:2548401e77b60108e6195aa3c83842dc0c1caa7f04e8c777b61ccab2ca397777` bundled with release `0.1.1`. Maintainers can preview daily contract updates with the repository's `Sync live API contract` workflow; unchanged contracts do not produce package releases.

Both packages expose all 5 operations in the bundled API contract. JavaScript uses camelCase methods and Python uses snake_case methods. Methods also remain available through the `brave` group and the generated `Client` alias.

## Examples

The checked-in examples discover current entities or feeds before making the related requests, using parameter names and values supported by the API contract:

- [JavaScript](../examples/javascript.mjs)
- [Python](../examples/python.py)



## Complete operation reference

Required and optional parameter names below come from this package's generated OpenAPI contract. Path parameters are passed alongside query and body values in the same method argument object/keywords.

| Method | Endpoint | Parameters | Description |
| --- | --- | --- | --- |
| `images` / `images` | `GET /brave/images` | `q` (query, required), `offset` (query, optional), `count` (query, optional), `country` (query, optional; values: `all`, `ar`, `at`, `au`, `be`, `br`, `ca`, `ch`, `cl`, `cn`, `de`, `dk`, `es`, `fi`, `fr`, `gb`, `gr`, `hk`, `id`, `in`, `it`, `jp`, `kr`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `sa`, `se`, `sg`, `tr`, `tw`, `us`, `za`), `lang` (query, optional; values: `de-de`, `en-ca`, `en-gb`, `en-in`, `en-us`, `fi-fi`, `fr-ca`, `fr-fr`, `ja-jp`, `pt-br`, `sq-al`, `sw-ke`, `zh-tw`) | Search Brave image results |
| `news` / `news` | `GET /brave/news` | `q` (query, required), `offset` (query, optional), `count` (query, optional), `country` (query, optional; values: `all`, `ar`, `at`, `au`, `be`, `br`, `ca`, `ch`, `cl`, `cn`, `de`, `dk`, `es`, `fi`, `fr`, `gb`, `gr`, `hk`, `id`, `in`, `it`, `jp`, `kr`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `sa`, `se`, `sg`, `tr`, `tw`, `us`, `za`), `lang` (query, optional; values: `de-de`, `en-ca`, `en-gb`, `en-in`, `en-us`, `fi-fi`, `fr-ca`, `fr-fr`, `ja-jp`, `pt-br`, `sq-al`, `sw-ke`, `zh-tw`), `time_range` (query, optional; values: `any`, `day`, `week`, `month`, `year`, `custom`), `date_from` (query, optional), `date_to` (query, optional) | Search Brave news results |
| `search` / `search` | `GET /brave/search` | `q` (query, required), `offset` (query, optional), `country` (query, optional; values: `all`, `ar`, `at`, `au`, `be`, `br`, `ca`, `ch`, `cl`, `cn`, `de`, `dk`, `es`, `fi`, `fr`, `gb`, `gr`, `hk`, `id`, `in`, `it`, `jp`, `kr`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `sa`, `se`, `sg`, `tr`, `tw`, `us`, `za`), `lang` (query, optional; values: `de-de`, `en-ca`, `en-gb`, `en-in`, `en-us`, `fi-fi`, `fr-ca`, `fr-fr`, `ja-jp`, `pt-br`, `sq-al`, `sw-ke`, `zh-tw`), `time_range` (query, optional; values: `any`, `day`, `week`, `month`, `year`, `custom`), `date_from` (query, optional), `date_to` (query, optional) | Search Brave |
| `suggest` / `suggest` | `GET /brave/suggest` | `q` (query, required), `count` (query, optional), `country` (query, optional; values: `all`, `ar`, `at`, `au`, `be`, `br`, `ca`, `ch`, `cl`, `cn`, `de`, `dk`, `es`, `fi`, `fr`, `gb`, `gr`, `hk`, `id`, `in`, `it`, `jp`, `kr`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `sa`, `se`, `sg`, `tr`, `tw`, `us`, `za`), `lang` (query, optional; values: `de-de`, `en-ca`, `en-gb`, `en-in`, `en-us`, `fi-fi`, `fr-ca`, `fr-fr`, `ja-jp`, `pt-br`, `sq-al`, `sw-ke`, `zh-tw`), `rich` (query, optional) | Suggest Brave search queries |
| `videos` / `videos` | `GET /brave/videos` | `q` (query, required), `offset` (query, optional), `count` (query, optional), `country` (query, optional; values: `all`, `ar`, `at`, `au`, `be`, `br`, `ca`, `ch`, `cl`, `cn`, `de`, `dk`, `es`, `fi`, `fr`, `gb`, `gr`, `hk`, `id`, `in`, `it`, `jp`, `kr`, `mx`, `my`, `nl`, `no`, `nz`, `ph`, `pl`, `pt`, `ru`, `sa`, `se`, `sg`, `tr`, `tw`, `us`, `za`), `lang` (query, optional; values: `de-de`, `en-ca`, `en-gb`, `en-in`, `en-us`, `fi-fi`, `fr-ca`, `fr-fr`, `ja-jp`, `pt-br`, `sq-al`, `sw-ke`, `zh-tw`), `time_range` (query, optional; values: `any`, `day`, `week`, `month`, `year`, `custom`), `date_from` (query, optional), `date_to` (query, optional) | Search Brave video results |

## Client forms

- JavaScript: import `BraveClient` (also exported as `Client`) from `@crawlora-org/brave`; use `new BraveClient({ apiKey })` and `await client.method({ ... })`.
- Python: import `BraveClient` (also exported as `Client`) from `crawlora_brave`; use `with BraveClient(api_key=...) as client` and `client.method(...)`.
- Python async class: `AsyncBraveClient`, used with `async with` and `await`.

See the package READMEs for installation details. Keep API keys in environment variables or a secret store; do not commit them.
