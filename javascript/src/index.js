import { groups } from "./operations.js";
import {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
} from "./client.js";

export class BraveClient extends CrawloraClient {
  constructor(options = {}) {
    super({ ...options, userAgent: options.userAgent ?? "crawlora-brave-js/0.2.0" });
    this["images"] = (...args) => this.request("brave-images", ...args);
    this["news"] = (...args) => this.request("brave-news", ...args);
    this["search"] = (...args) => this.request("brave-search", ...args);
    this["suggest"] = (...args) => this.request("brave-suggest", ...args);
    this["videos"] = (...args) => this.request("brave-videos", ...args);
  }
}

export { BraveClient as Client };
export {
  CrawloraClient,
  CrawloraClientError,
  CrawloraError,
  CrawloraNetworkError,
  CrawloraServerError
};
export { groups, operations, operationCount, OperationIds } from "./operations.js";
export const VERSION = "0.2.0";
export default BraveClient;
