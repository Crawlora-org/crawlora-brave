# @crawlora-org/brave — Brave Search API client for JavaScript and TypeScript

JavaScript and TypeScript client for Crawlora's hosted Brave Search API.
It exposes 5 API endpoints for web, news, image, and video search plus query suggestions through [Crawlora](https://crawlora.net/?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-javascript-homepage). It does not run a browser or scrape Brave Search locally. A Crawlora account and `CRAWLORA_API_KEY` are required, and API use is billed under your Crawlora account. Crawlora is independent from and not endorsed by Brave Search or its owners.

## Install

```sh
npm install @crawlora-org/brave
```

## Get an API key

Create an account at [crawlora.net](https://crawlora.net/signup?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-javascript-signup), then open the [Crawlora console](https://crawlora.net/app?utm_source=npm&utm_medium=referral&utm_campaign=platform-clients&utm_content=brave-javascript-console) for API-key setup. Set your key in the shell before running the client:

```sh
export CRAWLORA_API_KEY="your-crawlora-api-key"
```

## Use

Save this example as `example.mjs`, then run `node example.mjs` after installing the package and setting your API key.

```js
import process from "node:process";
import { BraveClient } from "@crawlora-org/brave";

const apiKey = process.env.CRAWLORA_API_KEY;
if (!apiKey) throw new Error("Set CRAWLORA_API_KEY before running this example.");
const client = new BraveClient({ apiKey });
const result1 = await client.search({ q: "open source web crawler" });
console.log(result1);
const result2 = await client.suggest({ q: "open source" });
console.log(result2);
```

The client also exports `Client` as an alias for `BraveClient`. Operation
methods are available directly in camelCase and through the `brave`
group. See the full method and parameter list in the [online reference](https://github.com/Crawlora-org/crawlora-brave/blob/main/docs/usage.md).

Methods return promises and can be awaited. See the [runnable example](https://github.com/Crawlora-org/crawlora-brave/blob/main/examples/javascript.mjs) for a complete usage example.

## Supported Brave Search API endpoints

This package exposes each route below as a direct method and through the `brave` group. See the [endpoint and parameter reference](https://github.com/Crawlora-org/crawlora-brave/blob/main/docs/usage.md) for complete input details.

| Method | Endpoint | API operation | Description |
| --- | --- | --- | --- |
| `GET` | `/brave/images` | `brave-images` | Search Brave image results |
| `GET` | `/brave/news` | `brave-news` | Search Brave news results |
| `GET` | `/brave/search` | `brave-search` | Search Brave |
| `GET` | `/brave/suggest` | `brave-suggest` | Suggest Brave search queries |
| `GET` | `/brave/videos` | `brave-videos` | Search Brave video results |

## Configuration

Pass your key through `apiKey` or set `CRAWLORA_API_KEY` and read it from the
environment. Keep credentials out of source control and logs. Requests are
made to Crawlora's hosted API. Response data and availability depend on
Crawlora's current API behavior.
